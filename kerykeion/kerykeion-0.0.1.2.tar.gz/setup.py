"""
    This is part of Kerykeion (C) 2020 Giacomo Battaglia
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kerykeion",
    version="0.0.1.2",
    author="Giacomo Battaglia",
    author_email="battaglia.giacomo@yahoo.it",
    description="Astrology library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/g-battaglia/kerykeion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['pyswisseph==2.00.00-2', 'pytz'],
)
