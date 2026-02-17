#!/usr/bin/env bash
set -euo pipefail

mapfile -t changed_py < <(git diff --name-only HEAD 2>/dev/null | grep -E '\.py$' || true)

if [[ ${#changed_py[@]} -eq 0 ]]; then
  exit 0
fi

if command -v pytest >/dev/null 2>&1; then
  echo "🧪 Running targeted tests for changed files..."
  test_files=()
  for pyfile in "${changed_py[@]}"; do
    base="$(basename "$pyfile")"
    for test_dir in tests gateway/tests; do
      test_file="$test_dir/test_$base"
      if [ -f "$test_file" ]; then
        test_files+=("$test_file")
      fi
    done
  done

  if [[ ${#test_files[@]} -gt 0 ]]; then
    pytest -q "${test_files[@]}"
  else
    pytest -q -m "not slow"
  fi
fi
