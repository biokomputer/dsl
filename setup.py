from setuptools import setup, find_packages

setup(
    name='biocomp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyparsing==2.4.7',
        'matplotlib==3.4.3',
        'numpy==1.21.2'
    ],
    entry_points={
        'console_scripts': [
            'biocomp=biocomp:main',
        ],
    },
)