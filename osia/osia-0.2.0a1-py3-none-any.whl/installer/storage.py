# -*- coding: utf-8 -*-
#
# Copyright 2020 Osia authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module implements logic for persistence layer of osia

Currently the only supported persistance is via git.
Module is responsible for maintenance of the git repository
and to store the generated artifacts by the `openshift-install
binary."""
import logging
from git import Repo


def check_repository():
    """Function checks local repository if it is up2date with
    remote.
    In case when there is difference between upstream and
    local copy it tries to pull from remote.

    It returns the Repo object and remote associated with
    current tracking branch."""
    rep = Repo("./")
    remote = rep.active_branch.tracking_branch()
    fetches = rep.remotes[remote.remote_name].fetch()
    for fetch in fetches:
        if fetch.name == remote.name and fetch.commit != rep.commit():
            logging.warning("There are changes in remote repository, trying to pull")
            rep.remotes[remote.remote_name].pull()
    if rep.is_dirty():
        logging.warning("There are not committed changes in your repository, please fix this")

    return rep, remote


def write_changes(cluster_directory):
    """Function stages generated directory, which contains files
    generated by openshift-install function, creates commit,
    and pushes to the remote of tracking branch."""
    rep, remote = check_repository()
    rep.index.add(cluster_directory)
    logging.info("Commiting installer changes for cluster %s", cluster_directory)
    rep.index.commit(f"[OCP Installer] installation files for {cluster_directory} added")

    rep.remotes[remote.remote_name].push()


def delete_directory(cluster_directory):
    """Function deletes commited directory both
    from local copy and from the remote repository."""
    rep, remote = check_repository()
    logging.info("Removing cluster directory from git repository %s", cluster_directory)
    rep.index.remove(cluster_directory, working_tree=True, r=True, f=True)
    rep.index.commit(f"[OCP Installer] removed installation files for {cluster_directory}")
    rep.remotes[remote.remote_name].push()
