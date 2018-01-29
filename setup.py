#!/usr/bin/env python

from distutils.core import setup

setup(
    name='mplisp',
    version='0.1',
    packages=[
        'mplisp',
        'mplisp.functions',
        'mplisp.functions.arithmetic',
        'mplisp.functions.special_forms',
        'mplisp.structures',
    ],
    scripts=[
        "scripts/mplisp"
    ],
    install_requires=[
    ]
 )
