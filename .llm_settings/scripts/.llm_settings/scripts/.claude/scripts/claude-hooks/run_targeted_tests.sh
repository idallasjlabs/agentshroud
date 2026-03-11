#!/usr/bin/env bash
set -euo pipefail

# Detect changed Python files
changed_py="$(git diff --name-only HEAD 2>/dev/null | grep -E '\.py$' || true)"

if [[ -z "$changed_py" ]]; then
  exit 0
fi

# Run targeted tests for changed Python files
if command -v pytest >/dev/null 2>&1; then
  echo "🧪 Running targeted tests for changed files..."
  # Build test file list from changed Python files
  test_files=""
  for pyfile in $changed_py; do
    # Convert module path to test path (e.g., src/module.py -> tests/test_module.py)
    test_file="tests/test_$(basename "$pyfile")"
    if [ -f "$test_file" ]; then
      test_files="$test_files $test_file"
    fi
  done

  if [ -n "$test_files" ]; then
    pytest -q $test_files || true
  else
    # Fallback: run all quick tests if no specific test files found
    pytest -q -m "not slow" || true
  fi
fi
