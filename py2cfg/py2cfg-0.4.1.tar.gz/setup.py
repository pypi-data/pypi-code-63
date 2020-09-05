# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py2cfg']

package_data = \
{'': ['*']}

install_requires = \
['astor>=0.8.1,<0.9.0', 'graphviz>=0.11,<0.12']

entry_points = \
{'console_scripts': ['py2cfg = py2cfg._runner:main']}

setup_kwargs = {
    'name': 'py2cfg',
    'version': '0.4.1',
    'description': 'Converts python source code to colorful Control Flow Graphs (CFGs).',
    'long_description': "# py2cfg\nPython3 control flow graph generator\n\n`py2cfg` is a package that can be used to produce control flow graphs (CFGs) for Python 3 programs. \nThe CFGs it generates can be easily visualised with graphviz.\nThat graphical analysis is the main purpose of the module.\n\n## Examples\nBelow is an example of a piece of code that generates the Fibonacci sequence and the CFG produced for it with py2cfg:\n\n```py\n# fib.py\n\ndef fib():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\nfib_gen = fib()\nfor _ in range(10):\n    next(fib_gen)\n```\n\n![The image display works in the Gitlab README.md](fib_cfg.png)\n\nAfter cloning, see `./examples/` for some code snippets to run this on.\nTo generate *_cfg.png images for each example, clone this repo and run the following command in the repo root directory:\n```sh\ngit clone repourl\ncd intorepodirectory\n./generate_examples.sh\n```\n\n## Installation via pip3\nNote: installation is not required, but is handy.\n\nTo install simply run\n```sh\npip3 install py2cfg --user\n```\n\nor clone this repo and pip install locally\n```\ngit clone <url>\ncd intoprojectdirectory\npip3 install . --user\n```\n\n## Usage\nIt can be used three ways:\n\n### Run via shell command\nIf you have installed, then the default command is py2cfg:\n```py\npy2cfg <file.py>\n``` \nThis will create a <file>_cfg.png file, which contains the colored cfg of the file.\nIf you don't want to install via pip, the innards of the py2cfg command can be run right from the repo:\n\n### Via wrapper\nIf you have not installed, then you can run a script present in the repo, py2cfg/_runner.py, to directly generate a CFG of a Python program and visualise it:\n```sh\ncd intoreporootdir\npython3 py2cfg/_runner.py path_to_my_code.py\n```\n\n### Via import\nWhether or not you have installed (easier if you have), to use py2cfg in your own python code, simply import the module in your Python interpreter or program.\nThen use the `py2cfg.CFGBuilder` class to build CFGs. \nFor example, to build the CFG of a program defined in a file with the path *./example.py*, the following code can be used:\n\n```py\nfrom py2cfg import CFGBuilder\n\ncfg = CFGBuilder().build_from_file('example', './example.py')\n```\n\nThis returns the CFG for the code in *./example.py* in the `cfg` variable. \nThe first parameter of `build_from_file` is the desired name for the CFG, and the second one is the path to the file containing the source code.\nThe produced CFG can then be visualised with:\n\n```py\ncfg.build_visual('exampleCFG', 'pdf')\n```\n\nThe first paramter of `build_visual` is the desired name for the DOT file produced by the method, and the second one is the format to use for the visualisation.\n\n\n# Contributing\n\n## Issues\nModifications and improvements to this project are driven via Gitlab-Issues.\nCheck them out to create one, or fix one.\n\n## Unit tests \nOur minimal tests are run via Gitlab-CI. \nMake sure you don't break them!\n* [ ] This is a current task: the tests work locally, but not all work on Gitlab-CI...\n\n## Type hinting\nNote: any new additions to the project should adhere to type-hinting standards enforced by:\n```sh\nmypy --strict --disallow-any-explicit *.py\n```\n* [ ] This is a current issue -- yes we need to fix some things...\n\n## Style\nTo maximize the ability of version control to pin down changes, and keep the style consistent, before you make any commit to the project, run this strict code auto-formatter:\n```sh\nblack py2cfg/*.py\n```\n\n# Project history\nNote: py2cfg is a significantly re-worked and improved fork of the older staticfg project:\n* https://github.com/coetaur0/staticfg\n* https://pypi.org/project/staticfg/\n",
    'author': 'Joe Studer',
    'author_email': 'jmsxw4@mst.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/classroomcode/py2cfg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
