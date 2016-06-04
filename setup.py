#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages


EXCLUDE_FROM_PACKAGES = [
    'tests*',
    'raml2nthing.bin',
]


def install_requires():
    install_requires = [
        'ramlfications',
        'Jinja2',
    ]
    if sys.version_info < '2.7':
        install_requires.append('argparse')
    return install_requires


setup(
    name='raml2nthing',
    version='0.1.0',
    description='A tool for converting RAML to anything',
    long_description='',
    url='',
    license='Apache 2.0',
    author='Eugene Pokidov',
    author_email='pokidovea@gmail.com',
    keywords=['raml', 'converter'],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    scripts=['raml2nthing/bin/raml2nthing'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=install_requires()
)
