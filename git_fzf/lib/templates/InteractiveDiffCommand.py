from git_fzf.lib.utils.shell import run

from .InteractiveDiffLikeCommand import InteractiveDiffLikeCommand


class InteractiveDiffCommand(InteractiveDiffLikeCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_candidates(self, *args, **kwargs):
        return super().get_candidates(*args, **kwargs)

    def affect_selected(self, selected):
        run(
            "git diff {} {}".format(
                " ".join(self.flags.get("affect_selected")),
                " ".join(selected),
            )
        )
