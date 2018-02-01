#!/usr/bin/env python
from distutils.core import setup

setup(
    name='mplisp',
    version='0.2',
    packages=[
        'mplisp',
        'mplisp.functions',
        'mplisp.functions.arithmetic',
        'mplisp.functions.list',
        'mplisp.functions.special_forms',
        'mplisp.structures',
    ],
    scripts=[
        "scripts/mplisp"
    ],
    install_requires=[
    ]
)
