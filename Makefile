.PHONY: clean_project dev py-fmt

dev:
	uv pip install -e .
	# ensure pre-commit is installed in the venv
	uv pip install --upgrade pre-commit
	pre-commit install

py-fmt:
	# Format Python files with ruff and then run a check
	python -m ruff format .
	python -m ruff check .

clean_project:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf
