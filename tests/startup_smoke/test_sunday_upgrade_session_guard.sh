#!/usr/bin/env bash
# Behavioral test for sunday-upgrade.sh's _session_guard and _return_to_main.
#
# 2026-10-11 on dev, every fire after 03:00 was lost:
#   05:00  FATAL "repo checkout is on branch 'chore/upgrade-2026-10-11', not
#          main" — the 03:00 session was still running on its branch, and the
#          branch guard ran BEFORE the "already running" check.
#   11:00  "tmux session ... already running — skipping" — the 08:00 session's
#          watcher kills at 180m + boot, i.e. ~40s AFTER the 11:00 fire.
# The fix runs the session guard first (an overlapping fire skips cleanly),
# reaps a session older than its budget whose watcher is gone, and returns a
# reaped run's checkout to main so the branch guard that follows can pass.
#
# Same pattern as test_sunday_upgrade_head_guard.sh: extract the REAL function
# text from the script (its top level launches tmux/claude) and run it against
# a fake tmux and a scratch git repo.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SCRIPT="$REPO_ROOT/scripts/sunday-upgrade.sh"
fail=0

extract_fn() {
  local name="$1" start close
  start="$(grep -n "^${name}() {\$" "$SCRIPT" | head -1 | cut -d: -f1)"
  [ -n "$start" ] || { echo "  FAIL: ${name} not found in $SCRIPT" >&2; return 1; }
  close="$(tail -n "+${start}" "$SCRIPT" | grep -n '^}$' | head -1 | cut -d: -f1)"
  sed -n "${start},$((start + close - 1))p" "$SCRIPT"
}

GUARD_SRC="$(extract_fn _session_guard)" || exit 1
RETURN_SRC="$(extract_fn _return_to_main)" || exit 1
eval "$GUARD_SRC"
eval "$RETURN_SRC"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Fake tmux: one session whose creation time lives in $TMP/created; an absent
# file means no session. kill-session removes it and logs the call.
mkdir -p "$TMP/bin"
cat > "$TMP/bin/tmux" <<EOF
#!/usr/bin/env bash
state="$TMP/created"
case "\$1" in
  has-session)     [ -f "\$state" ] ;;
  display-message) cat "\$state" ;;
  kill-session)    echo killed >> "$TMP/kills"; rm -f "\$state" ;;
  *)               exit 0 ;;
esac
EOF
chmod +x "$TMP/bin/tmux"
PATH="$TMP/bin:$PATH"

echo ""
echo "── _session_guard ──"

rm -f "$TMP/created" "$TMP/kills"
got="$(_session_guard s 180)"
if [ "$got" = "none" ]; then echo "  OK : no session -> none"
else echo "  FAIL: no session -> '$got', want none" >&2; fail=1; fi

echo "$(( $(date +%s) - 120 * 60 ))" > "$TMP/created"
got="$(_session_guard s 180)"
if [ "$got" = "running" ] && [ ! -f "$TMP/kills" ]; then
  echo "  OK : a 2h-old session (03:00 run at the 05:00 fire) -> running, not killed"
else echo "  FAIL: 2h-old session -> '$got' (kills: $(cat "$TMP/kills" 2>/dev/null))" >&2; fail=1; fi

echo "$(( $(date +%s) - 181 * 60 ))" > "$TMP/created"
got="$(_session_guard s 180)"
if [ "$got" = "reaped" ] && [ -f "$TMP/kills" ] && [ ! -f "$TMP/created" ]; then
  echo "  OK : a session past its budget -> killed and reported reaped"
else echo "  FAIL: overdue session -> '$got' (still present: $([ -f "$TMP/created" ] && echo yes || echo no))" >&2; fail=1; fi

rm -f "$TMP/kills"; echo "garbage" > "$TMP/created"
got="$(_session_guard s 180)"
if [ "$got" = "running" ] && [ ! -f "$TMP/kills" ]; then
  echo "  OK : unreadable creation time -> treated as running, never killed blind"
else echo "  FAIL: unreadable age -> '$got'" >&2; fail=1; fi

echo ""
echo "── _return_to_main ──"
# A bare origin plus a clone left on the run's chore branch, as a timed-out
# 2026-10-11 run left it.
git init -q --bare "$TMP/origin.git"
git clone -q "$TMP/origin.git" "$TMP/work" 2>/dev/null
(
  cd "$TMP/work"
  git config user.email t@example.com; git config user.name t
  git checkout -q -b main
  echo one > f; git add f; git commit -q -m one; git push -q origin main
  git checkout -q -b chore/upgrade-2026-10-11
  echo two > f; git commit -q -am two
)
(cd "$TMP/work" && _return_to_main) >"$TMP/out" 2>&1 || true
branch="$(git -C "$TMP/work" rev-parse --abbrev-ref HEAD)"
if [ "$branch" = "main" ] && git -C "$TMP/origin.git" rev-parse -q --verify refs/heads/chore/upgrade-2026-10-11 >/dev/null; then
  echo "  OK : clean chore branch is pushed, then the checkout returns to main"
else echo "  FAIL: branch=$branch out=$(cat "$TMP/out")" >&2; fail=1; fi

(
  cd "$TMP/work"
  git checkout -q chore/upgrade-2026-10-11
  echo dirty > f
)
(cd "$TMP/work" && _return_to_main) >"$TMP/out" 2>&1 || true
branch="$(git -C "$TMP/work" rev-parse --abbrev-ref HEAD)"
if [ "$branch" = "chore/upgrade-2026-10-11" ] && grep -q 'dirty' "$TMP/work/f"; then
  echo "  OK : uncommitted work is never switched away from"
else echo "  FAIL: dirty tree -> branch=$branch" >&2; fail=1; fi

echo ""
echo "── wrapper ordering ──"
# The guard must run before the branch guard, or an overlapping fire FATALs
# on the live run's branch instead of skipping (the 05:00 failure).
# shellcheck disable=SC2016  # literal $SESSION is the text being searched for
guard_line="$(grep -n '_session_guard "\$SESSION"' "$SCRIPT" | head -1 | cut -d: -f1)"
branch_line="$(grep -n 'FATAL: repo checkout is on branch' "$SCRIPT" | head -1 | cut -d: -f1)"
if [ -n "$guard_line" ] && [ -n "$branch_line" ] && [ "$guard_line" -lt "$branch_line" ]; then
  echo "  OK : session guard (line $guard_line) runs before the branch guard (line $branch_line)"
else echo "  FAIL: session guard line=${guard_line:-none}, branch guard line=${branch_line:-none}" >&2; fail=1; fi

timeout_min="$(grep -oE '^WATCH_TIMEOUT_MIN=[0-9]+' "$SCRIPT" | cut -d= -f2)"
if [ -n "$timeout_min" ] && [ "$timeout_min" -le 175 ]; then
  echo "  OK : WATCH_TIMEOUT_MIN=${timeout_min} leaves the watcher done before the next 3-hourly fire"
else echo "  FAIL: WATCH_TIMEOUT_MIN=${timeout_min:-unset} — a timed-out run outlives the next fire" >&2; fail=1; fi

echo ""
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED" >&2; fi
exit "$fail"
