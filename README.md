# git-fzf

git-fzf provides interactive versions of built-in Git commands using
[fzf](https://github.com/junegunn/fzf).

## Installation

* Install [fzf](https://github.com/junegunn/fzf)
* Download the scripts in the *src* directory and put them somewhere in your
  `$PATH`

## Usage

<dl>
  <dt>
    git iadd
  </dt>
  <dd>
    Interactively choose which files to add
  </dd>

  <dt>
    git idiff
  </dt>
  <dd>
    Interactively choose which files to diff. Provide the `--cached` flag to
    choose from cached files.
  </dd>

  <dt>
    git idifftool
  </dt>
  <dd>
    Interactively choose which files to diff with the difftool. Provide the
    `--cached` flag to choose from cached files.
  </dd>

  <dt>
    git ireset
  </dt>
  <dd>
    Interactively choose which files to reset
  </dd>

  <dt>
    git iswitch
  </dt>
  <dd>
    Interactively choose a branch to switch to. Provide the `--remotes` flag to
    choose from remote branches.
  </dd>
</dl>
