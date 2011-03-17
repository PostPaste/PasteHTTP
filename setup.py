from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pastehttp/',
      version=version,
      description="The Paste HTTP WSGI Server",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
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
      # -*- Entry points: -*-
      """,
      )
