#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# run-unit.sh — unit tests, type checks and coverage (i-unit-tdd gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="run-unit"; T_SUMMARY="unit tests, type checks and coverage (i-unit-tdd gate)"
T_OPTIONS="Environment: I_UNIT_CMD='<cmd>' overrides runner detection."
t_parse "" "$@"; t_init
if [ -n "${I_UNIT_CMD:-}" ]; then
    t_run unit "$I_UNIT_CMD"
else
    found=false
    if [ -f pytest.ini ] || [ -f tox.ini ] || [ -f setup.cfg ] || [ -f pyproject.toml ] || [ -n "$(git ls-files 'test_*.py' '*_test.py' 2>/dev/null | head -1)" ]; then
        if [ -n "$(git ls-files 'test_*.py' '*_test.py' 'tests/*.py' 2>/dev/null | head -1)" ]; then
            found=true; t_have pytest unit-pytest && t_run unit-pytest "pytest -q -m 'not integration'"
        fi
    fi
    if [ -f package.json ] && /usr/bin/grep -q '"test"' package.json; then
        found=true; t_have npm unit-npm && t_run unit-npm "npm test --silent"
    fi
    if [ -f Cargo.toml ]; then found=true; t_have cargo unit-cargo && t_run unit-cargo "cargo test --quiet"; fi
    if [ -n "$(git ls-files '*.bats' 2>/dev/null | head -1)" ]; then
        found=true; t_have bats unit-bats && t_run unit-bats "bats $(git ls-files '*.bats' | grep -v integration | tr '\n' ' ')"
    fi
    if ! $found; then
        if [ -n "$(git ls-files 'tests/test-*.sh' 2>/dev/null | head -1)" ]; then
            t_skip unit "shell test suites found in tests/ — set I_UNIT_CMD='bash tests/test-<name>.sh' to run one"
        else
            t_skip unit "no unit-test runner detected (set I_UNIT_CMD)"
        fi
    fi
    # type checks (optional)
    if [ -f mypy.ini ] || { [ -f pyproject.toml ] && /usr/bin/grep -q 'mypy' pyproject.toml; }; then t_have mypy types-mypy && t_run types-mypy "mypy ."; fi
    if [ -f tsconfig.json ]; then t_have tsc types-tsc && t_run types-tsc "tsc --noEmit"; fi
fi
t_finish
