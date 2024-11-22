#!/usr/bin/env python

from os.path import exists
from setuptools import setup

packages = ['streamz', 'streamz.dataframe']

tests = [p + '.tests' for p in packages]


setup(name='streamz',
      version='0.6.4',
      description='Streams',
      url='http://github.com/python-streamz/streamz/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='streams',
      packages=packages + tests,
      python_requires='>=3.9',
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      zip_safe=False)
