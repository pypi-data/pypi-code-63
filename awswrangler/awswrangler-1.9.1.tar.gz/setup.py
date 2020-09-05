import os
from io import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
about = {}
path = os.path.join(here, "awswrangler", "__metadata__.py")
with open(file=path, mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Igor Tavares",
    url="https://github.com/awslabs/aws-data-wrangler",
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=about["__license__"],
    packages=["awswrangler", "awswrangler.s3", "awswrangler.quicksight", "awswrangler.athena", "awswrangler.catalog"],
    include_package_data=True,
    python_requires=">=3.6, <3.9",
    install_requires=open("requirements.txt").read().strip().split("\n"),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
