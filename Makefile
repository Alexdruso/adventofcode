.PHONY: clean_project dev dev-recreate py-fmt set-session fetch-input

dev:
	# create a virtualenv in .venv if it does not exist
	test -d .venv || python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -e .
	# ensure pre-commit is installed in the venv
	.venv/bin/pip install --upgrade pre-commit
	.venv/bin/pre-commit install || true

dev-recreate:
	# remove and recreate the venv from scratch
	rm -rf .venv
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -e .
	.venv/bin/pip install --upgrade pre-commit
	.venv/bin/pre-commit install || true


set-session:
	# Write .setup.json containing the user agent and session cookie (TOKEN)
	@if [ -z "$(TOKEN)" ]; then \
		echo "Usage: make set-session TOKEN=<your_aoc_session_token> [USER_AGENT='my-agent']"; exit 1; \
	fi
	@USER_AGENT="$${USER_AGENT:-adventofcode-fetcher}"; \
	printf '%s' "{\"user_agent\": \"$${USER_AGENT}\", \"session_cookie\": \"$(TOKEN)\"}" > .setup.json; \
	chmod 600 .setup.json; \
	echo "Wrote .setup.json (permissions 600)"

py-fmt:
	# Format Python files with ruff and then run a check
	python -m ruff format .
	python -m ruff check .

clean_project:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf
