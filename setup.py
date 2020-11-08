#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py

import os
import re
import sys

from codecs import open

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from gytrash.__about__ import version

repo_path = os.path.abspath(os.path.dirname(__file__))

packages = find_packages(exclude=("examples",))

about = {}
with open(os.path.join(repo_path, "gytrash", "__about__.py"), "r", "utf-8") as f:
    exec(f.read(), about)
with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=version,
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=packages,
    package_dir={"gytrash": "gytrash"},
    package_data={"": ["*.cwl", "*.yaml"]},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["coloredlogs==14.0", "slack-sdk==3.0.0b1"],
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    tests_require=[],
    project_urls={"Source": "https://github.com/trejas/gytrash"},
)
