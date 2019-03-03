#!/usr/bin/env python3
import io
import re
from setuptools import setup, find_packages
import sys

if sys.version_info[:2] < (3, 6):
    raise SystemExit("BovespaWolf requires Python 3.4+")

with io.open('./sample/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='BovespaWolf',
    version=version,
    description='Win money honey',
    long_description=long_description,
    author=['Renato Avellar Nobre', 'Khalil Carsten'],
    author_email='rekanobre@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development'
    ],
    test_suite='tests'
)
