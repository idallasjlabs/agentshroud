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
  'merge-commit.txt' \
  'dev-merge-commit-YYYY-MM-DD.txt'; do
  if grep -qF "$needle" "$PROMPT"; then pass "dev gate mentions: $needle"; else fail "dev gate missing: $needle"; fi
done

# 2b. Not all-or-nothing (owner directive 2026-10-18): an OPEN finding with no
# upstream fix must not block every other upgrade; only a regression does.
for needle in 'do not block' 'a regression blocks the merge' 'PARTIAL (n components failed/blocked)' 'promotes the components that passed'; do
  if grep -qF "$needle" "$PROMPT"; then pass "partial path mentions: $needle"; else fail "partial path missing: $needle"; fi
done
if grep -nF 'every finding is FIXED or ACCEPTED' "$PROMPT"; then
  fail "a merge/promote gate still requires every finding FIXED or ACCEPTED"
else
  pass "no all-findings-fixed gate"
fi

# 2c. Per-component report the owner asked for (2026-10-18): from -> to with
# security fixes / bug fixes / features, and a week plan for what did not update.
for needle in 'Per-component change report' '- Security fixes:' '- Bug fixes:' '- New features:' 'Not updated this run — plan for the week' '- Why:' '- Exposure left open:' '- Plan:'; do
  if grep -qF -- "$needle" "$PROMPT"; then pass "report mentions: $needle"; else fail "report missing: $needle"; fi
done

# 2d. 08:00 window (owner directive 2026-10-18).
for needle in 'everything is up and usable by 08:00 ET' 'After **07:00 ET** do not START the prod cutover' 'After **07:30 ET** start no new change' 'BLOCKED (08:00 window)'; do
  if grep -qF -- "$needle" "$PROMPT"; then pass "window mentions: $needle"; else fail "window missing: $needle"; fi
done

# 2e. Named inventory items (owner 2026-10-20): ClamAV ships from Debian, so
# "latest" must come from upstream releases, not apt; the Hermes image's
# critical findings are a tracked item, not a number in the scan table.
for needle in 'Cisco-Talos/clamav' 'not the Debian package' 'Hermes image critical findings'; do
  if grep -qF -- "$needle" "$PROMPT"; then pass "inventory names: $needle"; else fail "inventory missing: $needle"; fi
done

# 2f. Conduit plugin (owner 2026-10-22): conduit_push was hand-installed into
# Hermes's data volume, so no repo pin existed and Sunday never checked it
# (0.41.0 vs upstream 0.55.2). Upstream has no tags: "latest" is plugin.yaml.
for needle in 'conduit_push' 'kaishi00/hermes-conduit-notifier' 'plugin.yaml' 'update-conduit-push.sh' 'Status: enabled' 'Pulse stays off' 'accepted risk (owner 2026-10-22)' 'pinned to a reviewed commit SHA'; do
  if grep -qF -- "$needle" "$PROMPT"; then pass "inventory names: $needle"; else fail "inventory missing: $needle"; fi
done

# 3. The automatic prod-cutover gate names every condition and the rollback.
for needle in \
  'Gate the cutover automatically' \
  'sunday_dev_handoff_gate' \
  'git merge-base --is-ancestor' \
  'no file = dev never merged = stop' \
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
