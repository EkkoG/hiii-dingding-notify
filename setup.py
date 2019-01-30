#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='hiii-dingding-notify',
    version='0.0.1',
    author='cielpy',
    author_email='beijiu572@gmail.com',
    url='https://github.com/cielpy/hiii-dingding-notify',
    description='hiii 发钉钉通知',
    packages=find_packages(),
    install_requires=['requests'],
)