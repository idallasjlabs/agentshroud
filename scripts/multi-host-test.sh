#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/multi-host-test.sh — SCRUM-91: multi-host test runner
#
# Runs a command (default: the smoke suite) across the lab hosts over SSH and
# prints an aggregated PASS/FAIL summary. Overall exit code is non-zero if ANY
# host failed or was unreachable, so a change can be validated on every runtime
# (x86/arm, differing container state) before a coordinated deploy.
#
# The coordinated multi-host DEPLOY (rolling apply + health-gated promotion) is
# a separate, larger follow-up and is intentionally NOT built here.
#
# Usage:
#   bash scripts/multi-host-test.sh                          # smoke on default hosts
#   bash scripts/multi-host-test.sh -- bash scripts/smoke.sh # explicit command
#   bash scripts/multi-host-test.sh --hosts marvin,trillian -- uptime
#   bash scripts/multi-host-test.sh --dry-run                # print plan, touch nothing
#
# Env overrides:
#   MULTI_HOST_HOSTS  — default host list (comma/space separated)
#   MULTI_HOST_USER   — remote SSH user (default: agentshroud-bot)
#   PYTHON            — python interpreter (default: python3)
#
# Exit 0 = every host passed. Non-zero = at least one host failed/unreachable.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON="${PYTHON:-python3}"

# Split caller args into wrapper flags (before `--`) and the remote command
# (after `--`). We forward everything straight to the Python module, which owns
# the argument contract; this keeps parsing in one tested place.
args=("$@")

# Apply env defaults ONLY when the caller did not pass the matching flag.
have_hosts=0
have_user=0
for a in "$@"; do
    case "$a" in
        --hosts | --hosts=*) have_hosts=1 ;;
        --user | --user=*) have_user=1 ;;
        --) break ;;
    esac
done

prefix=()
if [[ "$have_hosts" -eq 0 && -n "${MULTI_HOST_HOSTS:-}" ]]; then
    prefix+=(--hosts "$MULTI_HOST_HOSTS")
fi
if [[ "$have_user" -eq 0 && -n "${MULTI_HOST_USER:-}" ]]; then
    prefix+=(--user "$MULTI_HOST_USER")
fi

cd "$REPO"
exec "$PYTHON" -m gateway.tools.multi_host_test ${prefix[@]+"${prefix[@]}"} ${args[@]+"${args[@]}"}
