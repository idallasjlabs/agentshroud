#!/usr/bin/env bash
# Smoke test: OpenClaw's startup readiness poll must retry after its initial
# window expires, instead of permanently giving up.
#
# start-agentshroud.sh's readiness poll originally waited a fixed 120s (60 x
# 2s) for the HTTP/Telegram/model probes, then sent "readiness delayed" and
# exited its notification subshell for good — even if the container became
# fully healthy moments later. Real OpenClaw startup (npm reseeding + 3 SDK
# repatches every boot) frequently runs past 120s under host load, so this
# produced a false "delayed" state that never recovered to "online" for that
# boot. Recurring 2026-08-30, 2026-09-03, 2026-09-04.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FILE="$REPO/docker/scripts/start-agentshroud.sh"
fail=0

echo ""
echo "── OpenClaw readiness retry-after-expiry ───────────────"

check() {
    local label="$1" pattern="$2"
    if /usr/bin/grep -qE "$pattern" "$FILE"; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label — pattern not found in $FILE" >&2
        fail=1
    fi
}

check "extended readiness window is configurable" \
    'OPENCLAW_EXTENDED_READY_ITERATIONS'

check "extended poll is invoked after the initial window" \
    '_poll_openclaw_ready "\$\{_EXTENDED_READY_ITERATIONS\}"'

# Regression guard: the Telegram "readiness delayed" notification must be
# sent exactly once. Two sends (once when the initial window expires, once
# more in a leftover "give up" branch) would double-notify on every slow-but-
# eventually-healthy boot. (Slack gets its own, separate single send — not
# counted here.)
delayed_sends="$(/usr/bin/grep -c '_telegram_send "🟠 OpenClaw starting (readiness delayed)"' "$FILE")"
if [ "$delayed_sends" -eq 1 ]; then
    echo "  OK : Telegram 'readiness delayed' notification sent exactly once (found $delayed_sends)"
else
    echo "  FAIL: Telegram 'readiness delayed' notification found $delayed_sends times, expected exactly 1 — duplicate-send regression" >&2
    fail=1
fi

# Structural guard: the extended-poll call must sit between the initial
# readiness check and the final ready/not-ready branch, so a healthy-but-slow
# boot can still flip $ready to "yes" before that branch runs. Anchored to
# the bare call (not the "_reconcile_security_critical_cron() {" definition,
# which appears earlier in the file for an unrelated purpose).
initial_check_line="$(/usr/bin/grep -n '^\s*_poll_openclaw_ready 60\s*$' "$FILE" | head -1 | cut -d: -f1)"
extended_call_line="$(/usr/bin/grep -n '_poll_openclaw_ready "\${_EXTENDED_READY_ITERATIONS}"' "$FILE" | head -1 | cut -d: -f1)"
final_branch_line="$(/usr/bin/grep -n '^\s*_reconcile_security_critical_cron\s*$' "$FILE" | head -1 | cut -d: -f1)"
if [ -n "$initial_check_line" ] && [ -n "$extended_call_line" ] && [ -n "$final_branch_line" ] \
   && [ "$initial_check_line" -lt "$extended_call_line" ] && [ "$extended_call_line" -lt "$final_branch_line" ]; then
    echo "  OK : extended poll runs after the initial window and before the final ready branch"
else
    echo "  FAIL: expected order initial-poll(${initial_check_line:-?}) < extended-poll(${extended_call_line:-?}) < final-branch(${final_branch_line:-?})" >&2
    fail=1
fi

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
