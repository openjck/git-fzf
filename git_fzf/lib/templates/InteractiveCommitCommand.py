from git_fzf.lib.utils.git import get_repo_root
from git_fzf.lib.utils.shell import run

from .InteractiveCommand import InteractiveCommand


class InteractiveCommitCommand(InteractiveCommand):
    def __init__(self):
        super().__init__(
            no_candidates_message=(
                "you do not have any files which can be committed"
            ),
            enable_multi_select=True,
        )

    def get_candidates(self):
        staged_files = run(
            "git diff --name-only --relative --staged",
            capture_output=True,
        ).splitlines()

        other_files = run(
            "git ls-files --modified --others --exclude-standard {}".format(
                get_repo_root(),
            ),
            capture_output=True,
        ).splitlines()

        # Return a sorted list. sorted() both sorts the set and converts it to
        # a list.
        return sorted(set(staged_files + other_files))

    def affect_selected(self, selected):
        run(f"git commit {' '.join(selected)}")
