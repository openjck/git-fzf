import subprocess

from .errors import handle_error


# This pattern requires that the named parameters be passed as named arguments.
# They cannot be passed by position.
#
# https://stackoverflow.com/a/15302042
def run(cmd, *, capture_output=False):
    sp = subprocess.run(cmd.split(), capture_output=capture_output, text=True)
    if sp.returncode != 0:
        error_message = sp.stderr.strip() if sp.stderr else None
        handle_error(error_message, sp.returncode)
    elif capture_output:
        return sp.stdout.strip()
