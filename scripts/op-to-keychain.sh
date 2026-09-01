#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# op-to-keychain.sh — Mirror the "Agent Shroud Bot Credentials" 1Password
# vault into the macOS login Keychain, so scripts read secrets via
# `security find-generic-password` WITHOUT a Touch ID prompt.
#
# Owner request 2026-09-01: op's biometric prompt doesn't work over remote
# sessions; the login keychain (unlocked whenever the user is logged in at
# the console) works for both local and SSH use. macOS ONLY — other systems
# keep their existing op/secret-file flows unchanged.
#
# Run this ONCE while at the Mac (op will prompt Touch ID a single time);
# re-run any time to refresh values. Values stream op -> security directly;
# nothing is echoed, logged, or written to disk.
#
# Read side (any script, no prompt):
#   security find-generic-password -s "agentshroud/<item-name>/<field>" -w
#
# Usage: scripts/op-to-keychain.sh [--dry-run]

set -euo pipefail

VAULT="Agent Shroud Bot Credentials"   # ONLY this vault — Private is off-limits (owner rule)
PREFIX="agentshroud"
DRY_RUN=false
[ "${1:-}" = "--dry-run" ] && DRY_RUN=true

command -v op >/dev/null || { echo "op CLI not found" >&2; exit 1; }
[ "$(uname -s)" = "Darwin" ] || { echo "macOS only — other systems keep as-is" >&2; exit 1; }

echo "Mirroring vault '$VAULT' -> login keychain (prefix: ${PREFIX}/)..."
count=0
op item list --vault "$VAULT" --format json \
  | /usr/bin/python3 -c "import json,sys; [print(i['id']+'\t'+i['title']) for i in json.load(sys.stdin)]" \
  | while IFS="$(printf '\t')" read -r item_id title; do
      # Every concealed/text field with a value becomes one keychain entry:
      # service = agentshroud/<item title>/<field label>, account = $USER.
      op item get "$item_id" --vault "$VAULT" --format json \
        | /usr/bin/python3 -c "
import json, sys
item = json.load(sys.stdin)
for f in item.get('fields', []):
    if f.get('value') and f.get('type') in ('CONCEALED', 'STRING'):
        label = (f.get('label') or f.get('id') or 'value').strip()
        print(label + '\t' + f['value'])
" \
        | while IFS="$(printf '\t')" read -r label value; do
            svc="${PREFIX}/${title}/${label}"
            if $DRY_RUN; then
              echo "  would store: $svc"
            else
              # -U updates in place; value passed via -w argument (not shown in ps
              # long enough to matter on a single-user machine; avoids tmp files)
              security add-generic-password -U -a "$USER" -s "$svc" -w "$value" >/dev/null
              echo "  stored: $svc"
            fi
            count=$((count+1))
          done
    done
echo "Done. Read anywhere with:"
echo "  security find-generic-password -s '${PREFIX}/<item>/<field>' -w"
