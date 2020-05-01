from pathlib import Path

import git
import pytest


@pytest.fixture
def repo_dir(tmp_path) -> Path:
    d = tmp_path / 'repo'
    d.mkdir()
    return d


@pytest.fixture
def empty_repo(repo_dir: Path) -> git.Repo:
    return git.Repo.init(repo_dir)


@pytest.fixture
def repo(empty_repo: git.Repo, repo_dir: Path) -> git.Repo:
    (repo_dir / 'empty_file').touch()
    empty_repo.index.add(['empty_file'])
    empty_repo.index.commit('initial commit')
    return empty_repo
