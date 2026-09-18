#!/usr/bin/env bash
# scripts/check-soak-status.sh — Soak-period gate for the OpenClaw bot
#
# post-deploy-check.sh proves the stack BOOTED. This proves it has actually
# RUN something real since that boot. A container can pass every
# post-deploy-check.sh assertion and still be broken in a way that only
# shows up once a real scheduled job fires — the models.json/openai-local
# gap, the missing sandbox image, and the op-proxy allowlist gaps fixed
# 2026-09-18 were all exactly this class of bug, invisible to any boot-time
# check. This script is the gate that should run BEFORE promoting a dev
# build to prod: it requires at least one real cron job to have completed
# successfully since the container's current boot, and fails loudly if any
# job that fired since boot errored.
#
# SCOPE: OpenClaw only. Hermes's `hermes cron runs`/`list` CLI has no --json
# output (checked 2026-09-18) — a reliable soak-check for it would mean
# parsing its human-formatted table output, which is fragile enough to be
# its own follow-up rather than bolted on here. Hermes soak coverage is not
# yet implemented.
#
# Usage:
#   bash scripts/check-soak-status.sh [--min-successes N] [--container NAME]
#
# Exit codes:
#   0  — soaked: at least --min-successes jobs completed OK since boot, none errored
#   1  — not yet soaked, or a job that fired since boot errored
#   2  — could not determine (container not found, CLI unavailable, etc.)

set -euo pipefail

MIN_SUCCESSES="${AGENTSHROUD_SOAK_MIN_SUCCESSES:-1}"
BOT_CONTAINER="${AGENTSHROUD_SOAK_CONTAINER:-}"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --min-successes) shift; MIN_SUCCESSES="${1:-1}"; shift ;;
        --container)     shift; BOT_CONTAINER="${1:-}"; shift ;;
        *) echo "Unknown argument: $1" >&2; exit 2 ;;
    esac
done

if [[ -z "$BOT_CONTAINER" ]]; then
    BOT_CONTAINER=$(docker ps --filter 'label=com.docker.compose.service=openclaw' --format '{{.Names}}' 2>/dev/null | head -1)
fi

if [[ -z "$BOT_CONTAINER" ]]; then
    echo "  [soak-status] UNKNOWN: no running OpenClaw container found" >&2
    exit 2
fi

started_at=$(docker inspect --format '{{.State.StartedAt}}' "$BOT_CONTAINER" 2>/dev/null || echo "")
if [[ -z "$started_at" ]]; then
    echo "  [soak-status] UNKNOWN: could not read $BOT_CONTAINER's StartedAt" >&2
    exit 2
fi

started_at_ms=$(python3 -c "
import datetime, sys
ts = sys.argv[1].split('.')[0].rstrip('Z')
dt = datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S').replace(tzinfo=datetime.timezone.utc)
print(int(dt.timestamp() * 1000))
" "$started_at" 2>/dev/null || echo "")

if [[ -z "$started_at_ms" ]]; then
    echo "  [soak-status] UNKNOWN: could not parse StartedAt '$started_at'" >&2
    exit 2
fi

echo "  [soak-status] $BOT_CONTAINER booted at $started_at (${started_at_ms}ms epoch)"

cron_json=$(docker exec "$BOT_CONTAINER" sh -c 'NODE_OPTIONS= openclaw cron list --json 2>/dev/null' || echo "")
if [[ -z "$cron_json" ]]; then
    echo "  [soak-status] UNKNOWN: 'openclaw cron list --json' produced no output" >&2
    exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set +e  # soak_status.py is expected to exit non-zero on NOT_SOAKED — under
        # `set -e` that would abort this script before the diagnostic
        # message below ever printed.
result=$(python3 "${SCRIPT_DIR}/soak_status.py" "$started_at_ms" "$MIN_SUCCESSES" <<< "$cron_json")
status=$?
set -e

echo "  [soak-status] $result"
exit "$status"
