# CLAUDE.md

Guidance for Claude Code in this repository. Replace the placeholders when you
start a project from this template, and keep the file short.

## What this project is

<!-- One paragraph: the problem it solves and who uses it. -->

## Layout

- `src/project_name/` — package code (src layout)
- `tests/` — pytest tests, mirroring the package structure
- `pyproject.toml` — dependencies, tool config (ruff, pytest, ty, coverage); `uv.lock` pins everything

## Development

```bash
make install   # uv sync (.venv from uv.lock) + pre-commit hooks
make check     # ruff check, ruff format --check, ty, pytest + coverage (= CI)
make format    # apply ruff fixes and formatting
```

`make check` runs exactly what CI runs. If it fails before you have changed
anything, say so instead of working around it.

## Conventions

- Python >= 3.10, ruff (line length 88, isort rules included), NumPy-style docstrings.
- Use uv for everything: `uv add <pkg>` / `uv add --dev <pkg>` to add dependencies,
  `uv run <cmd>` to run tools, `uv lock --upgrade` to update. Commit `uv.lock`.
  There is no `requirements.txt` and no `pip install`.
- Type checking uses ty (pre-1.0): if it reports a false positive, tune the rule in
  `[tool.ty.rules]` or add a targeted `# ty: ignore[rule]` with a reason.
- Configuration comes from environment variables; document each one in the README
  and add it to `.env.example` if a typical install needs it.
- Add or update a test with every behaviour change.
