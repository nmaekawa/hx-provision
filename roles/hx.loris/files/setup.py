#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
from setuptools import setup
from setuptools import find_packages
import loris
import os
import shutil
import stat

VERSION = loris.__version__


with open('requirements.txt') as f:
    install_requires = list(f)

def _read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Loris',
    author='Jon Stroop',
    author_email='jpstroop@gmail.com',
    url='https://github.com/loris-imageserver/loris',
    description = ('IIIF Image API 2.0 Level 2 compliant Image Server'),
    long_description=_read('README.md'),
    license='Simplified BSD',
    version=VERSION,
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=install_requires,
)


