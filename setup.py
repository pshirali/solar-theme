#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='solar',
    version='1.3.1',
    description='Theme for Python Sphinx',
    long_description=readme + '\n\n' + history,
    author='Vimalkumar Velayudhan',
    author_email='vimalkumarvelayudhan@gmail.com',
    url='https://github.com/vkvn/solar',
    packages=[
        'solar',
    ],
    package_dir={'solar': 'solar'},
    package_data={'solar': ['theme.conf', 'static/subtle_dots.png', '*.html',
                            'static/*.css']},
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='solar',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
)
