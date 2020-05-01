import os
import re
import enum

from undo.strategies import STRATEGIES


def get_latest_git_command():
    with open(os.environ.get("HISTFILE")) as history_file:
        for history_line in history_file.readlines()[::-1]:
            # TODO add aliases expansion
            # TODO ignore unrevertable commands (log, status, etc.)
            if re.search(r"\bgit ", history_line):
                # in cause of multiple commands (with ; or &), will look for the last git command
                return re.findall("git[^;&]+(?=[;&])|git.+$", history_line)[-1]


def main():
    git_cmd = get_latest_git_command()
    print(git_cmd)
    for strategy in STRATEGIES:
        if strategy.identify(git_cmd):
            print(strategy)
            strategy.undo(git_cmd, repo=None)
    else:
        print("NOT FOUND")
