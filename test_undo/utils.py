from pathlib import Path

import git


def add_empty_file(repo: git.Repo, file_name: str) -> Path:
    empty_file = repo.repo_dir / file_name
    empty_file.touch()
    repo.index.add([file_name])
    return empty_file
