#!/bin/sh
# Sunday Upgrade Report delivery — no-agent Hermes cron script (Sun 08:30 ET).
# Reads the report the host-side sunday-upgrade.sh staged and prints it once
# (stdout is delivered verbatim to Telegram; empty stdout = silent, so weeks
# where the host job didn't run produce no message at all).
# Canonical copy: agentshroud repo scripts/hermes-cron/; installed at
# /opt/data/scripts/ (the path the cron runner actually resolves).
F=/opt/data/reports/sunday-upgrade-latest.md
[ -s "$F" ] || exit 0
# Telegram caps messages ~4096 chars; lead with the summary, note truncation.
SIZE=$(wc -c < "$F")
head -c 3500 "$F"
if [ "$SIZE" -gt 3500 ]; then
  printf '\n\n[truncated — full report: reports/ in the agentshroud repo]\n'
fi
mv "$F" "$F.delivered"
