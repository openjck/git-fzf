from .shell import run


def get_repo_root():
    return run("git rev-parse --show-toplevel", capture_output=True)
