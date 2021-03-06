from setuptools import setup, Command
import os
import sys

setup(name='atspy',
      version='0.1.9',
      description='Automated Time Series in Python',
      url='https://github.com/firmai/atspy',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['atspy','atspy.TS'],
      install_requires=[
          'pandas',
          'scipy',
          'numba',
          'datetime',
          'pmdarima',
          'matplotlib',
          'lightgbm',
          'sklearn',
          'gluonts==0.4.2',
          'nbeats-pytorch==1.3.0',
          'seasonal==0.3.1',
          'tbats==1.0.9',
          'tsfresh',
          'python-dateutil==2.8.0',
          'mxnet-cu100==1.4.1',
          'numpy==1.17.4',

      ],
      zip_safe=False)
