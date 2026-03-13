clean:
  uv run pyclean .

format:
  npx prettier --write --prose-wrap always .
  uv run isort .
  uv run black .

lint:
  npx prettier --check --prose-wrap always .
  uv run isort --check .
  uv run black --check .
  uv run flake8 .
