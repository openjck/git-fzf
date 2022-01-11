from git_fzf.lib.utils.shell import run

from .InteractiveDiffLikeCommand import InteractiveDiffLikeCommand


class InteractiveDifftoolCommand(InteractiveDiffLikeCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flags.get("affect_selected").append("--no-prompt")

    def get_candidates(self, *args, **kwargs):
        return super().get_candidates(*args, **kwargs)

    def affect_selected(self, selected):
        run(
            "git difftool {} {}".format(
                " ".join(self.flags.get("affect_selected")),
                " ".join(selected),
            )
        )
