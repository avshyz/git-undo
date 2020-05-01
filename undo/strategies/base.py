import abc
import git


class Strategy(abc.ABC):

    @classmethod
    def identify(cls, command: str) -> bool:
        raise NotImplementedError()

    @classmethod
    def undo(cls, command: str, repo: git.Repo):
        raise NotImplementedError()
