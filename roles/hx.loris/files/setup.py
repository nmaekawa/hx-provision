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

DEPENDENCIES = [
    # (package, version, module)
    ('werkzeug', '>=0.8.3', 'werkzeug'),
    ('pillow', '>=2.4.0', 'PIL'),
    ('configobj', '>=4.7.2,<=5.0.0', 'configobj'),
    ('requests', '>=2.12.0', 'requests'),
]

install_requires = []
for d in DEPENDENCIES:
    try:
        __import__(d[2], fromlist=[''])
    except ImportError:
        install_requires.append(''.join(d[0:2]))

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
    install_requires=install_requires
)
