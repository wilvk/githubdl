"""

A package for downloading files/directories from Github/Github Enterprise

See:
https://github.com/wilvk/githbdl

"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

  name = 'githubdl',

  version = '0.1.2',

  description = 'A tool for downloading individual files/directories from Github or Github Enterprise. This circumvents the requirement to clone an entire repository.',

  author = 'Willem van Ketwich',
  author_email = 'willvk@gmail.com',

  license = 'MIT',

  python_requires='>=3.4',

  url = 'https://github.com/wilvk/githubdl',

  download_url = 'https://github.com/wilvk/githubdl/archive/0.1.tar.gz',

  long_description=long_description,

  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
  ],

  keywords = ['github', 'github enterprise', 'download', 'file', 'path', 'git', 'version control', 'deployment'],

  install_requires = [
      'requests'
  ],

  packages = find_packages(exclude=['contrib', 'docs', 'tests']),

  extras_require={
      'dev': [],
      'test': [ 'nose' ],
  },

  entry_points={
      'console_scripts': [
          'githubdl=githubdl:main',
      ],
  },

)
