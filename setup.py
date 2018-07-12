# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sqintools',
    version='0.0.1',
    description='shuang‘s common tools',
    long_description=readme,
    author='Shuang Qin ',
    author_email='qinshuang_11@163.com',
    url='https://www.baidu.com',
    license=license,
    packages=find_packages(),
)

