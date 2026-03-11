#!/usr/bin/env bash
set -euo pipefail

# Reads JSON on stdin. Needs: jq (recommended).
# Claude Code provides: cwd, model.display_name, context_window.used_percentage, cost.total_cost_usd, version, etc.
# See docs for full schema.  [oai_citation:7‡Claude Code](https://code.claude.com/docs/en/statusline)

json="$(cat)"

cwd="$(jq -r '.cwd // .workspace.current_dir // empty' <<<"$json")"
model="$(jq -r '.model.display_name // .model.id // "?"' <<<"$json")"
used_pct="$(jq -r '.context_window.used_percentage // empty' <<<"$json")"
cost="$(jq -r '.cost.total_cost_usd // empty' <<<"$json")"

# Git info (best-effort)
git_branch=""
git_dirty=""
if [ -n "${cwd:-}" ] && git -C "$cwd" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git_branch="$(git -C "$cwd" branch --show-current 2>/dev/null || true)"
  if ! git -C "$cwd" diff --quiet --ignore-submodules -- 2>/dev/null; then
    git_dirty="*"
  fi
fi

# Conda env (best-effort)
conda_env="${CONDA_DEFAULT_ENV:-}"
if [ -n "${conda_env}" ]; then
  conda_env="conda:${conda_env}"
fi

# Directory (short)
dir="${cwd##*/}"

# Build line (keep it compact)
# ANSI colors are supported.  [oai_citation:8‡Claude Code](https://code.claude.com/docs/en/statusline)
line=""
[ -n "$git_branch" ] && line+=" ${git_branch}${git_dirty} "
[ -n "$conda_env" ] && line+="${conda_env} "
line+="| ${dir} "
line+="| ${model} "
[ -n "$used_pct" ] && line+="| ctx:${used_pct}% "
[ -n "$cost" ] && line+="| $:${cost}"

echo "$line"
