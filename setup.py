#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os
import sys
from setuptools import find_packages, setup

NAME = 'domainhelper'
DESCRIPTION = ' verify the domain and operate it'
URL = 'https://github.com/tiagn/domainhelper'
EMAIL = '347618578@qq.com'
AUTHOR = 'tiagn'
REQUIRES_PYTHON = '>=2.6'
VERSION = '1.0.0'

if '2' == sys.version[0]:
    # with open('requirements.txt', 'r') as f:
    #     REQUIRED = [pack.strip() for pack in f.readlines()]
    REQUIRED = []
else:
    REQUIRED = []

TESTS_REQUIRED = []

EXTRAS = {
}

# The rest you shouldn't have to touch too much :)
here = os.path.abspath(os.path.dirname(__file__))
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    tests_require=TESTS_REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
