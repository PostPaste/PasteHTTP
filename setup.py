from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pastehttp/',
      version=version,
      description="The Paste HTTP WSGI Server",
      long_description=open('README.rst').read(),
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: Internet :: WWW/HTTP :: WSGI",
                   "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
    "Framework :: Paste"], 
      keywords='',
      author='Ian Bicking',
      author_email='whit at surveymonkey.com',
      url='http://pastehttp.github.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [paste.server_runner]
      http = paste.httpserver:server_runner

      [karnac.server_runner]
      http = paste.httpserver:server_runner      
      """,
      )
