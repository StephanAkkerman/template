# One definition of "done": `make check` runs the same gates CI runs.
# Everything goes through uv, which creates .venv and keeps it in sync with uv.lock.
.PHONY: help install check lint format test typecheck lock upgrade clean

help:
	@echo "make install    sync .venv from uv.lock and install git hooks"
	@echo "make check      lint, format check, type check and tests (what CI runs)"
	@echo "make lint       ruff check + ruff format --check"
	@echo "make format     apply ruff fixes and formatting"
	@echo "make test       pytest with coverage"
	@echo "make typecheck  ty"
	@echo "make lock       refresh uv.lock after editing pyproject.toml"
	@echo "make upgrade    upgrade every dependency to the latest allowed version"
	@echo "make clean      remove caches and build output"

install:
	uv sync
	uv run pre-commit install

check: lint typecheck test

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

typecheck:
	uv run ty check

test:
	uv run pytest --cov --cov-report=term-missing

lock:
	uv lock

upgrade:
	uv lock --upgrade
	uv sync

clean:
	rm -rf build dist .pytest_cache .ruff_cache .coverage htmlcov coverage.xml *.egg-info src/*.egg-info
