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
# permission requests to the connected phone/desktop unless
# SUNDAY_UPGRADE_AUTON=1 (set by default in
# com.agentshroud.sunday-upgrade.plist as of 2026-09-06 — the job must run
# fully unattended every week, not opt-in per run).
#
# MUST run on the HOST (Hermes container has no claude/gh/repo — verified
# 2026-08-30). After the tmux session ends, the watcher stages the report
# into the hermes-config volume for the "Sunday Upgrade Report" no-agent
# cron (Sun 08:30 ET) to deliver via Telegram.

set -euo pipefail

# PATH hardening — DO NOT rely on the caller's PATH alone.
# launchd and cron both hand a job a minimal PATH that excludes Homebrew's bin
# dir, which is where tmux/claude/gh live on these machines. The 2026-09-06 dev
# run died at the `tmux new-session` line with "tmux: command not found" because
# that account's INSTALLED plist predates the PATH key in this repo's copy — a
# hand-copied plist that drifted. Setting PATH here too makes the script correct
# under any invocation (launchd, cron, manual, ssh) regardless of plist drift.
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"

# Fail loudly and specifically if a required binary is missing, instead of dying
# 40 lines later with a bare "command not found" that takes a session to diagnose.
missing=""
for _bin in tmux claude docker git; do
  command -v "$_bin" >/dev/null 2>&1 || missing="${missing} ${_bin}"
done
if [ -n "$missing" ]; then
  echo "[sunday-upgrade] FATAL: required binary/binaries not on PATH:${missing}" >&2
  echo "[sunday-upgrade] PATH was: $PATH" >&2
  exit 127
fi

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

# Idempotency: don't stack a second session if today's already running or
# already finished — guards against a manual re-trigger the same day, or
# launchd re-firing after a delayed wake (2026-09-06: a stale prior week's
# session name colliding was seen as "duplicate session" log noise).
if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[sunday-upgrade] tmux session ${SESSION} already running — skipping."
  exit 0
fi
# Skip only on a run that actually COMPLETED, tracked by an explicit sentinel.
# Previously this tested `[ -s "$REPORT_MD" ]`, which meant any run that died
# partway after writing even a stub report permanently blocked every retry for
# the rest of that day — the failure mode was self-perpetuating. A report that
# exists without its sentinel is an incomplete run and MUST be retryable.
DONE_MARKER="$REPO/reports/.upgrade-${TODAY}.done"
if [ -f "$DONE_MARKER" ]; then
  echo "[sunday-upgrade] run already completed today (${DONE_MARKER}) — skipping."
  exit 0
fi
if [ -s "$REPORT_MD" ]; then
  echo "[sunday-upgrade] NOTE: report ${REPORT_MD} exists but has no completion sentinel — treating as an incomplete run and re-running."
fi

EXTRA="--permission-mode acceptEdits"
if [ "${SUNDAY_UPGRADE_AUTON:-0}" = "1" ]; then
  EXTRA="$EXTRA --allowedTools Bash,Read,Edit,Write,Glob,Grep"
fi

echo "[sunday-upgrade] $(date '+%H:%M:%S') launching remote-control session '$SESSION'"
# NO pipe on claude's stdout: piping (e.g. `| tee`) makes stdout a non-TTY,
# claude falls back to --print mode, demands a prompt argument, and exits
# before send-keys can reach it ("can't find pane", observed 2026-08-30).
# tmux pipe-pane captures the log without stealing the TTY.
#
# Mission is passed as a positional argument at launch (not typed into a
# live composer afterward) — 2026-08-30/09-06: a separate send-keys paste
# followed by a retry-Enter loop was fragile (Claude Code's composer can
# swallow an Enter that arrives too soon after a large paste; the mission
# sat unsubmitted for 40+ min on two separate occasions despite a 3-attempt
# retry). Passing it as an argument at launch removes the race entirely —
# same pattern local-llms/scripts/sunday-maintenance.sh already uses.
tmux new-session -d -s "$SESSION" -c "$REPO" \
  "claude --remote-control --name '$SESSION' $EXTRA \"\$(cat '$PROMPT_FILE')\""
tmux pipe-pane -t "$SESSION" -o "cat >> '$LOG'"

# give it time to boot and register with claude.ai
sleep 20
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[sunday-upgrade] ERROR: session died during boot — see $LOG" >&2
  exit 1
fi
echo "[sunday-upgrade] mission submitted at launch — watch/steer from the phone (session: $SESSION)"

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

# Completion sentinel — only written once the run reached the end of the script.
# Guards same-day re-fires (see DONE_MARKER check above) WITHOUT trapping a
# failed run behind its own partial output.
touch "$DONE_MARKER"
echo "[sunday-upgrade] $(date '+%H:%M:%S') run complete (sentinel: $DONE_MARKER)"
