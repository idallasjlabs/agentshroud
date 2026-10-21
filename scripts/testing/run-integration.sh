#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# run-integration.sh — integration, regression and migration tests (i-integration-qa gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="run-integration"; T_SUMMARY="integration, regression and migration tests (i-integration-qa gate)"
T_OPTIONS="Environment: I_INTEGRATION_CMD='<cmd>' overrides runner detection."
t_parse "" "$@"; t_init
if [ -n "${I_INTEGRATION_CMD:-}" ]; then
    t_run integration "$I_INTEGRATION_CMD"
else
    found=false
    if [ -d tests/integration ] && [ -n "$(git ls-files 'tests/integration/*.py' 2>/dev/null | head -1)" ]; then
        found=true; t_have pytest integration-pytest && t_run integration-pytest "pytest -q tests/integration"
    elif [ -n "$(git grep -l 'mark.integration' -- '*.py' 2>/dev/null | head -1)" ]; then
        found=true; t_have pytest integration-pytest && t_run integration-pytest "pytest -q -m integration"
    fi
    if [ -n "$(git ls-files 'tests/integration/*.sh' 2>/dev/null | head -1)" ]; then
        found=true
        for f in $(git ls-files 'tests/integration/*.sh'); do t_run "integration-$(basename "$f" .sh)" "bash $f"; done
    fi
    $found || t_skip integration "no integration tests detected (tests/integration or -m integration; set I_INTEGRATION_CMD)"
fi
t_finish
