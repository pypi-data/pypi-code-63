# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitman', 'gitman.models', 'gitman.tests']

package_data = \
{'': ['*'], 'gitman.tests': ['files/*']}

install_requires = \
['datafiles>=0.11b4,<0.12.0', 'minilog>=2.0b1,<3.0']

entry_points = \
{'console_scripts': ['git-deps = gitman.plugin:main',
                     'gitman = gitman.cli:main']}

setup_kwargs = {
    'name': 'gitman',
    'version': '2.1b4',
    'description': 'A language-agnostic dependency manager using Git.',
    'long_description': '## Overview\n\nGitMan is a language-agnostic dependency manager using Git. It aims to serve as a submodules replacement and provides advanced options for managing versions of nested Git repositories.\n\n![demo](https://raw.githubusercontent.com/jacebrowning/gitman/main/docs/demo.gif)\n\n[![Unix Build Status](https://img.shields.io/travis/jacebrowning/gitman/master.svg?label=unix)](https://travis-ci.org/jacebrowning/gitman)\n[![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/gitman/master.svg?label=window)](https://ci.appveyor.com/project/jacebrowning/gitman)\n[![Coverage Status](https://img.shields.io/coveralls/jacebrowning/gitman/master.svg)](https://coveralls.io/r/jacebrowning/gitman)\n[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/jacebrowning/gitman.svg)](https://scrutinizer-ci.com/g/jacebrowning/gitman/?branch=master)\n[![PyPI Version](https://img.shields.io/pypi/v/GitMan.svg)](https://pypi.org/project/GitMan)\n[![PyPI License](https://img.shields.io/pypi/l/GitMan.svg)](https://pypi.org/project/GitMan)\n\n## Setup\n\n### Requirements\n\n- Python 3.6+\n- Git 2.8+ (with [stored credentials](http://gitman.readthedocs.io/en/latest/setup/git/))\n\n### Installation\n\nInstall this tool globally:\n\n```sh\n$ pip install gitman\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n```sh\n$ poetry add gitman\n```\n\n### Configuration\n\nGenerate a sample config file:\n\n```sh\n$ gitman init\n```\n\nor manually create one (`gitman.yml` or `.gitman.yml`) in the root of your working tree:\n\n```yaml\nlocation: vendor/gitman\n\nsources:\n  - name: framework\n    repo: https://github.com/kstenerud/iOS-Universal-Framework\n    rev: Mk5-end-of-life\n  - name: coverage\n    repo: https://github.com/jonreid/XcodeCoverage\n    rev: master\n    link: Tools/XcodeCoverage\n  - name: trufflehog\n    repo: https://github.com/dxa4481/truffleHog\n    rev: master\n    scripts:\n      - chmod a+x truffleHog/truffleHog.py\n  - name: fontawesome\n    repo: https://github.com/FortAwesome/Font-Awesome\n    sparse_paths:\n      - "webfonts/*"\n    rev: master\n  - name: material-design-icons\n    repo: https://github.com/google/material-design-icons.git\n    rev: master\n\ngroups:\n  - name: code\n    members:\n      - framework\n      - trufflehog\n  - name: resources\n    members:\n      - fontawesome\n      - material-design-icons\n```\n\nIgnore the dependency storage location:\n\n```sh\n$ echo vendor/gitman >> .gitignore\n```\n\n## Usage\n\nSee the available commands:\n\n```sh\n$ gitman --help\n```\n\n### Updating Dependencies\n\nGet the latest versions of all dependencies:\n\n```sh\n$ gitman update\n```\n\nwhich will essentially:\n\n1. Create a working tree at `<root>`/`<location>`/`<name>`\n2. Fetch from `repo` and checkout the specified `rev`\n3. Symbolically link each `<location>`/`<name>` from `<root>`/`<link>` (if specified)\n4. Repeat for all nested working trees containing a config file\n5. Record the actual commit SHAs that were checked out (with `--lock` option)\n6. Run optional post-install scripts for each dependency\n\nwhere `rev` can be:\n\n- all or part of a commit SHA: `123def`\n- a tag: `v1.0`\n- a branch: `main`\n- a `rev-parse` date: `\'main@{2015-06-18 10:30:59}\'`\n\nAlternatively get the latest versions of certain dependencies or even dependency groups:\n\n- Update a single repository\n\n```sh\n$ gitman update framework\n```\n\n- Update a dependency group\n\n```sh\n$ gitman update resources\n```\n\n### Restoring Previous Versions\n\nDisplay the specific revisions that are currently installed:\n\n```sh\n$ gitman list\n```\n\nReinstall these specific versions at a later time:\n\n```sh\n$ gitman install\n```\n\n### Deleting Dependencies\n\nRemove all installed dependencies:\n\n```sh\n$ gitman uninstall\n```\n',
    'author': 'Jace Browning',
    'author_email': 'jacebrowning@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/gitman',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
