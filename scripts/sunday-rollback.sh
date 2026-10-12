#!/usr/bin/env bash
# sunday-rollback.sh — the one-line backout for a merged Sunday upgrade.
#
# Reverts the week's merge commit on main (so the pins go back to what they
# were before the run) and redeploys dev's previous pinned images using the
# fast local-retag path the run already captured, instead of a full rebuild.
#
# This does not touch prod — prod has its own rollback (§4.4 of
# prompts/sunday-upgrade.md), triggered automatically on a failed health
# check, using reports/sunday/<date>/rollback.sh scoped to prod's own
# baseline. Run that one directly if only prod needs to come back, not this.
#
# Usage:
#   scripts/sunday-rollback.sh YYYY-MM-DD

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE="${1:?Usage: scripts/sunday-rollback.sh YYYY-MM-DD}"
ARTIFACT_DIR="$REPO_DIR/reports/sunday/${DATE}"
MERGE_SHA_FILE="$ARTIFACT_DIR/merge-commit.txt"
IMAGE_ROLLBACK="$ARTIFACT_DIR/rollback.sh"

if [ ! -f "$MERGE_SHA_FILE" ]; then
    echo "ERROR: no merge commit recorded for $DATE at $MERGE_SHA_FILE." >&2
    echo "       Either that date's PR was never merged via sunday-upgrade-approve.sh," >&2
    echo "       or this is the wrong date. Check: gh pr list --state merged --search 'chore/upgrade-${DATE}'" >&2
    exit 1
fi
MERGE_SHA="$(cat "$MERGE_SHA_FILE")"

echo "==> Reverting merge commit $MERGE_SHA on main (upgrade $DATE)"
git -C "$REPO_DIR" fetch origin main
git -C "$REPO_DIR" checkout main
git -C "$REPO_DIR" pull --ff-only origin main
git -C "$REPO_DIR" revert --no-edit "$MERGE_SHA"
git -C "$REPO_DIR" push origin main
echo "    main reverted and pushed."

if [ -f "$IMAGE_ROLLBACK" ]; then
    echo "==> Redeploying dev's previous pinned images via $IMAGE_ROLLBACK"
    bash "$IMAGE_ROLLBACK"
else
    echo "WARNING: no image rollback script at $IMAGE_ROLLBACK." >&2
    echo "         Pins are reverted on main, but containers need a manual" >&2
    echo "         'docker compose pull && docker compose up -d' to catch up." >&2
fi

echo ""
echo "==> Rollback complete for $DATE."
