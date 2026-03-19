#!/usr/bin/env bash
set -euo pipefail

# claude_repo_setup.sh
# - Adds team-shareable Claude Code config files to git staging
# - Adds local-only + secrets/caches to .gitignore
# - Safe to run multiple times (idempotent where possible)

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "${repo_root}" ]]; then
  echo "ERROR: Not inside a git repository."
  exit 1
fi
cd "$repo_root"

echo "Repo: $repo_root"

# -------------------------------------------------------------------
# 1) Ensure expected directories exist (no content created)
# -------------------------------------------------------------------
mkdir -p .claude/agents .claude/skills

# -------------------------------------------------------------------
# 2) Ensure .gitignore exists
# -------------------------------------------------------------------
touch .gitignore

# -------------------------------------------------------------------
# 3) Append ignore rules (idempotent)
# -------------------------------------------------------------------
append_ignore_line() {
  local line="$1"
  if ! grep -qxF "$line" .gitignore; then
    echo "$line" >> .gitignore
  fi
}

echo "Updating .gitignore…"

# Claude local overrides
append_ignore_line ""
append_ignore_line "# Claude Code (local overrides / caches)"
append_ignore_line ".claude/settings.local.json"
append_ignore_line ".claude/settings.local.*.json"
append_ignore_line ".claude/cache/"
append_ignore_line ".claude/tmp/"
append_ignore_line ".claude/logs/"

# Common secrets files (prevent accidental commits)
append_ignore_line ""
append_ignore_line "# Secrets / tokens (never commit)"
append_ignore_line ".env"
append_ignore_line ".env.*"
append_ignore_line "*.pem"
append_ignore_line "*.key"
append_ignore_line "*_token"
append_ignore_line "*_tokens"
append_ignore_line "*token*"
append_ignore_line "*secret*"
append_ignore_line "*cookie*"
append_ignore_line "*cookies*"

# Misc tool caches that sometimes contain auth artifacts
append_ignore_line ""
append_ignore_line "# Tool caches that may contain credentials"
append_ignore_line ".aws/"
append_ignore_line ".npmrc"
append_ignore_line ".yarnrc"
append_ignore_line ".pnpm-store/"
append_ignore_line "node_modules/"
append_ignore_line ".pytest_cache/"
append_ignore_line ".mypy_cache/"
append_ignore_line ".ruff_cache/"
append_ignore_line "__pycache__/"
append_ignore_line "*.pyc"

# -------------------------------------------------------------------
# 4) Stage the files we DO want committed (if they exist)
# -------------------------------------------------------------------
echo "Staging team-shareable Claude Code files (if present)…"

stage_if_exists() {
  local path="$1"
  if [[ -e "$path" ]]; then
    git add "$path"
    echo "  ✓ staged: $path"
  else
    echo "  - missing (not staged): $path"
  fi
}

stage_if_exists "CLAUDE.md"
stage_if_exists ".claude/settings.json"
stage_if_exists ".claude/agents"
stage_if_exists ".claude/skills"
stage_if_exists ".claude/scripts"
stage_if_exists ".mcp.json"
stage_if_exists ".gitignore"

# -------------------------------------------------------------------
# 5) Summary
# -------------------------------------------------------------------
echo ""
echo "Done."
echo ""
echo "Next steps:"
echo "  1) Review staged changes:   git status"
echo "  2) Review diff:             git diff --cached"
echo "  3) Commit:                  git commit -m \"Add Claude Code repo configuration\""
