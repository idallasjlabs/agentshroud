#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# A8 verification helper: print the current greeter state file so the operator
# can confirm a real Telegram DM triggered the collaborator greeting (Item 10).
#
# Usage:
#   bash scripts/verify-greeter-state.sh
#
# Expect:   {"hermes:<owner_uid>": <unix_ts>, "openclaw:<owner_uid>": <unix_ts>}
# If empty: {}   → no greeting has fired yet; send /start to both bots first.

set -eu

CONTAINER="${1:-agentshroud-gateway}"
STATE_PATH="/app/data/collaborator_greetings.json"

echo "=== Greeter state (${CONTAINER}:${STATE_PATH}) ==="
docker exec "${CONTAINER}" cat "${STATE_PATH}" 2>/dev/null | python3 -m json.tool || echo "(file not found or not valid JSON)"
echo ""
echo "To reset a specific entry and re-trigger a greeting:"
echo "  docker exec ${CONTAINER} python3 -c \""
echo "    import json, os; p='${STATE_PATH}'; s=json.load(open(p)); s.pop('<bot_id>:<user_id>', None); json.dump(s, open(p, 'w'))\""
