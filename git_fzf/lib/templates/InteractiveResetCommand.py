from git_fzf.lib.utils.shell import run

from .InteractiveCommand import InteractiveCommand


class InteractiveResetCommand(InteractiveCommand):
    def __init__(self):
        super().__init__(
            no_candidates_message="you do not have any files to reset",
            enable_multi_select=True,
        )

    def get_candidates(self):
        return run(
            "git diff --name-only --relative --staged",
            capture_output=True,
        ).splitlines()

    def affect_selected(self, selected):
        run(f"git reset {' '.join(selected)}")
