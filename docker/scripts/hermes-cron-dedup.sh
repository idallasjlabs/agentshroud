#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
#
# One-time cleanup: delete duplicate Hermes cron jobs, keeping one of each name.
# Idempotent — safe to run multiple times; a second run is a no-op.
#
# Usage: bash docker/scripts/hermes-cron-dedup.sh
# Requires: agentshroud-hermes-v2 container running

set -euo pipefail

CONTAINER="${HERMES_CONTAINER:-agentshroud-hermes-v2}"

echo "[hermes-dedup] Cleaning up duplicate cron jobs in ${CONTAINER}..."

# `hermes` isn't on PATH inside the container (no /opt/hermes symlink into
# any bin dir) — must invoke via its own venv interpreter directly, same as
# every other in-container hermes CLI call in this repo. `--all` is required
# on both listings below: plain `cron list` hides paused jobs, and PR #431's
# root cause was exactly a dedupe pass that missed paused duplicates.
HERMES_CLI='/opt/hermes/.venv/bin/python3 /opt/hermes/hermes'

docker exec "${CONTAINER}" sh -c "
    ${HERMES_CLI} cron list --all 2>/dev/null \
      | awk '
            /^  [a-f0-9]{12} \[/ { id = \$1; next }
            /Name:/ { name = \$0; if (seen[name]++) print id }
          ' \
      | xargs -r -n1 ${HERMES_CLI} cron delete
"

echo "[hermes-dedup] Done. Current job counts:"
docker exec "${CONTAINER}" sh -c "${HERMES_CLI} cron list --all" 2>/dev/null \
  | /usr/bin/grep "Name:" | sort | uniq -c | sort -rn
