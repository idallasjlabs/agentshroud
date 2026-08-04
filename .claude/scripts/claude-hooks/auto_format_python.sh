#!/usr/bin/env bash
set -euo pipefail

# Only run if Python files were modified in the last tool call
changed_files="$(git diff --name-only HEAD 2>/dev/null || true)"

py_files=$(echo "$changed_files" | grep -E '\.py$' || true)
if [[ -n "$py_files" ]]; then
  echo "🧹 Running Python formatters (ruff + black)..."

  if command -v ruff >/dev/null 2>&1; then
    echo "$py_files" | xargs ruff check --fix --force-exclude || true
  fi

  if command -v black >/dev/null 2>&1; then
    echo "$py_files" | xargs black || true
  fi
fi
