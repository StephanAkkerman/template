# One definition of "done": `make check` runs the same gates CI runs.
.PHONY: help install check lint format test typecheck clean

help:
	@echo "make install    create/refresh the dev environment and git hooks"
	@echo "make check      lint, format check, type check and tests (what CI runs)"
	@echo "make lint       ruff check"
	@echo "make format     apply ruff fixes and formatting"
	@echo "make test       pytest with coverage"
	@echo "make typecheck  mypy"
	@echo "make clean      remove caches and build output"

install:
	python -m pip install --upgrade pip
	python -m pip install -e ".[dev]"
	pre-commit install

check: lint typecheck test

lint:
	ruff check .
	ruff format --check .

format:
	ruff check --fix .
	ruff format .

typecheck:
	mypy

test:
	python -m pytest --cov --cov-report=term-missing

clean:
	rm -rf build dist .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov *.egg-info src/*.egg-info
