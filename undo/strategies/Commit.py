from undo.strategies.base import Strategy
import git


class Commit(Strategy):
    @classmethod
    def identify(cls, command: str) -> bool:
        return "commit" in command

    @classmethod
    def undo(cls, command: str, repo: git.Repo):
        repo.git.reset("HEAD~1", soft=True)
