#!/usr/bin/env python

import glob

from pip.download import PipSession
from pip.req import parse_requirements

from setuptools import setup, find_packages


setup(
    name='eventboard_challenge',
    description='Eventboard Coding challenge.',
    url='https://github.com/rmalleman/eventboard-challenge',
    author='Matt Alleman',
    author_email='rmalleman@gmail.com',
    maintainer='Matt Alleman',
    maintainer_email='rmalleman@gmail.com',
    version='0.0.1',
    classifiers=('Programming Language :: Python :: 3.5',),
    py_modules=['word_count', 'meeting_times'],
    scripts=glob.glob('scripts/*'),
    install_requires=[str(a).split(' ')[0] for a in parse_requirements('requirements.txt', session=PipSession())]
)
