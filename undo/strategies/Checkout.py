from undo.strategies.base import Strategy
import git


class Checkout(Strategy):
    @classmethod
    def identify(cls, command: str) -> bool:
        return "checkout" in command

    @classmethod
    def undo(cls, command: str, repo: git.Repo):
        repo.git.checkout("-")
