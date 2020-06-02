#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

import weather_station

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author=weather_station.__author__,
    author_email=weather_station.__email__,
    python_requires='>=3.5',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description=weather_station.__description__,
    install_requires=requirements,
    license=weather_station.__licence__,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='weather_station',
    name=weather_station.__title__,
    packages=find_packages(include=['weather_station', 'weather_station.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/allenerocha/weather_station',
    version=weather_station.__version__,
    zip_safe=False,
)
