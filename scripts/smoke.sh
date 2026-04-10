#!/usr/bin/env bash
# scripts/smoke.sh — Startup smoke test runner
#
# Runs all static startup smoke tests and (when SMOKE_LIVE=1) the live boot test.
# Safe to run on any machine with bash + node.
#
# Usage:
#   bash scripts/smoke.sh                   # static tests only
#   SMOKE_LIVE=1 bash scripts/smoke.sh      # static + live boot test
#
# Exit 0 = all tests passed. Exit 1 = one or more failures.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"
SMOKE_DIR="$REPO/tests/startup_smoke"

pass_suites=0
fail_suites=0

run_test() {
    local name="$1"
    local cmd=("${@:2}")
    echo ""
    echo "──────────────────────────────────────────────────────"
    if "${cmd[@]}"; then
        echo "  SUITE PASS: $name"
        (( pass_suites++ )) || true
    else
        echo "  SUITE FAIL: $name"
        (( fail_suites++ )) || true
    fi
}

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║  AgentShroud™ — Startup Smoke Tests                  ║"
echo "╚══════════════════════════════════════════════════════╝"

# Static assertion suite (no Docker required)
run_test "test_bot_boot_static.sh" bash "$SMOKE_DIR/test_bot_boot_static.sh"

# apply-patches.js behavioral assertions (requires node)
if command -v node &> /dev/null; then
    run_test "test_apply_patches.js" node "$SMOKE_DIR/test_apply_patches.js"
else
    echo ""
    echo "  SKIP: test_apply_patches.js — node not found in PATH"
fi

# setup-secrets.sh behavioral assertions
run_test "test_setup_secrets.sh" bash "$SMOKE_DIR/test_setup_secrets.sh"

# Live boot test (gated by SMOKE_LIVE=1)
run_test "test_bot_boot_live.sh" bash "$SMOKE_DIR/test_bot_boot_live.sh"

# ── Summary ────────────────────────────────────────────────────────────────
echo ""
echo "══════════════════════════════════════════════════════"
total=$(( pass_suites + fail_suites ))
echo "  Suites: ${total}  Passed: ${pass_suites}  Failed: ${fail_suites}"
echo "══════════════════════════════════════════════════════"
echo ""

[[ "$fail_suites" -eq 0 ]]
