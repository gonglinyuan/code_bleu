import os
import tempfile

import git
from tree_sitter import Language

LIBRARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'parser', 'my-languages.so')


def build():
    repositories = [
        'https://github.com/tree-sitter/tree-sitter-go',
        'https://github.com/tree-sitter/tree-sitter-javascript',
        'https://github.com/tree-sitter/tree-sitter-python',
        'https://github.com/tree-sitter/tree-sitter-ruby',
        'https://github.com/tree-sitter/tree-sitter-php',
        'https://github.com/tree-sitter/tree-sitter-java',
        'https://github.com/tree-sitter/tree-sitter-c-sharp'
    ]

    with tempfile.TemporaryDirectory() as temp_dir:
        for repo_url in repositories:
            git.Repo.clone_from(repo_url, os.path.join(temp_dir, os.path.basename(repo_url)), depth=1)

        Language.build_library(
            LIBRARY_PATH,
            [os.path.join(temp_dir, os.path.basename(repo_url)) for repo_url in repositories]
        )


def maybe_build():
    if not os.path.exists(LIBRARY_PATH):
        print("Tree-Sitter binary not built yet, building...")
        build()
