"""Module for the base BlameInteractionDatabase class."""
import typing as tp
from pathlib import Path

import pandas as pd

from varats.data.cache_helper import build_cached_report_table
from varats.data.databases.evaluationdatabase import EvaluationDatabase
from varats.data.report import MetaReport
from varats.data.reports.blame_report import (
    BlameReport,
    generate_in_head_interactions,
    generate_out_head_interactions,
)
from varats.data.reports.commit_report import CommitMap
from varats.data.revisions import (
    get_failed_revisions_files,
    get_processed_revisions_files,
)
from varats.jupyterhelper.file import load_blame_report
from varats.paper.case_study import CaseStudy, get_case_study_file_name_filter


class BlameInteractionDatabase(
    EvaluationDatabase,
    cache_id="blame_interaction_data",
    columns=[
        "IN_HEAD_Interactions", "OUT_HEAD_Interactions", "HEAD_Interactions"
    ]
):
    """Provides access to blame interaction data."""

    @classmethod
    def _load_dataframe(
        cls, project_name: str, commit_map: CommitMap,
        case_study: tp.Optional[CaseStudy], **kwargs: tp.Any
    ) -> pd.DataFrame:

        def create_dataframe_layout() -> pd.DataFrame:
            df_layout = pd.DataFrame(columns=cls.COLUMNS)
            df_layout.IN_HEAD_Interactions = \
                df_layout.IN_HEAD_Interactions.astype('int64')
            df_layout.OUT_HEAD_Interactions = \
                df_layout.OUT_HEAD_Interactions.astype('int64')
            df_layout.HEAD_Interactions = \
                df_layout.HEAD_Interactions.astype('int64')
            return df_layout

        def create_data_frame_for_report(
            report_path: Path
        ) -> tp.Tuple[pd.DataFrame, str, str]:
            report = load_blame_report(report_path)
            in_head_interactions = len(generate_in_head_interactions(report))
            out_head_interactions = len(generate_out_head_interactions(report))

            return pd.DataFrame({
                'revision':
                    report.head_commit,
                'time_id':
                    commit_map.short_time_id(report.head_commit),
                'IN_HEAD_Interactions':
                    in_head_interactions,
                'OUT_HEAD_Interactions':
                    out_head_interactions,
                'HEAD_Interactions':
                    in_head_interactions + out_head_interactions
            },
                                index=[0]), report.head_commit, str(
                                    report_path.stat().st_mtime_ns
                                )

        report_files = get_processed_revisions_files(
            project_name, BlameReport,
            get_case_study_file_name_filter(case_study)
        )

        failed_report_files = get_failed_revisions_files(
            project_name, BlameReport,
            get_case_study_file_name_filter(case_study)
        )

        # cls.CACHE_ID is set by superclass
        # pylint: disable=E1101
        data_frame = build_cached_report_table(
            cls.CACHE_ID, project_name, report_files, failed_report_files,
            create_dataframe_layout, create_data_frame_for_report,
            lambda path: MetaReport.get_commit_hash_from_result_file(path.name),
            lambda path: str(path.stat().st_mtime_ns),
            lambda a, b: int(a) > int(b)
        )

        return data_frame
