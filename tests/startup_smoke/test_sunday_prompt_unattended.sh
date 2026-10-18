#!/usr/bin/env bash
# Static guard: the Sunday upgrade prompt must run end to end with nobody
# watching. Owner decision 2026-10-18: the automatic gates in §3 step 5 and
# §4 step 0b replace the two human taps. A prompt that asks the owner anything
# parks the run at PENDING APPROVAL, which is the failure this test prevents.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PROMPT="$REPO/prompts/sunday-upgrade.md"
fails=0
pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; fails=$((fails + 1)); }

[ -f "$PROMPT" ] || { echo "FAIL: $PROMPT missing"; exit 1; }

# 1. No instruction to ask the human, in any form.
# "do not call AskUserQuestion" is the instruction we want; any other call is not.
if grep -nE 'call (\*\*)?AskUserQuestion' "$PROMPT" | grep -vE 'not call (\*\*)?AskUserQuestion'; then
  fail "prompt still instructs AskUserQuestion"
else
  pass "no AskUserQuestion instruction"
fi
if grep -nE 'PENDING APPROVAL|awaiting tap|gate the merge on a human tap|Gate the cutover on a human tap' "$PROMPT"; then
  fail "prompt still has a human-tap / PENDING APPROVAL path"
else
  pass "no PENDING APPROVAL / human-tap path"
fi

# 2. The automatic dev-merge gate names every condition.
for needle in \
  'merge it automatically when every gate below holds' \
  'scan.images_scanned > 0' \
  'scan.scans_failed == 0' \
  'check-soak-status.sh' \
  'gh pr merge --squash --delete-branch' \
  'merge-commit.txt'; do
  if grep -qF "$needle" "$PROMPT"; then pass "dev gate mentions: $needle"; else fail "dev gate missing: $needle"; fi
done

# 3. The automatic prod-cutover gate names every condition and the rollback.
for needle in \
  'Gate the cutover automatically' \
  'sunday_dev_handoff_gate' \
  'git merge-base --is-ancestor' \
  'check-version-pins-parity.sh' \
  'BLOCKED (<gate>)' \
  'ROLLED BACK'; do
  if grep -qF "$needle" "$PROMPT"; then pass "prod gate mentions: $needle"; else fail "prod gate missing: $needle"; fi
done

# 4. The gate the prompt names must exist in the scripts it runs.
if grep -q 'sunday_dev_handoff_gate' "$REPO/scripts/lib/sunday-scan.sh"; then
  pass "sunday_dev_handoff_gate defined in scripts/lib/sunday-scan.sh"
else
  fail "sunday_dev_handoff_gate not defined in scripts/lib/sunday-scan.sh"
fi

echo "Results: $fails failure(s)"
[ "$fails" -eq 0 ]
