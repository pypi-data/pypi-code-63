#!/usr/bin/env python3

"""
Template by pypi-mobans
"""

import os
import sys
import codecs
import locale
import platform
from shutil import rmtree

from setuptools import Command, setup, find_packages
from setuptools import __version__ as setuptools_version
from pkg_resources import parse_version

import pkg_resources

try:
    import _markerlib.markers
except ImportError:
    _markerlib = None

PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7
PY33 = sys.version_info < (3, 4)

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
# This work around is only if a project supports Python < 3.4

# Work around for locale not being set
try:
    lc = locale.getlocale()
    pf = platform.system()
    if pf != "Windows" and lc == (None, None):
        locale.setlocale(locale.LC_ALL, "C.UTF-8")
except (ValueError, UnicodeError, locale.Error):
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

NAME = "moban"
AUTHOR = "chfw"
VERSION = "0.8.1"
EMAIL = "wangc_2011@hotmail.com"
LICENSE = "MIT"
ENTRY_POINTS = {
    "console_scripts": [
        "moban = moban.main:main"
    ],
}
DESCRIPTION = (
    "General purpose static text generator"
)
URL = "https://github.com/moremoban/moban"
DOWNLOAD_URL = "%s/archive/0.8.1.tar.gz" % URL
FILES = ["README.rst", "CONTRIBUTORS.rst", "CHANGELOG.rst"]
KEYWORDS = [
    "python",
    "jinja2",
    "moban",
]

CLASSIFIERS = [
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python",
    "Intended Audience :: Developers",

    "Programming Language :: Python :: 3 :: Only",



    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",

]

PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    "jinja2>=2.7.1",
    "lml>=0.0.9",
    "appdirs>=1.4.3",
    "crayons>= 0.1.0",
    "fs>=2.4.11",
    "jinja2-fsloader>=0.2.0",
    "moban-jinja2-github",
]
SETUP_COMMANDS = {}

PACKAGES = find_packages(exclude=["ez_setup", "examples", "tests", "tests.*"])
EXTRAS_REQUIRE = {
    ":python_version == '3.7'": ["ruamel.yaml>=0.15.42"],
    ":python_version != '3.4' and python_version < '3.7'": ["ruamel.yaml>=0.15.5"],
    ":python_version == '3.8'": ["ruamel.yaml>=0.15.98"],
}
# You do not need to read beyond this line
PUBLISH_COMMAND = "{0} setup.py sdist bdist_wheel upload -r pypi".format(sys.executable)
GS_COMMAND = ("gs moban v0.8.1 " +
              "Find 0.8.1 in changelog for more details")
NO_GS_MESSAGE = ("Automatic github release is disabled. " +
                 "Please install gease to enable it.")
UPLOAD_FAILED_MSG = (
    'Upload failed. please run "%s" yourself.' % PUBLISH_COMMAND)
HERE = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package on github and pypi"
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(HERE, "dist"))
            rmtree(os.path.join(HERE, "build"))
            rmtree(os.path.join(HERE, "moban.egg-info"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        run_status = True
        if has_gease():
            run_status = os.system(GS_COMMAND) == 0
        else:
            self.status(NO_GS_MESSAGE)
        if run_status:
            if os.system(PUBLISH_COMMAND) != 0:
                self.status(UPLOAD_FAILED_MSG)

        sys.exit()


SETUP_COMMANDS.update({
    "publish": PublishCommand
})


def has_gease():
    """
    test if github release command is installed

    visit http://github.com/moremoban/gease for more info
    """
    try:
        import gease  # noqa
        return True
    except ImportError:
        return False


def read_files(*files):
    """Read files into setup"""
    text = ""
    for single_file in files:
        content = read(single_file)
        text = text + content + "\n"
    return text


def read(afile):
    """Read a file into setup"""
    the_relative_file = os.path.join(HERE, afile)
    with codecs.open(the_relative_file, "r", "utf-8") as opened_file:
        content = filter_out_test_code(opened_file)
        content = "".join(list(content))
        return content


def filter_out_test_code(file_handle):
    found_test_code = False
    for line in file_handle.readlines():
        if line.startswith(".. testcode:"):
            found_test_code = True
            continue
        if found_test_code is True:
            if line.startswith("  "):
                continue
            else:
                empty_line = line.strip()
                if len(empty_line) == 0:
                    continue
                else:
                    found_test_code = False
                    yield line
        else:
            for keyword in ["|version|", "|today|"]:
                if keyword in line:
                    break
            else:
                yield line


# _markerlib.default_environment() obtains its data from _VARS
# and wraps it in another dict, but _markerlib_evaluate writes
# to the dict while it is iterating the keys, causing an error
# on Python 3 only.
# Replace _markerlib.default_environment to return a custom dict
# that has all the necessary markers, and ignores any writes.

class Python3MarkerDict(dict):

    def __setitem__(self, key, value):
        pass

    def pop(self, i=-1):
        return self[i]


if _markerlib and sys.version_info[0] == 3:
    env = _markerlib.markers._VARS
    for key in list(env.keys()):
        new_key = key.replace(".", "_")
        if new_key != key:
            env[new_key] = env[key]

    _markerlib.markers._VARS = Python3MarkerDict(env)

    def default_environment():
        return _markerlib.markers._VARS

    _markerlib.default_environment = default_environment

# Avoid the very buggy pkg_resources.parser, which does not consistently
# recognise the markers needed by this setup.py
# See https://github.com/pypa/packaging/issues/72 for details
# Change this to setuptools 20.10.0 to support all markers.
if pkg_resources:
    if parse_version(setuptools_version) < parse_version("18.5"):
        MarkerEvaluation = pkg_resources.MarkerEvaluation

        del pkg_resources.parser
        pkg_resources.evaluate_marker = MarkerEvaluation._markerlib_evaluate
        MarkerEvaluation.evaluate_marker = MarkerEvaluation._markerlib_evaluate

if __name__ == "__main__":
    setup(
        test_suite="tests",
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        author_email=EMAIL,
        description=DESCRIPTION,
        url=URL,
        download_url=DOWNLOAD_URL,
        long_description=read_files(*FILES),
        license=LICENSE,
        keywords=KEYWORDS,
        python_requires=PYTHON_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        tests_require=["nose"],
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        entry_points=ENTRY_POINTS,
        classifiers=CLASSIFIERS,
        cmdclass=SETUP_COMMANDS
    )
