"""
The PaperConfig pins down a specific set of case studies, one or more for each
project, where each encaspulates a fixed set of revision to evaluate.

This allows users to specify which revisions of what project have to be
analyzed. Furthermore, it allows other users to reproduce the exact same set of
projects and revisions, either with the old experiment automatically or with a
new experiment to compare the results.
"""

import typing as tp
from pathlib import Path

from varats.paper.artefacts import (
    Artefact,
    Artefacts,
    load_artefacts_from_file,
    store_artefacts,
)
from varats.paper.case_study import (
    CaseStudy,
    load_case_study_from_file,
    store_case_study,
)
from varats.utils.settings import vara_cfg


class PaperConfig():
    """
    Paper config, a specific set of case studies, e.g.,  for a publication.

    The paper config allows easy reevaluation of a set of case studies.

    Args:
        folder_path: path to the paper config folder
    """

    def __init__(self, folder_path: Path) -> None:
        self.__path = Path(folder_path)
        self.__case_studies: tp.Dict[str, tp.List[CaseStudy]] = dict()
        for case_study_path in \
                [x for x in self.__path.iterdir()
                 if x.suffix == ".case_study"]:
            case_study = load_case_study_from_file(case_study_path)
            if case_study.project_name in self.__case_studies.keys():
                self.__case_studies[case_study.project_name].append(case_study)
            else:
                self.__case_studies[case_study.project_name] = [case_study]
        if (self.__path / 'artefacts.yaml').exists():
            self.__artefacts = load_artefacts_from_file(
                self.__path / 'artefacts.yaml'
            )
        else:
            self.__artefacts = Artefacts([])

    @property
    def path(self) -> Path:
        """Path to the paper config folder."""
        return self.__path

    @property
    def artefacts(self) -> Artefacts:
        """The artefacts of this paper config."""
        return self.__artefacts

    def get_case_studies(self, cs_name: str) -> tp.List[CaseStudy]:
        """
        Lookup all case studies with a given name.

        Args:
            cs_name: name of the case study

        Returns:
            case studies with project name `cs_name`.
        """
        return self.__case_studies[cs_name]

    def get_all_case_studies(self) -> tp.List[CaseStudy]:
        """
        Generate a list of all case studies in the paper config.

        Returns:
            full list of all case studies with all different version.
        """
        return [
            case_study for case_study_list in self.__case_studies.values()
            for case_study in case_study_list
        ]

    def get_all_artefacts(self) -> tp.Iterable[Artefact]:
        """Returns an iterable of the artefacts of this paper config."""
        if self.__artefacts:
            return self.__artefacts
        return []

    def has_case_study(self, cs_name: str) -> bool:
        """
        Checks if a case study with `cs_name` was loaded.

        Args:
            cs_name: name of the case study

        Returns:
            ``True``, if a case study with ``cs_name`` was loaded
        """
        return cs_name in self.__case_studies.keys()

    def get_filter_for_case_study(self,
                                  cs_name: str) -> tp.Callable[[str], bool]:
        """
        Return a case study specific revision filter. If one case study includes
        a revision the filter function will return ``True``. This can be used to
        automatically filter out revisions that are not part of a case study,
        loaded by this paper config.

        Args:
            cs_name: name of the case study

        Returns:
            a filter function that checks if a given revision is part of a
            case study with name ``cs_name`` and returns ``True`` if it was
        """
        if self.has_case_study(cs_name):
            rev_filters = [
                cs.get_revision_filter()
                for cs in self.get_case_studies(cs_name)
            ]

            def multi_case_study_rev_filter(revision: str) -> bool:
                for rev_filter in rev_filters:
                    if rev_filter(revision):
                        return True
                return False

            return multi_case_study_rev_filter

        return lambda x: False

    def add_case_study(self, case_study: CaseStudy) -> None:
        """
        Add a new case study to this paper config.

        Args:
            case_study: to be added
        """
        self.__case_studies[case_study.project_name] += [case_study]

    def add_artefact(self, artefact: Artefact) -> None:
        """
        Add a new artefact to this paper config.

        Args:
            artefact: the artefact to add
        """
        self.__artefacts.add_artefact(artefact)

    def store(self) -> None:
        """Persist the current state of the paper config saving all case studies
        to their corresponding files in the paper config path."""
        for case_study_list in self.__case_studies.values():
            for case_study in case_study_list:
                store_case_study(case_study, self.__path)
        if self.__artefacts:
            store_artefacts(self.__artefacts, self.__path)

    def __str__(self) -> str:
        string = "Loaded case studies:\n"
        for case_study_list in self.__case_studies.values():
            for case_study in case_study_list:
                string += case_study.project_name
        return string


__G_PAPER_CONFIG: tp.Optional[PaperConfig] = None


def project_filter_generator(project_name: str) -> tp.Callable[[str], bool]:
    """
    Generate project specific revision filters.

    - if no paper config is loaded, we allow all revisions
    - otherwise the paper config generates a specific revision filter

    Args:
        project_name: corresponding project name

    Returns:
        a filter function that returns ``True`` if a revision of the specified
        project is included in one of the related case studies.
    """
    if vara_cfg()["paper_config"]["current_config"].value is None:
        return lambda x: True

    if not is_paper_config_loaded():
        load_paper_config(
            Path(
                str(vara_cfg()["paper_config"]["folder"]) + "/" +
                str(vara_cfg()["paper_config"]["current_config"])
            )
        )

    return get_paper_config().get_filter_for_case_study(project_name)


def get_loaded_paper_config() -> PaperConfig:
    """
    Returns the currently active paper config, this requires a config to be
    loaded before use.

    Returns:
        currently active paper config
    """
    if __G_PAPER_CONFIG is None:
        raise Exception('Paper config was not loaded')
    return __G_PAPER_CONFIG


def is_paper_config_loaded() -> bool:
    """
    Check if a currently a paper config is loaded.

    Returns:
        ``True``, if a paper config has been loaded
    """
    return __G_PAPER_CONFIG is not None


def load_paper_config(config_path: tp.Optional[Path] = None) -> None:
    """
    Loads a paper config from a yaml file, initializes the paper config and sets
    it to the currently active paper config. If no config path is provided, the
    paper config set in the vara settings yaml is loaded.

    Note:
        Only one paper config can be active at a time

    Args:
        config_path: path to a paper config folder
    """
    if config_path is None:
        if vara_cfg()["paper_config"]["folder"].value is None or \
                vara_cfg()["paper_config"][
                    "current_config"].value is None:
            raise Exception(
                "No paper config was set in VaRA config file {}".format(
                    vara_cfg()['config_file']
                )
            )
        config_path = Path(
            str(vara_cfg()["paper_config"]["folder"]) + "/" +
            str(vara_cfg()["paper_config"]["current_config"])
        )

    global __G_PAPER_CONFIG  # pylint: disable=global-statement
    __G_PAPER_CONFIG = PaperConfig(config_path)


def get_paper_config() -> PaperConfig:
    """
    Returns the current paper config and loads one if there is currenlty no
    active paper config.

    Returns:
        currently active paper config
    """
    if __G_PAPER_CONFIG is None:
        load_paper_config()
    return get_loaded_paper_config()
