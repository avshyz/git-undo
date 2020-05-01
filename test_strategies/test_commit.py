
def test_foo(repo):
    assert repo.branches['master'].log() == 1