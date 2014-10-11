# -*- coding: utf-8 -*-

import sys
from setuptools import setup

install_requires = [
    'doit',
    'mergedict',
    'configclass >=0.1, <0.2',
    'doit-cmd >=0.1, <0.2',
    ],

if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    install_requires.append('pathlib')


setup (
    name = 'doit-web',
    version = '0.1.dev0',
    author = 'Eduardo Naufel Schettino',
    author_email = 'schettino72@gmail.com',
    description = 'doit tasks for web stuff',
    url = 'https://github.com/schettino72/doit-web/',
    keywords = ['doit', 'javascript'],
    platforms = ['any'],
    license = 'MIT',
    packages = ['doitweb'],
    install_requires = install_requires,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ]
)
