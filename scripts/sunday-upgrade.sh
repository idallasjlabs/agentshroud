#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# sunday-upgrade.sh — Weekly (Sunday) upgrade run: headless Claude Code session
# driven by prompts/sunday-upgrade.md (owner-authored, 2026-08-30).
#
# MUST run on the HOST, not in a bot container: the Hermes container has no
# `claude`, no `gh`, and no ~/Development checkout (verified 2026-08-30).
# Hermes's role is delivery only — this wrapper drops the finished report
# into the hermes-config volume, where the "Sunday Upgrade Report" no-agent
# cron job (Sun 08:30 ET) reads it once and sends it to Telegram.
#
# The prompt itself owns all safety: rollback baseline before changes,
# dev-first promotion, pinned-stable-only versions, never loosening
# gateway/sandbox policy (BLOCKED instead), volume backups before prod,
# 90-minute budget, never ending with a broken stack.
#
# Usage: scripts/sunday-upgrade.sh
#   Headless permission note: --allowedTools pre-approves the listed tools;
#   anything else fails closed (a headless run cannot answer prompts).
#   Repo PreToolUse hooks (block_main_commits etc.) still apply.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

TODAY="$(date +%F)"
mkdir -p reports
RUN_LOG="reports/upgrade-run-${TODAY}.log"
REPORT_MD="reports/upgrade-${TODAY}.md"
HERMES_CONTAINER="agentshroud-hermes-v2"

echo "[sunday-upgrade] $(date '+%H:%M:%S') starting headless run (log: $RUN_LOG)"

set +e
claude -p "$(cat prompts/sunday-upgrade.md)" \
  --allowedTools "Bash,Read,Edit,Write,Glob,Grep" \
  --max-turns 300 \
  > "$RUN_LOG" 2>&1
CLAUDE_RC=$?
set -e
echo "[sunday-upgrade] $(date '+%H:%M:%S') claude exited rc=$CLAUDE_RC"

# Hand the report to Hermes for Telegram delivery. Prefer the structured
# report the run maintains from its first minutes; fall back to the raw log
# tail so even an aborted run reaches the owner.
DELIVER_SRC="$REPORT_MD"
if [ ! -s "$DELIVER_SRC" ]; then
  DELIVER_SRC="$RUN_LOG"
fi

if docker ps --format '{{.Names}}' | grep -q "^${HERMES_CONTAINER}$"; then
  docker exec "$HERMES_CONTAINER" mkdir -p /opt/data/reports
  docker cp "$DELIVER_SRC" "${HERMES_CONTAINER}:/opt/data/reports/sunday-upgrade-latest.md"
  docker exec -u root "$HERMES_CONTAINER" chown -R hermes:hermes /opt/data/reports
  echo "[sunday-upgrade] report staged for Hermes delivery"
else
  echo "[sunday-upgrade] WARN: ${HERMES_CONTAINER} not running — report NOT staged for Telegram (see $DELIVER_SRC)"
fi

exit "$CLAUDE_RC"
