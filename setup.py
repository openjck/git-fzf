import setuptools

setuptools.setup(
    scripts=[
        "src/commands/add",
        "src/commands/commit",
        "src/commands/diff",
        "src/commands/difftool",
        "src/commands/reset",
        "src/commands/restore",
        "src/commands/switch",
    ],
    packages=[
        "git_fzf",
        "git_fzf.templates",
        "git_fzf.utils",
    ],
    package_dir={
        "git_fzf": "./src/lib/git_fzf",
        "git_fzf.templates": "./src/lib/git_fzf/templates",
        "git_fzf.utils": "./src/lib/git_fzf/utils",
    },
)
