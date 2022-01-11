import sys


def handle_error(msg, returncode=1):
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(returncode)


# The provided error message should be based on the error message that is
# printed if "git log" is run in an empty repository
def handle_fatal_error(msg):
    handle_error(f"fatal: {msg}")
