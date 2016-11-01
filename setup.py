#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import ast


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def get_version():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    init_file = os.path.join(this_dir, "solar_theme", "__init__.py")
    with open(init_file) as f:
        for line in f:
            if line.startswith("__version__"):
                version = ast.literal_eval(line.split("=")[1].strip())
                if version:
                    return version
    raise ValueError(
        "Cannot determine the version of the package from the file: "
        "".format(init_file)
    )


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='solar-theme',
    version=get_version(),
    description='Theme for Python Sphinx',
    long_description=readme + '\n\n' + history,
    author='Vimalkumar Velayudhan',
    author_email='vimalkumarvelayudhan@gmail.com',
    url='https://github.com/vimalkvn/solar-theme',
    packages=[
        'solar_theme',
    ],
    package_dir={'solar_theme': 'solar_theme'},
    package_data={'solar_theme': [
        'theme.conf', 'static/subtle_dots.png', '*.html', 'static/*.css']},
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords=['solar', 'theme', 'sphinx'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Framework :: Sphinx :: Theme',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.3'
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
    ],
    test_suite='tests',
)
