import os
import re
import git


def get_latest_git_command():
    with open(os.environ.get('HISTFILE')) as history_file:
        for history_line in history_file.readlines()[::-1]:
            # TODO add aliases expansion
            if "git" in history_line:
                # in cause of multiple commands (with ; or &), will look for the last git command
                return re.findall("git[^;&]+(?=[;&])|git.+$", history_line)[-1]


def main():
    print('hello world!')
    repo = git.Repo(search_parent_directories=True)


if __name__ == '__main__':
    main()
