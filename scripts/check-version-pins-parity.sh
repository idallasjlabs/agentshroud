#!/usr/bin/env bash
# scripts/check-version-pins-parity.sh — Dev/prod artifact-parity gate
#
# "It passed in dev" only means anything if prod is about to build the exact
# same artifact dev actually tested. Dev and prod are separate checkouts
# (separate macOS accounts, separate Colima VMs) that each pull independently
# from origin — there is no automated check that a prod rebuild is using the
# same docker/versions.env pins dev just verified, versus a stale checkout,
# a local-only override, or a checkout that's behind/diverged from what
# actually merged. Found live 2026-09-18: a Hermes log referenced a module
# path (hermes_plugins.telegram_platform.adapter) that does not exist
# anywhere in dev's currently-running Hermes container, which is exactly the
# failure mode this check exists to catch early instead of discovering it
# mid-investigation.
#
# This is intentionally a LOCAL check: each environment runs it against its
# own checkout, comparing "what I'm about to build" against "what origin/main
# says should be built" — not a live cross-session diff (dev cannot reach
# prod's checkout directly, and must not — see CLAUDE.md's coordination
# model). Run this in BOTH environments before a promotion; if either one
# fails, the checkouts have diverged and promoting would not actually test
# what ships.
#
# Usage:
#   bash scripts/check-version-pins-parity.sh
#
# Exit codes:
#   0 — local checkout's docker/versions.env matches origin/main exactly,
#       and HEAD is origin/main (or a strict ancestor with no local-only commits)
#   1 — mismatch: pins differ, or checkout has diverged/has unpushed local commits
#   2 — could not determine (no git repo, no network, origin/main unreachable)

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
    echo "  [version-parity] UNKNOWN: not a git repository" >&2
    exit 2
fi

if ! git fetch origin main --quiet 2>/dev/null; then
    echo "  [version-parity] UNKNOWN: could not fetch origin/main" >&2
    exit 2
fi

local_head=$(git rev-parse HEAD)
origin_main=$(git rev-parse origin/main)

fail=0

if [[ "$local_head" != "$origin_main" ]]; then
    if git merge-base --is-ancestor "$local_head" "$origin_main" 2>/dev/null; then
        echo "  [version-parity] FAIL: local HEAD ($local_head) is behind origin/main ($origin_main) — checkout is stale, pull before promoting" >&2
    elif git merge-base --is-ancestor "$origin_main" "$local_head" 2>/dev/null; then
        echo "  [version-parity] FAIL: local HEAD ($local_head) has unpushed/unmerged commits ahead of origin/main ($origin_main) — prod would build something dev's own PR process never reviewed" >&2
    else
        echo "  [version-parity] FAIL: local HEAD ($local_head) has DIVERGED from origin/main ($origin_main) — not a simple ahead/behind, needs manual reconciliation" >&2
    fi
    fail=1
fi

local_versions=$(cat docker/versions.env 2>/dev/null || echo "")
origin_versions=$(git show origin/main:docker/versions.env 2>/dev/null || echo "")

if [[ -z "$local_versions" || -z "$origin_versions" ]]; then
    echo "  [version-parity] UNKNOWN: could not read docker/versions.env locally or from origin/main" >&2
    exit 2
fi

if [[ "$local_versions" != "$origin_versions" ]]; then
    echo "  [version-parity] FAIL: docker/versions.env differs from origin/main's copy:" >&2
    diff <(echo "$origin_versions") <(echo "$local_versions") | head -20 >&2 || true
    fail=1
fi

if [[ "$fail" -eq 1 ]]; then
    exit 1
fi

echo "  [version-parity] PASS: checkout is exactly origin/main ($local_head), docker/versions.env matches"
exit 0
