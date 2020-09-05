#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pyanchor']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4', 'requests', 'typer', 'lxml']

entry_points = \
{'console_scripts': ['pyanchor = pyanchor.cli:app']}

setup(name='pyanchor',
      version='0.2',
      description='Check you site for broken links!',
      author='Ricky White',
      author_email='ricky@whitelionmedia.com',
      url='https://github.com/EndlessTrax/pyanchor/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
