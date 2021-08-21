.PHONY: format test lint

format:
	npx prettier --write --prose-wrap always .

test: lint

lint:
	npx prettier --check --prose-wrap always .
