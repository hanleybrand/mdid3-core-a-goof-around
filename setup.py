#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="mdid3",
    version="0.1.0",
    author="Hanleybrand",
    author_email="phanley@temple.edu",
    packages=[
        "mdid3",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["mdid3/manage.py"],
)
