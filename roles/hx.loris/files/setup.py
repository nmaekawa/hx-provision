#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
from setuptools import setup
from setuptools import find_packages
import loris
import os
import shutil
import stat

try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


VERSION = loris.__version__


def local_file(name):
    return os.path.relpath(os.path.dirname(__file__), name))


install_requires = parse_requirements(
    local_file('requirements.txt'), session=PipSession()
)

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
    install_requires=[str(ir.req) for ir in install_requires],
)


