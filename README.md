# git-fzf

git-fzf provides interactive versions of built-in Git commands using
[fzf](https://github.com/junegunn/fzf).

## Installation

1. Install [fzf](https://github.com/junegunn/fzf)
2. Download the scripts in the *commands* directory and put them somewhere in
   your `$PATH`

## Usage

<dl>
  <dt>
    git iadd
  </dt>
  <dd>
    Interactively choose one or more files to add
  </dd>

  <dt>
    git idiff
  </dt>
  <dd>
    Interactively to choose one or more files to diff. Provide the
    <code>--staged</code> flag to choose from staged files.
  </dd>

  <dt>
    git idifftool
  </dt>
  <dd>
    Interactively to choose one or more filees to diff with the difftool.
    Provide the <code>--staged</code> flag to choose from staged files.
  </dd>

  <dt>
    git ireset
  </dt>
  <dd>
    Interactively to choose one or more files to reset
  </dd>

  <dt>
    git iswitch
  </dt>
  <dd>
    Interactively choose a branch to switch to. Provide the
    <code>--remotes</code> flag to choose from remote branches.
  </dd>
</dl>
