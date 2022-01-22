from .errors import handle_fatal_error
from .shell import run


def handle_startup():
    # If "git rev-parse" fails, then we are not in a Git repository. When "git
    # rev-parse" fails, Git will print a generic error message about not being
    # in a Git repository. We want that generic error message, not an error
    # message specific to the command that provides input to fzf, because the
    # user does not care what command is providing input to fzf.
    #
    # Some Git commands (like "git add") fail if they are run inside the .git
    # directory itself. Users would be annoyed if that happened after they
    # selected their file(s), so the situation is handled here before anything
    # else is done. The error message that is printed is identical to the error
    # message that Git itself prints in this situation. For example, see what
    # Git prints when "git add" is run inside the .git directory itself.
    #
    # It's important to do the bare "git rev-parse" check first to determine if
    # we are in a Git repository at all. If the order were switched, "git
    # rev-parse --is-inside-git-dir" would fail with the generic error message
    # about not being in a Git repository, then "git rev-parse" would be run
    # and would fail again with the same error message.

    # If we are in a Git repo, "git rev-parse" will silently succeed. If we are
    # not, the run() function will print the error and exit immediately.
    run("git rev-parse")

    if run("git rev-parse --is-inside-git-dir", capture_output=True) == "true":
        handle_fatal_error("this operation must be run in a work tree")
