#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.util import convert_path
import codecs

# Load version information
main_ns = {}
ver_path = convert_path('src/xmlrunner/version.py')
with codecs.open(ver_path, 'rb', 'utf8') as ver_file:
    exec(ver_file.read(), main_ns)

install_requires = ['six>=1.4.0']

# this is for sdist to work.
import sys
if sys.version_info < (2, 7):
    install_requires += ['unittest2']

setup(
    name = 'unittest-xml-reporting',
    version = main_ns['__version__'],
    author = 'Daniel Fernandes Martins',
    author_email = 'daniel.tritone@gmail.com',
    description = 'unittest-based test runner with Ant/JUnit like XML reporting.',
    license = 'BSD',
    platforms = ['Any'],
    keywords = [
        'pyunit', 'unittest', 'junit xml', 'report', 'testrunner', 'xmlrunner'
    ],
    url = 'http://github.com/xmlrunner/unittest-xml-reporting/tree/master/',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    packages = find_packages('src'),
    package_dir = {'':'src'},
    zip_safe = False,
    include_package_data = True,
    install_requires = install_requires,
    extras_require={
        # this is for wheels to work
        ':python_version=="2.6"': ['unittest2'],
    },
    test_suite = 'xmlrunner.tests.testsuite'
)
