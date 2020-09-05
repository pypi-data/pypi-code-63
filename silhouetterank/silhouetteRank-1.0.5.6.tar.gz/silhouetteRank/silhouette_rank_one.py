import sys
import os
import re
import numpy as np
import subprocess
import math
import scipy
import silhouetteRank.spatial_genes as spatial_genes
from shutil import copyfile
from operator import itemgetter
from scipy.spatial.distance import squareform, pdist
from scipy.stats import percentileofscore
from sklearn.metrics import roc_auc_score
import argparse
import silhouetteRank
import silhouetteRank.prep as prep
import silhouetteRank.evaluate_exact_one_2b as evaluate_exact_one_2b
import silhouetteRank.use_previous_cluster as use_previous_cluster
import silhouetteRank.combine as combine

def main():
	parser = argparse.ArgumentParser(description="silhouette_rank_one.py: calculate silhouette score for randomly distributed spatial patterns", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-x", "--file-expr", dest="expr", type=str, required=True, help="expression matrix. Will use input binary expr.npy (if exists) to speed up reading.")
	parser.add_argument("-c", "--file-centroid", dest="centroid", type=str, required=True, help="cell coordinate. Will use input binary Xcen.npy (if exists) to speed up reading.")
	parser.add_argument("-w", "--overwrite-input-binary", dest="overwrite_input_bin", action="store_true", help="overwrite input binaries")
	parser.add_argument("-r", "--rbp-ps", dest="rbp_ps", nargs="+", type=float, default=[0.95, 0.99], help="p parameter of RBP")
	parser.add_argument("-e", "--examine-tops", dest="examine_tops", nargs="+", type=float, default=[0.005, 0.010, 0.050, 0.100, 0.300], help="top proportion of cells per gene to be 1's (expressed)")
	parser.add_argument("-m", "--matrix-type", dest="matrix_type", type=str, choices=["sim", "dissim"], help="whether to calculate similarity matrix or dissimilarity matrix", default="dissim")
	parser.add_argument("-l", "--log-dir", dest="logdir", type=str, default="logs", help="log directory")
	parser.add_argument("-p", "--cores", dest="num_core", type=int, default=4, help="number of cores")
	parser.add_argument("-a", "--parallel-path", dest="parallel_path", type=str, default="/usr/bin", help="parallel binary path")
	parser.add_argument("-o", "--output-dir", dest="output", type=str, default=".", help="output directory")
	parser.add_argument("-q", "--query-sizes", dest="query_sizes", type=int, default=10, help="query sizes (advanced user setting)")
	args = parser.parse_args()

	if not os.path.isdir(args.output):
		os.mkdir(args.output)
	if not os.path.isdir(args.logdir):
		os.mkdir(args.logdir)

	fw = open("%s/args" % args.output, "w")
	for rbp_p in args.rbp_ps:
		for examine_top in args.examine_tops:
			for i in range(args.query_sizes):
				fw.write("%.2f\n" % rbp_p)
				fw.write("%.3f\n" % examine_top)
				fw.write("%d\n" % i)
	fw.close()

	fw = open("%s/args.basic" % args.output, "w")
	for rbp_p in args.rbp_ps:
		for examine_top in args.examine_tops:
			fw.write("%.2f\n" % rbp_p)
			fw.write("%.3f\n" % examine_top)
	fw.close()
	

	args1 = argparse.Namespace(expr=args.expr, centroid=args.centroid, rbp_ps=args.rbp_ps, examine_tops=args.examine_tops, matrix_type=args.matrix_type, output=args.output, query_sizes=args.query_sizes, overwrite_input_bin=args.overwrite_input_bin)
	prep.do_one(args1)


	bin_path = os.path.dirname(silhouetteRank.__file__)
	for i in range(4):
		bin_path = os.path.dirname(bin_path)
	bin_path = os.path.join(bin_path, "bin")	

	sys.stderr.write("Start calculating silhouette rank...\n")
	sys.stderr.flush()
	cmd = "cat '%s'/args.basic | '%s'/parallel --jobs %d --max-args=2 \\''%s'\\'''/silhouette_rank_main -x \\''%s'\\''' -c \\''%s'\\''' -r {1} -e {2} -m %s -o \\''%s'\\''' \"2>\" \\''%s'\\'''/real_{1}_{2}.out" % (args.output, args.parallel_path, args.num_core, bin_path, args.expr, args.centroid, args.matrix_type, args.output, args.logdir)
	os.system(cmd)

	sys.stderr.write("Start random...\n")
	sys.stderr.flush()
	cmd="cat '%s'/args | '%s'/parallel --jobs %d --max-args=3 \\''%s'\\'''/silhouette_rank_random -r {1} -e {2} -m %s -o \\''%s'\\''' -q {3} \"2>\" \\''%s'\\'''/{1}_{2}_{3}.out" % (args.output, args.parallel_path, args.num_core, bin_path, args.matrix_type, args.output, args.logdir)
	os.system(cmd)

	for rbp_p in args.rbp_ps:
		for examine_top in args.examine_tops:

			random_dir = "%s/result_sim_5000_%.2f_%.3f" % (args.output, rbp_p, examine_top)
			score_file = "%s/silhouette.sim.exact.rbp.%.2f.top.%.3f.txt" % (args.output, rbp_p, examine_top)
			output_score_file = "%s/silhouette.sim.exact.rbp.%.2f.top.%.3f.pval.txt" % (args.output, rbp_p, examine_top)
			if args.matrix_type=="dissim":
				random_dir = "%s/result_5000_%.2f_%.3f" % (args.output, rbp_p, examine_top)
				score_file = "%s/silhouette.exact.rbp.%.2f.top.%.3f.txt" % (args.output, rbp_p, examine_top)
				output_score_file = "%s/silhouette.exact.rbp.%.2f.top.%.3f.pval.txt" % (args.output, rbp_p, examine_top)
				

			args1 = argparse.Namespace(expr=args.expr, centroid=args.centroid, examine_top=examine_top, input=score_file, input_random=random_dir, output=output_score_file, outdir=args.output, query_sizes=args.query_sizes, overwrite_input_bin=args.overwrite_input_bin)
			use_previous_cluster.do_one(args1)

	combined_file = "%s/silhouette.overall.pval.txt" % args.output
	if args.matrix_type=="sim":
		combined_file = "%s/silhouette.sim.overall.pval.txt" % args.output
	args1 = argparse.Namespace(rbp_ps=args.rbp_ps, examine_tops=args.examine_tops, matrix_type=args.matrix_type, input=args.output, output=combined_file)
	combine.do_one(args1)
	#for i in range(args.query_sizes):
	#	evaluate_exact_one_2b.do_one(args)
	#do_one(args)
	
if __name__=="__main__":
	main()
