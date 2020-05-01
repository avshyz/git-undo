import git

from undo.strategies import Checkout


def test_undo_strategy_undoes_checkout(repo: git.Repo):
    head_before_commit = repo.head

    branch2 = repo.create_head("branch2")
    branch2.checkout()

    Checkout.undo('git checkout', repo)

    assert repo.head == head_before_commit
