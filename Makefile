.PHONY: clean format test lint

python = git_fzf/commands/* git_fzf/lib/*

clean:
	poetry run pyclean .

format:
	npx prettier --write --prose-wrap always .
	poetry run isort $(python)
	poetry run black $(python)

test: lint

lint:
	npx prettier --check --prose-wrap always .
	poetry run isort --check $(python)
	poetry run black --check $(python)
	poetry run flake8 $(python)
