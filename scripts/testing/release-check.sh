#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# release-check.sh — release readiness evidence (i-release-gate gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="release-check"; T_SUMMARY="clean tree, branch, impact analysis, rollback plan and changelog evidence"
T_OPTIONS="  --base <ref>         base ref for the changelog check (default: main, origin/main)"
BASE=""
t_parse "base=BASE" "$@"; t_init

git rev-parse --git-dir >/dev/null 2>&1 || t_die "not a git repository: $T_REPO"
branch="$(git branch --show-current 2>/dev/null)"
if [ -z "$(git status --porcelain 2>/dev/null)" ]; then t_record clean-tree pass "working tree clean"; else t_record clean-tree fail "uncommitted changes present"; fi
if [ -n "$branch" ] && [ "$branch" != main ]; then t_record branch pass "on $branch"; else t_record branch fail "release work must be on a branch, not '${branch:-detached}'"; fi

safe="$(printf '%s' "$branch" | tr -c 'A-Za-z0-9._-' '-')"
art=".impact-analysis/${safe}.md"
if [ -f "$art" ] && /usr/bin/grep -q 'i-code-reviewer' "$art"; then
    t_record impact-analysis pass "$art has an i-code-reviewer section"
else
    t_record impact-analysis fail "missing $art or its i-code-reviewer section (run scripts/testing/impact-map.sh)"
fi
if [ -f "$art" ] && /usr/bin/grep -qi 'rollback' "$art"; then
    t_record rollback pass "rollback documented in $art"
elif [ -n "$(git ls-files '*ROLLBACK*' '*rollback*' 2>/dev/null | head -1)" ]; then
    t_record rollback pass "rollback document tracked in repo"
else
    t_record rollback fail "no rollback plan found (document it in $art)"
fi
if [ -f CHANGELOG.md ]; then
    if [ -z "$BASE" ]; then for c in main origin/main; do git rev-parse --verify -q "$c" >/dev/null 2>&1 && { BASE="$c"; break; }; done; fi
    if [ -n "$BASE" ] && git diff --name-only "$BASE"...HEAD 2>/dev/null | /usr/bin/grep -qx 'CHANGELOG.md'; then
        t_record changelog pass "CHANGELOG.md updated since $BASE"
    else
        t_record changelog fail "CHANGELOG.md not updated on this branch"
    fi
else
    t_skip changelog "no CHANGELOG.md"
fi
t_finish
