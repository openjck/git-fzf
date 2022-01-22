.PHONY: format test lint

python = src/commands/* src/lib/**/*

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
