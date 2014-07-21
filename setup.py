# -*- coding: utf-8 -*-

from setuptools import setup

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
    install_requires = ['doit', 'pathlib', 'mergedict'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ]
)
