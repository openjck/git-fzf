from git_fzf.lib.utils.git import get_repo_root
from git_fzf.lib.utils.shell import run

from .InteractiveCommand import InteractiveCommand


class InteractiveAddCommand(InteractiveCommand):
    def __init__(self):
        super().__init__(
            no_candidates_message="you do not have any files to add",
            enable_multi_select=True,
        )

    def get_candidates(self):
        return run(
            "git ls-files --modified --others --exclude-standard {}".format(
                get_repo_root(),
            ),
            capture_output=True,
        ).splitlines()

    def affect_selected(self, selected):
        run(f"git add {' '.join(selected)}")
