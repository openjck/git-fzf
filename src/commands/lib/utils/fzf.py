import sys

from plumbum.commands.processes import ProcessExecutionError
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()


def single(selectable):
    return _prompt_gracefully(selectable)[0]


def multi(selectable):
    return _prompt_gracefully(selectable, "--multi")


def _prompt_gracefully(*args):
    try:
        return fzf.prompt(*args)
    except ProcessExecutionError:
        sys.exit(0)
