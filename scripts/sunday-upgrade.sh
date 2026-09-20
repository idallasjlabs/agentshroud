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
for _bin in tmux claude docker colima git; do
  command -v "$_bin" >/dev/null 2>&1 || missing="${missing} ${_bin}"
done
if [ -n "$missing" ]; then
  echo "[sunday-upgrade] FATAL: required binary/binaries not on PATH:${missing}" >&2
  echo "[sunday-upgrade] PATH was: $PATH" >&2
  exit 127
fi

# ── Colima auto-start ─────────────────────────────────────────────────────────
# Added 2026-09-19, the night before this job's first unattended Sunday firing:
# neither this account nor the dev account has a LaunchAgent that brings Colima
# back up after a reboot (confirmed empty on both -- `launchctl list | grep
# colima` and `~/Library/LaunchAgents/` had nothing), and this script never
# checked or started it either -- DOCKER_HOST above just points at a socket
# that may not exist yet. Without this, tmux/claude/git all launch fine (none
# of them need Docker), so the mission session would start successfully and
# only fall apart confusingly on its FIRST real docker call, deep inside the
# mission, instead of failing fast and clearly right here. Idempotent: a
# `colima status` check up front means an already-running Colima (the normal
# case on any non-post-reboot Sunday) costs one fast status call, not a
# needless restart.
if ! colima status >/dev/null 2>&1; then
  echo "[sunday-upgrade] Colima is not running -- starting it before anything else needs Docker..."
  if ! timeout 300 colima start; then
    echo "[sunday-upgrade] FATAL: colima start failed or did not finish within 300s." >&2
    echo "[sunday-upgrade] Nothing past this point can reach Docker. Resolve manually: colima start" >&2
    exit 126
  fi
  echo "[sunday-upgrade] Colima started."
else
  echo "[sunday-upgrade] Colima already running."
fi

# ── On-demand invocation (owner directive 2026-09-15) ────────────────────────
# The weekly launchd firing is not the only way this must run: a major advisory
# can land on a Tuesday. The idempotency guards below deliberately make a second
# run on the same day a no-op, which is right for launchd retries and wrong for
# "a CVE just dropped, run it now" — so --force is the documented escape hatch.
#
#   bash scripts/sunday-upgrade.sh                       # normal (launchd/weekly)
#   bash scripts/sunday-upgrade.sh --force               # run now, ignore today's guards
#   bash scripts/sunday-upgrade.sh --force --reason "GHSA-xxxx dropped"
#
# --force does NOT weaken any safety gate inside sunday-upgrade-apply.sh: the
# preflight/scan/verify/soak/rollback and the no-op gate all still apply. It
# only bypasses the "already ran today" short-circuit.
FORCE=0
RUN_REASON="scheduled weekly run"
while [ $# -gt 0 ]; do
  case "$1" in
    --force)  FORCE=1; shift ;;
    --reason) RUN_REASON="${2:-unspecified}"; shift 2 ;;
    -h|--help)
      sed -n '1,30p' "${BASH_SOURCE[0]}"
      exit 0 ;;
    *)
      echo "[sunday-upgrade] unknown argument: $1" >&2
      exit 2 ;;
  esac
done

REPO=~/Development/agentshroud
# A forced run must not collide with the day's scheduled session name, or the
# tmux guard below would treat it as "already running" and silently skip.
if [ "$FORCE" -eq 1 ]; then
  SESSION="agentshroud-upgrade-$(date +%F-%H%M%S)"
else
  SESSION="agentshroud-upgrade-$(date +%F)"
fi
PROMPT_FILE="$REPO/prompts/sunday-upgrade.md"
TODAY="$(date +%F)"
LOG="$REPO/reports/upgrade-run-${TODAY}.log"
REPORT_MD="$REPO/reports/upgrade-${TODAY}.md"
HERMES_CONTAINER="agentshroud-hermes-v2"
WATCH_TIMEOUT_MIN=180   # prompt's own budget is 90 min; hard stop at 3h

cd "$REPO"
mkdir -p reports

# ── Branch/freshness preflight — the job must run against current main ──────
# This script previously trusted whatever was checked out on the host, with no
# `git pull`/`git fetch` anywhere in this file, prompts/sunday-upgrade.md, or
# sunday-upgrade-apply.sh. A fix merged to main mid-week (e.g. 2026-09-12's
# #439) had no way to reach an unattended run until SOME LATER session
# happened to manually check out and pull main first — the 2026-09-06 run
# failed with a stale composer-submission bug that had already been fixed on
# main days earlier (see reports/upgrade-2026-09-06-prod.md, "dev is still on
# the older send-keys version and needs to pull"), and the identical failure
# recurred on 2026-09-13 for the same reason: nobody had happened to git pull
# in between. A host used for interactive dev work (this one) routinely sits
# on a feature branch with uncommitted changes between Sunday runs — exactly
# the state as of 2026-09-16 while this fix was written — so the unattended
# job cannot assume main is checked out either.
#
# Fail loudly here rather than silently run stale code or the wrong branch:
# a launchd/cron failure that emails/logs an actionable error is recoverable;
# a "successful" run against a week-old checkout or someone's feature branch
# is not, and reads as a completed upgrade when nothing current was applied.
# Retried, not single-shot. This job fires once a week (0 3 * * 0), so a
# single transient fetch failure forfeits the ENTIRE week — which is exactly
# what happened on 2026-09-20: the 03:02 run died here at the first attempt
# and nothing retried it, so no upgrade ran that Sunday. This host sees
# intermittent transport failures to some CDNs (verified 2026-09-20: streams
# from files.pythonhosted.org abort at random sizes with TLS "bad decrypt",
# while a 41.9MB file from another host downloads fine), so one blip must not
# cost a week. Backoff is 30/60/90/120s — about 5 minutes total, negligible
# against a weekly job with a 90-minute budget.
_fetch_ok=0
for _try in 1 2 3 4 5; do
  if git fetch origin main >/dev/null 2>&1; then
    _fetch_ok=1
    [ "$_try" -gt 1 ] && echo "[sunday-upgrade] git fetch succeeded on attempt ${_try}."
    break
  fi
  if [ "$_try" -lt 5 ]; then
    echo "[sunday-upgrade] git fetch origin main failed (attempt ${_try}/5) — retrying in $((_try * 30))s."
    sleep $((_try * 30))
  fi
done
if [ "$_fetch_ok" -ne 1 ]; then
  echo "[sunday-upgrade] FATAL: git fetch origin main failed after 5 attempts — check network/auth before the next scheduled run." >&2
  exit 3
fi
_current_branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"
if [ "$_current_branch" != "main" ]; then
  echo "[sunday-upgrade] FATAL: repo checkout is on branch '${_current_branch}', not main." >&2
  echo "[sunday-upgrade] The unattended upgrade must run against main. Run: git -C '$REPO' checkout main" >&2
  exit 4
fi
# A blanket FATAL-on-any-dirty-file here contradicts this job's own mission
# (prompts/sunday-upgrade.md, "Preflight" ground rules): graphify-out/** NEVER
# counts as dirty (repo hooks regenerate it every branch switch), and other
# pre-existing uncommitted files should be listed and PROCEEDED past, not
# treated as fatal — this script never commits or builds from the working
# tree itself, so unrelated WIP elsewhere in the repo is not its concern. This
# host is explicitly documented above as "routinely" carrying uncommitted
# state between Sunday runs, so an unconditional FATAL here reliably blocked
# every unattended run before the mission ever got a chance to start —
# confirmed live 2026-09-17 (this script's own prior bugfix commit was still
# unstaged when this check fired). The real, safety-critical dirty-build gate
# already lives downstream in sunday-upgrade-apply.sh's `_dirty_build_files`
# (only the actual Docker build context, hard-refuses without
# --allow-dirty-build) — this launcher-level check only needs to catch a
# genuinely broken checkout, not routine dev-host state.
# Unanchored `grep -v` (not `^.. graphify-out/`) is deliberate: git quotes
# porcelain paths containing spaces/special chars, so an anchored pattern
# misses those lines — same defect already fixed in sunday-upgrade-apply.sh's
# _dirty_build_files (see its comment for the 17999-vs-68 miscount).
_dirty="$(git status --porcelain 2>/dev/null | grep -v 'graphify-out/' || true)"
if [ -n "$_dirty" ]; then
  _n="$(printf '%s\n' "$_dirty" | wc -l | tr -d ' ')"
  echo "[sunday-upgrade] NOTE: ${_n} uncommitted change(s) present outside graphify-out/ — proceeding (this script does not build or commit from the working tree):" >&2
  printf '%s\n' "$_dirty" | sed 's/^/[sunday-upgrade]   /' >&2
fi
# `is-ancestor HEAD origin/main` alone only detects "local is behind or equal".
# When local has unpushed commits ahead of origin/main (e.g. a same-session
# graphify-refresh commit sweep) that check is FALSE too, indistinguishable
# from true divergence — a real run on 2026-09-17 hit this exact case (68
# local-only commits, 0 behind) and FATAL'd on "diverged" when there was
# nothing to fast-forward and nothing wrong. Only neither-is-ancestor is a
# genuine divergence that `--ff-only` cannot resolve.
if git merge-base --is-ancestor origin/main HEAD 2>/dev/null; then
  echo "[sunday-upgrade] ✓ main is at or ahead of origin/main ($(git rev-parse --short HEAD)) — nothing to fast-forward"
elif git merge-base --is-ancestor HEAD origin/main 2>/dev/null; then
  _before_sha="$(git rev-parse --short HEAD)"
  git merge --ff-only origin/main
  echo "[sunday-upgrade] ✓ Fast-forwarded main ${_before_sha} → $(git rev-parse --short HEAD)"
else
  echo "[sunday-upgrade] FATAL: local main has diverged from origin/main — cannot fast-forward." >&2
  echo "[sunday-upgrade] Resolve manually: git -C '$REPO' log --oneline main..origin/main" >&2
  exit 4
fi

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
if [ "$FORCE" -eq 1 ]; then
  echo "[sunday-upgrade] --force: on-demand run (reason: ${RUN_REASON})"
  echo "[sunday-upgrade] --force: bypassing today's completion/report guards."
  echo "[sunday-upgrade] --force: all safety gates in sunday-upgrade-apply.sh still apply."
elif [ -f "$DONE_MARKER" ]; then
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
#
# The `--` before the mission text is load-bearing, not stylistic. claude's
# `--allowedTools, --allowed-tools <tools...>` is a VARIADIC option (commander.js
# `<tools...>` — confirmed via `claude --help`): with no terminator, it greedily
# consumes every remaining positional argument as more tool names — including
# the entire mission prompt — then further splits each captured token on
# whitespace/comma (its own documented behavior: "Comma or space-separated
# list"). That is exactly what shattered the mission text into hundreds of
# fragments each logged as "Ignoring --allowedTools rule '...'" and left the
# composer completely EMPTY. Confirmed live 2026-09-17 by bisecting the actual
# bug with isolated tmux probes: (1) proved bash/tmux argv-passing itself was
# already 100% correct — the mission arrived as one intact argument either
# way; (2) proved even a two-word prompt failed identically, with or without
# --remote-control, ruling out prompt size/markdown entirely; (3) `claude
# --help` named the real cause; (4) a live `-- '<prompt>'` probe fixed it,
# confirmed again with --remote-control included. Every prior run of this job
# had this defect when SUNDAY_UPGRADE_AUTON=1 set --allowedTools — none of
# them ever actually submitted a mission; they sat open until the 180-minute
# watch timeout believing they were unattended.
tmux new-session -d -s "$SESSION" -c "$REPO" \
  "claude --remote-control --name '$SESSION' $EXTRA -- \"\$(cat '$PROMPT_FILE')\""
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
