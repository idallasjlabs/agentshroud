#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
#
# One-time cleanup: delete duplicate Hermes cron jobs, keeping one of each name.
# Idempotent — safe to run multiple times; a second run is a no-op.
#
# Usage: bash docker/scripts/hermes-cron-dedup.sh
# Requires: agentshroud-hermes container running

set -euo pipefail

CONTAINER="${HERMES_CONTAINER:-agentshroud-hermes}"

echo "[hermes-dedup] Cleaning up duplicate cron jobs in ${CONTAINER}..."

docker exec "${CONTAINER}" sh -c '
    hermes cron list 2>/dev/null \
      | awk '"'"'
            /^  [a-f0-9]{12} \[/ { id = $1; next }
            /Name:/ { name = $0; if (seen[name]++) print id }
          '"'"' \
      | xargs -r -n1 hermes cron delete
'

echo "[hermes-dedup] Done. Current job counts:"
docker exec "${CONTAINER}" hermes cron list 2>/dev/null \
  | /usr/bin/grep "Name:" | sort | uniq -c | sort -rn
