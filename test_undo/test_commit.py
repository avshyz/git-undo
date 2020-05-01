import os

import git

from test_undo.utils import add_empty_file
from undo.strategies import Commit


def test_undo_strategy_undoes_commit(repo: git.Repo):
    empty_file = add_empty_file(repo, 'commit_strategy_undo')
    head_before_commit = repo.head
    repo.index.commit('commit to revert')
    
    Commit.undo('git commit', repo)

    assert repo.head == head_before_commit
    assert empty_file.name in {name for name, stage in repo.index.entries}
    assert os.path.isfile(empty_file)
