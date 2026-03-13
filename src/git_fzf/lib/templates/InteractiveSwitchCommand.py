import argparse

from git_fzf.lib.utils.shell import run

from .InteractiveCommand import InteractiveCommand


class InteractiveSwitchCommand(InteractiveCommand):
    def __init__(self):
        super().__init__(
            no_candidates_message=(
                "your repository does not have any branches with commits yet"
            ),
            enable_multi_select=False,
        )

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-r", "--remotes", action="store_true")
        self.parser.set_defaults(remotes=False)
        self.args = self.parser.parse_args()

        self.flags = {
            "get_candidates": [
                "--format=%(refname:short)",
            ],
        }

        if self.args.remotes:
            self.flags.get("get_candidates").append("--remotes")

    def get_candidates(self):
        return run(
            f"git branch {' '.join(self.flags.get('get_candidates'))}",
            capture_output=True,
        ).splitlines()

    def affect_selected(self, selected):
        if self.args.remotes:
            # FIXME: When --track is supplied, the name of the local branch is
            # derived from the name of the remote branch. However, --track also
            # sets the local branch to track the remote branch, which the user
            # may not want.
            #
            # We also cannot use --track if the user passed the --all flag,
            # since "git switch" errors out if the --track flag is passed and
            # the name of a local branch is supplied, and a user may select a
            # local branch if they passed the --all flag to "git iswitch".
            #
            # See issue #14.
            run(f"git switch --track {selected}")
        else:
            run(f"git switch {selected}")
