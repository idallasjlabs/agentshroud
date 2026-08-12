#!/usr/bin/env bash
# run-tests-batched.sh — Run pytest in batches to stay within SSH timeout limits
#
# Usage: run-tests-batched.sh [batch_size] [pytest_args...]
#
# The full AgentShroud test suite (~1500+ tests) exceeds the SSH gateway
# exec timeout (600s). This script splits tests into batches of N files
# and runs each batch separately, collecting results.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™.

set -uo pipefail

BATCH_SIZE="${1:-10}"
shift 2>/dev/null || true
PYTEST_EXTRA_ARGS="$*"
VENV_PYTHON="$HOME/.venv/bin/python3"
TEST_DIR="gateway/tests"
RESULTS_DIR="/tmp/agentshroud-test-results"

mkdir -p "$RESULTS_DIR"

# Collect all test files
mapfile -t TEST_FILES < <(find "$TEST_DIR" -name 'test_*.py' -type f | sort)
TOTAL_FILES=${#TEST_FILES[@]}
TOTAL_BATCHES=$(( (TOTAL_FILES + BATCH_SIZE - 1) / BATCH_SIZE ))

echo "=== AgentShroud Batched Test Runner ==="
echo "Total test files: $TOTAL_FILES"
echo "Batch size: $BATCH_SIZE files"
echo "Total batches: $TOTAL_BATCHES"
echo ""

PASS_TOTAL=0
FAIL_TOTAL=0
ERROR_TOTAL=0
SKIP_TOTAL=0
FAILED_FILES=""

for ((i=0; i<TOTAL_FILES; i+=BATCH_SIZE)); do
    BATCH_NUM=$(( i / BATCH_SIZE + 1 ))
    BATCH_FILES=("${TEST_FILES[@]:i:BATCH_SIZE}")
    BATCH_FILE_LIST=$(printf '%s ' "${BATCH_FILES[@]}")

    echo "--- Batch $BATCH_NUM/$TOTAL_BATCHES (${#BATCH_FILES[@]} files) ---"

    # Run batch and capture output
    OUTPUT=$($VENV_PYTHON -m pytest $BATCH_FILE_LIST \
        --tb=no -q --no-header $PYTEST_EXTRA_ARGS 2>&1) || true

    # Parse results from the summary line (e.g., "143 passed, 2 skipped")
    SUMMARY=$(echo "$OUTPUT" | tail -1)
    echo "  $SUMMARY"

    # Extract counts
    PASSED=$(echo "$SUMMARY" | grep -oP '\d+ passed' | grep -oP '\d+' || echo 0)
    FAILED=$(echo "$SUMMARY" | grep -oP '\d+ failed' | grep -oP '\d+' || echo 0)
    ERRORS=$(echo "$SUMMARY" | grep -oP '\d+ error' | grep -oP '\d+' || echo 0)
    SKIPPED=$(echo "$SUMMARY" | grep -oP '\d+ skipped' | grep -oP '\d+' || echo 0)

    PASS_TOTAL=$((PASS_TOTAL + PASSED))
    FAIL_TOTAL=$((FAIL_TOTAL + FAILED))
    ERROR_TOTAL=$((ERROR_TOTAL + ERRORS))
    SKIP_TOTAL=$((SKIP_TOTAL + SKIPPED))

    if [ "$FAILED" -gt 0 ] || [ "$ERRORS" -gt 0 ]; then
        FAILED_FILES="$FAILED_FILES $BATCH_FILE_LIST"
    fi

    # Save batch output
    echo "$OUTPUT" > "$RESULTS_DIR/batch-$BATCH_NUM.txt"
done

echo ""
echo "=== FINAL RESULTS ==="
echo "Passed:  $PASS_TOTAL"
echo "Failed:  $FAIL_TOTAL"
echo "Errors:  $ERROR_TOTAL"
echo "Skipped: $SKIP_TOTAL"
echo "Total:   $((PASS_TOTAL + FAIL_TOTAL + ERROR_TOTAL + SKIP_TOTAL))"

if [ "$FAIL_TOTAL" -gt 0 ] || [ "$ERROR_TOTAL" -gt 0 ]; then
    echo ""
    echo "FAILED FILES: $FAILED_FILES"
    echo "Details in: $RESULTS_DIR/"
    exit 1
fi

echo ""
echo "ALL TESTS PASSED"
exit 0
