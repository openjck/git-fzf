import argparse

from abc import abstractmethod

from git_fzf.lib.utils.shell import run

from .InteractiveCommand import InteractiveCommand


class InteractiveDiffLikeCommand(InteractiveCommand):
    def __init__(self):
        super().__init__(
            no_candidates_message="you do not have any files to diff",
            enable_multi_select=True,
        )

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--staged", "--cached", action="store_true")
        self.parser.set_defaults(staged=False)
        self.args = self.parser.parse_args()

        self.flags = {
            "get_candidates": [
                "--name-only",
                "--relative",
            ],
            "affect_selected": [],
        }

        if self.args.staged:
            self.flags.get("get_candidates").append("--staged")
            self.flags.get("affect_selected").append("--staged")

    def get_candidates(self):
        return run(
            f"git diff {' '.join(self.flags.get('get_candidates'))}",
            capture_output=True,
        ).splitlines()

    @abstractmethod
    def affect_selected(self):
        raise NotImplementedError
