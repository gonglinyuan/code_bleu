#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name='code_bleu',
    version="1.0.0",
    description='Calculating CodeBLEU, a metric for code similarity',
    maintainer='Linyuan Gong',
    maintainer_email='gonglinyuan@hotmail.com',
    url='https://github.com/gonglinyuan/code_bleu',
    packages=find_packages(),
    package_data={'code_bleu': ['*.txt']},
    install_requires=['setuptools>=60.0.0', 'tree-sitter>=0.20.1', 'GitPython>=3.1'],
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Software Development :: Compilers',
        'Topic :: Text Processing :: Linguistic',
    ]
)
