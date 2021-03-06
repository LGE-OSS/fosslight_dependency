#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2020 LG Electronics

from codecs import open
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name             = 'fosslight_dependency',
        version          = '3.0.6',
        packages         = find_packages(),
        description      = 'FOSSLight Dependency',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        license          = 'Apache-2.0',
        author           = 'LG Electronics',
        url              = 'https://github.com/fosslight/fosslight_dependency',
        classifiers      = ['Programming Language :: Python :: 3.6',
                            'License :: OSI Approved :: Apache Software License'],
        install_requires = required,
        package_data = {'unified_script':['third_party/nomos/nomossa','third_party/askalono/askalono.exe','third_party/askalono/askalono_macos']},
        include_package_data = True,
        entry_points = {
            "console_scripts": [
                "fosslight_dependency=unified_script.dependency_unified:main"
                ]
            }
    )
