#!/usr/bin/env bash
set -euo pipefail

# Only run if Python files were modified in the last tool call
changed_files="$(git diff --name-only HEAD 2>/dev/null || true)"

if echo "$changed_files" | grep -qE '\.py$'; then
  echo "🧹 Running Python formatters (ruff + black)..."

  if command -v ruff >/dev/null 2>&1; then
    ruff check . --fix || true
  fi

  if command -v black >/dev/null 2>&1; then
    black . || true
  fi
fi
