#!/usr/bin/env python
# -*- coding: utf-8 -*-
# just enough setup.py to install via pip
from setuptools import setup
from setuptools import find_packages
import loris
import os
import shutil
import stat

VERSION = loris.__version__

requirements = [
    'configobj',
    'pillow',
    'requests',
    'werkzeug',
]

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
    install_requires=requirements,
)
