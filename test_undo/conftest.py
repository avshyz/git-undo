from pathlib import Path

import git
import pytest

from test_undo.utils import add_empty_file


@pytest.fixture
def repo_dir(tmp_path) -> Path:
    d = tmp_path / 'repo'
    d.mkdir()
    return d


@pytest.fixture
def empty_repo(repo_dir: Path) -> git.Repo:
    repo = git.Repo.init(repo_dir)
    repo.repo_dir = repo_dir
    return repo


@pytest.fixture
def repo(empty_repo: git.Repo) -> git.Repo:
    add_empty_file(empty_repo, 'empty_file')
    empty_repo.index.commit('initial commit')
    return empty_repo
