"""
GSPA
Calculate psuedo normal modes and approximate transition energies from DMC wave functions
"""

import sys
from setuptools import setup, find_packages

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    # Self-descriptive entries which should always be present
    name='GSPA_DMC',
    author='Ryan DiRisio',
    author_email='rjdiri@uw.edu',
    license='MIT',

    # Which Python importable modules should be included when your package is installed
    # Handled automatically by setuptools. Use 'exclude' to prevent some specific
    # subpackage(s) from being added, if needed
    packages=find_packages(),

    # Optional include package data to ship with your package
    # Customize MANIFEST.in if the general case does not suit your needs
    # Comment out this line to prevent the files from being packaged with your software
    include_package_data=True,

    # Allows `setup.py test` to work correctly with pytest
    setup_requires=[] + pytest_runner,

    # install_requires=[],              # Required packages, pulls from pip if needed; do not use for Conda deployment

    # Additional entries you may want simply uncomment the lines you want and fill in the data
    platforms=['Linux',
               'Mac OS-X',
               'Unix'],            # Valid platforms your code works on, adjust to your flavor
    python_requires=">=3.5",          # Python version restrictions

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,

)