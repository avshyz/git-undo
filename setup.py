from setuptools import setup, find_packages

setup(
    name='git-undo',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'git-undo=undo.main:main'
        ]
    }
)
