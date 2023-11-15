#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

from setuptools import Command, find_packages, setup


class CustomBuildCommand(Command):
    """Custom command to run build.sh operations."""

    description = 'Run custom build steps'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # List of commands to run
        commands = [
            'git clone https://github.com/tree-sitter/tree-sitter-go',
            'git clone https://github.com/tree-sitter/tree-sitter-javascript',
            'git clone https://github.com/tree-sitter/tree-sitter-python',
            'git clone https://github.com/tree-sitter/tree-sitter-ruby',
            'git clone https://github.com/tree-sitter/tree-sitter-php',
            'git clone https://github.com/tree-sitter/tree-sitter-java',
            'git clone https://github.com/tree-sitter/tree-sitter-c-sharp'
        ]

        for cmd in commands:
            subprocess.check_call(cmd, shell=True)

        from tree_sitter import Language

        Language.build_library(
            # Store the library in the `build` directory
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'code_bleu', 'parser', 'my-languages.so'),

            # Include one or more languages
            [
                'tree-sitter-go',
                'tree-sitter-javascript',
                'tree-sitter-python',
                'tree-sitter-php',
                'tree-sitter-java',
                'tree-sitter-ruby',
                'tree-sitter-c-sharp',
            ]
        )


setup(
    name='code_bleu',
    version="1.0.0",
    description='Calculating CodeBLEU, a metric for code similarity',
    maintainer='Linyuan Gong',
    maintainer_email='gonglinyuan@hotmail.com',
    url='https://github.com/gonglinyuan/code_bleu',
    packages=find_packages(''),
    package_dir={'': ''},
    package_data={'code_bleu': ['*.txt']},
    install_requires=['setuptools>=60.0.0', 'tree-sitter>=0.20.1'],
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Software Development :: Compilers',
        'Topic :: Text Processing :: Linguistic',
    ],
    cmdclass={
        'build': CustomBuildCommand,
    }
)
