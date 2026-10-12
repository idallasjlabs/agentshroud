#!/usr/bin/env bash
# sunday-upgrade-approve.sh — the one human step the unattended Sunday
# upgrade cannot do for itself: merging its own reviewed branch to main.
#
# The upgrade run (scripts/sunday-upgrade.sh) is fully unattended through
# discovery, patching, rebuild, scan, test, and PR creation. It stops at the
# PR on purpose — merging without human review is a hard boundary, not a
# gap. This script is the fast path for the human half: it verifies CI is
# actually green (never trusts a stale or partial rollup), shows the real
# upgrade report so review is a read, not a hunt, and merges on one typed
# confirmation. No --yes bypass — same intentional shape as
# promote-firmware.sh.
#
# Usage:
#   scripts/sunday-upgrade-approve.sh [YYYY-MM-DD]
#   Defaults to today's date.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_SLUG="idallasjlabs/agentshroud"
DATE="${1:-$(date +%Y-%m-%d)}"
BRANCH="chore/upgrade-${DATE}"
REPORT="$REPO_DIR/reports/upgrade-${DATE}.md"

command -v gh >/dev/null 2>&1 || { echo "ERROR: gh CLI not found." >&2; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "ERROR: jq not found." >&2; exit 1; }

echo "==> Looking up open PR for branch $BRANCH"
PR_JSON="$(gh pr list --repo "$REPO_SLUG" --head "$BRANCH" --state open \
    --json number,title,url,mergeable,statusCheckRollup --jq '.[0]')"

if [ -z "$PR_JSON" ] || [ "$PR_JSON" = "null" ]; then
    echo "ERROR: no open PR found for branch $BRANCH." >&2
    echo "       Check with: gh pr list --repo $REPO_SLUG --head $BRANCH" >&2
    exit 1
fi

PR_NUM=$(echo "$PR_JSON" | jq -r '.number')
PR_URL=$(echo "$PR_JSON" | jq -r '.url')
PR_TITLE=$(echo "$PR_JSON" | jq -r '.title')
MERGEABLE=$(echo "$PR_JSON" | jq -r '.mergeable')

echo "    PR #$PR_NUM: $PR_TITLE"
echo "    $PR_URL"
echo ""

TOTAL=$(echo "$PR_JSON" | jq -r '.statusCheckRollup | length')
if [ "$TOTAL" -eq 0 ]; then
    echo "ERROR: PR #$PR_NUM has no CI checks reported yet. Refusing to offer merge." >&2
    exit 1
fi

FAILING=$(echo "$PR_JSON" | jq -r \
    '[.statusCheckRollup[] | select((.conclusion // .state) != "SUCCESS" and (.conclusion // .state) != "NEUTRAL" and (.conclusion // .state) != "SKIPPED")] | length')
if [ "$FAILING" -gt 0 ]; then
    echo "ERROR: PR #$PR_NUM has $FAILING non-green check(s) of $TOTAL. Refusing to offer merge." >&2
    echo "$PR_JSON" | jq -r '.statusCheckRollup[] | "  - \(.name // .context): \(.conclusion // .state)"' >&2
    exit 1
fi

if [ "$MERGEABLE" != "MERGEABLE" ]; then
    echo "ERROR: PR #$PR_NUM mergeable state is '$MERGEABLE' (conflicts with main?). Refusing to offer merge." >&2
    exit 1
fi

echo "    CI: $TOTAL/$TOTAL checks green. Mergeable: yes."
echo ""

if [ -f "$REPORT" ]; then
    echo "==> Report: $REPORT"
    echo "────────────────────────────────────────────────────────────"
    cat "$REPORT"
    echo "────────────────────────────────────────────────────────────"
else
    echo "WARNING: no report found at $REPORT — review the PR diff directly:" >&2
    echo "         gh pr diff $PR_NUM --repo $REPO_SLUG" >&2
fi

echo ""
echo "This will squash-merge PR #$PR_NUM (branch $BRANCH) into main and delete"
echo "the branch. There is no further review step after this."
echo ""
read -r -p "Type 'MERGE' to confirm: " CONFIRM
if [ "$CONFIRM" != "MERGE" ]; then
    echo "Aborted. Nothing was merged."
    exit 1
fi

echo "==> Merging PR #$PR_NUM..."
gh pr merge "$PR_NUM" --repo "$REPO_SLUG" --squash --delete-branch

ARTIFACT_DIR="$REPO_DIR/reports/sunday/${DATE}"
mkdir -p "$ARTIFACT_DIR"
MERGE_SHA="$(gh pr view "$PR_NUM" --repo "$REPO_SLUG" --json mergeCommit --jq '.mergeCommit.oid')"
if [ -n "$MERGE_SHA" ] && [ "$MERGE_SHA" != "null" ]; then
    echo "$MERGE_SHA" > "$ARTIFACT_DIR/merge-commit.txt"
else
    echo "WARNING: could not resolve the merge commit SHA — scripts/sunday-rollback.sh needs it in $ARTIFACT_DIR/merge-commit.txt" >&2
fi

echo ""
echo "==> Merged. main now includes this week's upgrade ($DATE)."
echo "    Backout if needed:"
echo "      - whole merge (revert + redeploy):  bash scripts/sunday-rollback.sh ${DATE}"
echo "      - dev images only:                  bash reports/sunday/${DATE}/rollback.sh"
