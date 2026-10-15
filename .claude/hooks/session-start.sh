#!/bin/bash
# Prepares Claude Code on the web sessions: a uv-managed venv with the dev tools on PATH,
# so `make check` works straight away. No-op on local machines.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# uv manages the venv (.venv) and installs from uv.lock.
if ! command -v uv >/dev/null 2>&1; then
  python3 -m pip install --quiet uv
fi
uv sync --quiet

# Put the venv first on PATH so `ruff`, `pytest` and `ty` resolve to it.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export VIRTUAL_ENV=\"$CLAUDE_PROJECT_DIR/.venv\"" >> "$CLAUDE_ENV_FILE"
  echo "export PATH=\"$CLAUDE_PROJECT_DIR/.venv/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
