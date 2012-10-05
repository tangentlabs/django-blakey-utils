#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in django_blakey_utils.__init__.py
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

from django_blakey_utils import get_version

setup(name='django-blakey-utils',
    version=get_version().replace(' ', '-'),
    url='https://github.com/tangentlabs/django-blakey-utils',
    author="Tangent Labs",
    author_email="mariia.sakharova@tangentlabs.co.uk",
    description="Common utilities for Blakey project",
    long_description=open('README.rst').read(),
    keywords="Utilities, Blakey",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["*.tests"]),
    install_requires=[
        'Django==1.4.1',
        'django-tastypie==0.9.11'
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: Unix',
                 'Programming Language :: Python']
)
