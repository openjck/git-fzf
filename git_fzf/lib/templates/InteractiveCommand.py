from abc import ABC, abstractmethod

from git_fzf.lib.utils import fzf
from git_fzf.lib.utils.runtime import handle_fatal_error, handle_startup


class InteractiveCommand(ABC):
    # This pattern requires that the named parameters be passed as named
    # arguments. They cannot be passed by position.
    #
    # https://stackoverflow.com/a/15302042
    def __init__(self, *, no_candidates_message, enable_multi_select):
        self.no_candidates_message = no_candidates_message
        self.enable_multi_select = enable_multi_select

    @abstractmethod
    def get_candidates(self):
        raise NotImplementedError

    @abstractmethod
    def affect_selected(self):
        raise NotImplementedError

    def execute(self):
        handle_startup()
        candidates = self.get_candidates()
        if not len(candidates):
            handle_fatal_error(self.no_candidates_message)
        else:
            selector = fzf.multi if self.enable_multi_select else fzf.single
            selected = selector(candidates)
            self.affect_selected(selected)
