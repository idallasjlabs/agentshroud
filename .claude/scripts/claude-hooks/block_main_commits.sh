#!/usr/bin/env bash
# block_main_commits.sh — PreToolUse hook (BashTool)
#
# Blocks mutating git commands (commit, push, merge, rebase --onto main)
# when the working directory's current branch is 'main'.
#
# Exit 0  = allow
# Exit 2  = block (Claude Code interprets this as "do not execute the tool")
#
# Override: CLAUDE_ALLOW_MAIN=1 git ...  (for emergency hotfixes only)

set -euo pipefail

cmd="${CLAUDE_TOOL_INPUT:-}"

# Fast-exit for non-git commands
[[ "$cmd" =~ ^[[:space:]]*git[[:space:]] ]] || exit 0

# Only care about state-mutating operations
[[ "$cmd" =~ (commit|push[[:space:]]|merge[[:space:]]|rebase[[:space:]]--onto[[:space:]]main) ]] || exit 0

# Determine current branch
branch=$(git -C "$(pwd)" branch --show-current 2>/dev/null || echo "")

if [[ "$branch" == "main" ]]; then
    if [[ "${CLAUDE_ALLOW_MAIN:-}" == "1" ]]; then
        echo "WARNING: CLAUDE_ALLOW_MAIN=1 override active — proceeding on main (emergency only)."
        exit 0
    fi
    cat >&2 <<'BLOCKED'
BLOCKED by block_main_commits.sh:

  Current branch is 'main'. All changes must go through a feature branch + PR.

  Create a branch first:
    git checkout -b chore/v1.0.<NEXT>-<slug>
    (where NEXT = last bumped version + 1, e.g. v1.0.40)

  Compute next version:
    git log --oneline --grep='bump version to v' -1 \
      | grep -oE 'v1\.0\.[0-9]+' \
      | awk -F. '{print "v1.0."($3+1)}'

  Emergency override (dangerous):
    CLAUDE_ALLOW_MAIN=1 git ...
BLOCKED
    exit 2
fi

exit 0
