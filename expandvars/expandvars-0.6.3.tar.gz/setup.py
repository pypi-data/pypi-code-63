# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['expandvars']
setup_kwargs = {
    'name': 'expandvars',
    'version': '0.6.3',
    'description': 'Expand system variables Unix style',
    'long_description': 'expandvars\n==========\nExpand system variables Unix style\n\n[![PyPI version](https://img.shields.io/pypi/v/expandvars.svg)](https://pypi.org/project/expandvars)\n[![codecov](https://codecov.io/gh/sayanarijit/expandvars/branch/master/graph/badge.svg)](https://codecov.io/gh/sayanarijit/expandvars)\n\n\nInspiration\n-----------\nThis module is inspired by [GNU bash\'s variable expansion features](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html). It can be used as an alternative to Python\'s [os.path.expandvars](https://docs.python.org/3/library/os.path.html#os.path.expandvars) function.\n\nA good use case is reading config files with the flexibility of reading values from environment variables using advanced features like returning a default value if some variable is not defined.\nFor example:\n\n```toml\n[default]\nmy_secret_access_code = "${ACCESS_CODE:-default_access_code}"\nmy_important_variable = "${IMPORTANT_VARIABLE:?}"\nmy_updated_path = "$PATH:$HOME/.bin"\nmy_process_id = "$$"\nmy_nested_variable = "${!NESTED}\n```\n\n> NOTE: Although this module copies most of the common behaviours of bash,\n> it doesn\'t follow bash strictly. For example, it doesn\'t work with arrays.\n\n\nUsage\n-----\n\n```python\nfrom expandvars import expandvars\n\nprint(expandvars("$PATH:${HOME:?}/bin:${SOME_UNDEFINED_PATH:-/default/path}"))\n# /bin:/sbin:/usr/bin:/usr/sbin:/home/you/bin:/default/path\n```\n\n\nExamples\n--------\nFor now, [refer to the test cases](https://github.com/sayanarijit/expandvars/blob/master/tests) to see how it behaves.\n\n\nTIPs\n----\n\n### nounset=True\n\nIf you want to enable strict parsing by default, (similar to `set -u` / `set -o nounset` in bash), pass `nounset=True`.\n\n```python\n# All the variables must be defined.\nexpandvars("$VAR1:${VAR2}:$VAR3", nounset=True)\n\n# Raises UnboundVariable error.\n```\n\n> NOTE: Another way is to use the `${VAR?}` or `${VAR:?}` syntax. See the examples in tests.\n\n### EXPANDVARS_RECOVER_NULL="foo"\n\nIf you want to temporarily disable strict parsing both for `nounset=True` and the `${VAR:?}` syntax, set environment variable `EXPANDVARS_RECOVER_NULL=somevalue`.\nThis helps with certain use cases where you need to temporarily disable strict parsing of critical env vars, e.g. in testing environment, without modifying the code.\n\ne.g.\n\n```bash\nEXPANDVARS_RECOVER_NULL=foo myapp --config production.ini && echo "All fine."\n```\n\n> WARNING: Try to avoid `export EXPANDVARS_RECOVER_NULL` because that will disable strict parsing permanently until you log out.\n\n\nContributing\n------------\nTo contribute, setup environment following way:\n\nFirst you need to [install poetry](https://python-poetry.org/docs/#installation).\n\nThen\n\n```bash\n# Clone repo\ngit clone https://github.com/sayanarijit/expandvars && cd expandvars\n\n# Install poetry dependencies\npoetry install\n```\n\n- Follow [general git guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project).\n- Keep it simple. Run `poetry run black` to auto format the code.\n- Test your changes locally by running `poetry run pytest` (pass `--cov --cov-report html` for browsable coverage report).\n- If you are familiar with [tox](https://tox.readthedocs.io), you may want to use it for testing in different python versions.\n',
    'author': 'Arijit Basu',
    'author_email': 'sayanarijit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sayanarijit/expandvars',
    'py_modules': modules,
}


setup(**setup_kwargs)
