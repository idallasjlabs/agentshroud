#!/usr/bin/env bash
# Behavioral test for sunday-upgrade-apply.sh's _record_head/_assert_head_unchanged
# guard, extended 2026-10-04 to re-check on every iteration of phase_apply's
# per-service build loop, not just once before it starts.
#
# Root cause this guards against: a Sunday run's sequential multi-service build
# loop has several minutes BETWEEN services. On 2026-10-04 a second session ran
# `git checkout main` on the same shared working tree between the gateway and
# openclaw builds of the same run -- gateway baked one commit's code, openclaw
# baked a different one, and the run's own PASS result did not notice. The
# original guard only asserted once, before the loop; this test proves the
# extracted guard functions themselves behave correctly under the per-iteration
# calling pattern the fix adds (real execution, not a grep for the fix text).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SCRIPT="$REPO_ROOT/scripts/sunday-upgrade-apply.sh"
fail=0

# Extract ONLY the _record_head/_assert_head_unchanged function definitions
# (the real text in the real script -- not reimplemented here, so this test
# would fail if the real functions' logic changed) rather than sourcing the
# whole script, whose top-level code parses argv and calls `die` on anything
# it doesn't recognise. Uses grep/sed line-number arithmetic rather than an
# awk range/exit pattern: some awk implementations (observed here) buffer
# stdout and drop it on `exit` when piped/captured rather than to a tty,
# which silently produced an empty extraction during development of this
# test -- line numbers avoid that class of bug entirely.
_start_line="$(grep -n '^_record_head() {$' "$SCRIPT" | head -1 | cut -d: -f1)"
_assert_start_line="$(grep -n '^_assert_head_unchanged() {$' "$SCRIPT" | head -1 | cut -d: -f1)"
if [ -z "$_start_line" ] || [ -z "$_assert_start_line" ]; then
  echo "  FAIL: could not locate _record_head/_assert_head_unchanged in $SCRIPT" >&2
  exit 1
fi
_assert_close_offset="$(tail -n "+${_assert_start_line}" "$SCRIPT" | grep -n '^}$' | head -1 | cut -d: -f1)"
_end_line="$((_assert_start_line + _assert_close_offset - 1))"
EXTRACTED="$(sed -n "${_start_line},${_end_line}p" "$SCRIPT")"
if [ -z "$EXTRACTED" ]; then
  echo "  FAIL: extracted empty body for _record_head/_assert_head_unchanged from $SCRIPT" >&2
  exit 1
fi

# Minimal stubs for the logging helpers the real functions call.
log() { :; }
err() { printf '%s\n' "$*" >&2; }

eval "$EXTRACTED"

TMP_REPO="$(mktemp -d)"
cleanup() { rm -rf "$TMP_REPO"; }
trap cleanup EXIT

(
  cd "$TMP_REPO"
  git init -q
  git config user.email test@example.com
  git config user.name test
  echo one > f.txt
  git add f.txt
  git commit -q -m one
)
REPO="$TMP_REPO"

echo ""
echo "── _assert_head_unchanged ──"

HEAD_AT_START=""
_record_head
if [ "$HEAD_AT_START" != "$(git -C "$REPO" rev-parse HEAD)" ]; then
  echo "  FAIL: _record_head did not capture the real HEAD" >&2
  fail=1
else
  echo "  OK : _record_head captures the real HEAD"
fi

if _assert_head_unchanged; then
  echo "  OK : returns success when HEAD has not moved"
else
  echo "  FAIL: returned failure when HEAD had not moved" >&2
  fail=1
fi

# Simulate the exact failure mode: another session checks out a different
# commit on the SAME shared working tree mid-run.
(
  cd "$TMP_REPO"
  echo two > f.txt
  git add f.txt
  git commit -q -m two
)

if _assert_head_unchanged 2>/tmp/head_guard_test_err.txt; then
  echo "  FAIL: did not detect HEAD moving mid-run" >&2
  fail=1
else
  echo "  OK : detects HEAD moving mid-run and returns failure"
fi
if grep -q "the working tree MOVED mid-run" /tmp/head_guard_test_err.txt 2>/dev/null; then
  echo "  OK : error message names the real failure, not a generic one"
else
  echo "  FAIL: error message missing or generic" >&2
  fail=1
fi
rm -f /tmp/head_guard_test_err.txt

# No baseline recorded (e.g. not a git repo at startup) must never invent a
# failure -- re-check the documented early-return.
HEAD_AT_START=""
if _assert_head_unchanged; then
  echo "  OK : no-baseline case returns success, not a false failure"
else
  echo "  FAIL: no-baseline case incorrectly failed" >&2
  fail=1
fi

echo ""
echo "── phase_apply calls the guard inside the per-service loop, not just before it ──"
# Static check for the actual wiring (the behavioral checks above prove the
# function works; this proves phase_apply's loop actually calls it on every
# iteration, which is the fix's real point -- the original single call
# before the loop is unchanged and insufficient on its own). Range pattern,
# not exit, for the same buffering reason as the extraction above.
loop_body="$(awk '/for svc in \$build_list; do/,/^  done$/' "$SCRIPT")"
assert_calls="$(printf '%s' "$loop_body" | grep -c "_assert_head_unchanged" || true)"
if [ "$assert_calls" -ge 1 ]; then
  echo "  OK : phase_apply's per-service build loop calls _assert_head_unchanged"
else
  echo "  FAIL: phase_apply's per-service build loop does not re-check HEAD" >&2
  fail=1
fi

echo ""
if [ "$fail" -eq 0 ]; then
  echo "ALL CHECKS PASSED"
else
  echo "SOME CHECKS FAILED" >&2
fi
exit "$fail"
