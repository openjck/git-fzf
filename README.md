# git-fzf

git-fzf provides interactive versions of built-in Git commands using
[fzf](https://github.com/junegunn/fzf).

https://user-images.githubusercontent.com/933396/130337046-1f8b9143-55e1-4dde-a1a1-ea69feb1d2b4.mp4

## Installation

1. Install [fzf](https://github.com/junegunn/fzf)
2. Run `mkdir --parents ~/.local/share/applications`
3. Run
   `git clone https://github.com/openjck/git-fzf.git ~/.local/share/applications/git-fzf`
4. Run
   `echo 'export PATH="$HOME/.local/share/applications/git-fzf/commands:$PATH"' >> ~/.profile`
5. Log out and log back in

## Upgrading

1. Run `cd ~/.local/share/applications/git-fzf`
2. Run `git pull`

## Usage

<dl>
  <dt>
    git iadd
  </dt>
  <dd>
    Interactively choose one or more files to add
  </dd>

  <dt>
    git icommit
  </dt>
  <dd>
    Interactively choose one or more staged files to commit
  </dd>

  <dt>
    git idiff
  </dt>
  <dd>
    Interactively choose one or more files to diff. Provide the
    <code>--staged</code> flag to choose from staged files.
  </dd>

  <dt>
    git idifftool
  </dt>
  <dd>
    Interactively choose one or more filees to diff with the difftool. Provide
    the <code>--staged</code> flag to choose from staged files.
  </dd>

  <dt>
    git ireset
  </dt>
  <dd>
    Interactively choose one or more files to reset
  </dd>

  <dt>
    git irestore
  </dt>
  <dd>
    Interactively choose one or more files to restore
  </dd>

  <dt>
    git iswitch
  </dt>
  <dd>
    Interactively choose a branch to switch to. Provide the
    <code>--remotes</code> flag to choose from remote branches.
  </dd>
</dl>
