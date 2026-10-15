# CLAUDE.md

Guidance for Claude Code in this repository. Replace the placeholders when you
start a project from this template, and keep the file short.

## What this project is

<!-- One paragraph: the problem it solves and who uses it. -->

## Layout

- `src/project_name/` — package code (src layout)
- `tests/` — pytest tests, mirroring the package structure
- `pyproject.toml` — dependencies, tool config (ruff, pytest, mypy, coverage)

## Development

```bash
make install   # venv deps + pre-commit hooks
make check     # ruff check, ruff format --check, mypy, pytest + coverage (= CI)
make format    # apply ruff fixes and formatting
```

`make check` runs exactly what CI runs. If it fails before you have changed
anything, say so instead of working around it.

## Conventions

- Python >= 3.10, ruff (line length 88, isort rules included), NumPy-style docstrings.
- Dependencies live in `pyproject.toml` only; there is no `requirements.txt`.
- Configuration comes from environment variables; document each one in the README
  and add it to `.env.example` if a typical install needs it.
- Add or update a test with every behaviour change.
