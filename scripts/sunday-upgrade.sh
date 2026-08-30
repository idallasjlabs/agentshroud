#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# sunday-upgrade.sh — Weekly (Sunday) upgrade run as a REMOTE CONTROL session
# (owner sketch 2026-08-30): the run is visible and steerable from the phone
# via claude.ai, instead of a blind headless `claude -p`.
#
# The session is driven by prompts/sunday-upgrade.md (owner-authored).
# Permission mode is acceptEdits — file edits auto-approve; Bash calls queue
# permission requests to the connected phone/desktop. Pre-approve Bash via
# SUNDAY_UPGRADE_AUTON=1 if a given week should run fully unattended.
#
# MUST run on the HOST (Hermes container has no claude/gh/repo — verified
# 2026-08-30). After the tmux session ends, the watcher stages the report
# into the hermes-config volume for the "Sunday Upgrade Report" no-agent
# cron (Sun 08:30 ET) to deliver via Telegram.

set -euo pipefail

REPO=~/Development/agentshroud
SESSION="agentshroud-upgrade-$(date +%F)"
PROMPT_FILE="$REPO/prompts/sunday-upgrade.md"
TODAY="$(date +%F)"
LOG="$REPO/reports/upgrade-run-${TODAY}.log"
REPORT_MD="$REPO/reports/upgrade-${TODAY}.md"
HERMES_CONTAINER="agentshroud-hermes-v2"
WATCH_TIMEOUT_MIN=180   # prompt's own budget is 90 min; hard stop at 3h

cd "$REPO"
mkdir -p reports

EXTRA_FLAGS=()
if [ "${SUNDAY_UPGRADE_AUTON:-0}" = "1" ]; then
  EXTRA_FLAGS+=(--allowedTools "Bash,Read,Edit,Write,Glob,Grep")
fi

echo "[sunday-upgrade] $(date '+%H:%M:%S') launching remote-control session '$SESSION'"
tmux new-session -d -s "$SESSION" -c "$REPO" \
  "claude --remote-control --name '$SESSION' --permission-mode acceptEdits ${EXTRA_FLAGS[*]+"${EXTRA_FLAGS[*]}"} 2>&1 | tee '$LOG'"

# give it time to boot and register with claude.ai
sleep 20
tmux send-keys -t "$SESSION" -l "$(cat "$PROMPT_FILE")"
tmux send-keys -t "$SESSION" Enter
echo "[sunday-upgrade] mission sent — watch/steer from the phone (session: $SESSION)"

# Wait for the session to finish, then stage the report for Hermes delivery.
elapsed=0
while tmux has-session -t "$SESSION" 2>/dev/null; do
  sleep 60
  elapsed=$((elapsed + 1))
  if [ "$elapsed" -ge "$WATCH_TIMEOUT_MIN" ]; then
    echo "[sunday-upgrade] WARN: session still open after ${WATCH_TIMEOUT_MIN}m — staging whatever report exists and leaving the session running"
    break
  fi
done

DELIVER_SRC="$REPORT_MD"
[ -s "$DELIVER_SRC" ] || DELIVER_SRC="$LOG"
if [ -s "$DELIVER_SRC" ] && docker ps --format '{{.Names}}' | grep -q "^${HERMES_CONTAINER}$"; then
  docker exec "$HERMES_CONTAINER" mkdir -p /opt/data/reports
  docker cp "$DELIVER_SRC" "${HERMES_CONTAINER}:/opt/data/reports/sunday-upgrade-latest.md"
  docker exec -u root "$HERMES_CONTAINER" chown -R hermes:hermes /opt/data/reports
  echo "[sunday-upgrade] report staged for Hermes Telegram delivery"
else
  echo "[sunday-upgrade] WARN: no report staged (missing report/log or ${HERMES_CONTAINER} not running)"
fi
