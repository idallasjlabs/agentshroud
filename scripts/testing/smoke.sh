#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# smoke.sh — smoke / build-verification and post-deploy checks (i-integration-qa, i-release-gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="smoke"; T_SUMMARY="smoke / build-verification and post-deploy checks (i-integration-qa, i-release-gate)"
T_OPTIONS="Environment: I_SMOKE_CMD='<cmd>' or I_SMOKE_URLS='<url> <url>' (HTTP 2xx expected)."
t_parse "" "$@"; t_init
if [ -n "${I_SMOKE_CMD:-}" ]; then
    t_run smoke "$I_SMOKE_CMD"
elif [ -n "${I_SMOKE_URLS:-}" ]; then
    if t_have curl smoke-http; then
        for u in $I_SMOKE_URLS; do t_run "smoke-$u" "curl -fsS --max-time 10 -o /dev/null $u"; done
    fi
else
    t_skip smoke "no smoke target (set I_SMOKE_CMD or I_SMOKE_URLS)"
fi
t_finish
