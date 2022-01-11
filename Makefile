.PHONY: format test lint

python = src/commands/git-* src/commands/lib/*.py src/commands/lib/utils/*.py

format:
	npx prettier --write --prose-wrap always .
	isort $(python)
	black $(python)

test: lint

lint:
	npx prettier --check --prose-wrap always .
	isort --check $(python)
	black --check $(python)
	flake8 $(python)
