#!/usr/bin/env bash
# ============================================================================
# peer-review.sh — Multi-Model Peer Review Workflow
# ============================================================================
# Usage: ./scripts/peer-review.sh [target]
#   target: "branch" (diff vs main), "staged" (git staged), "last" (last commit)
#   Default: branch
#
# Runs Gemini (API) and Codex peer reviews, saves findings to reviews/,
# then prints the command for Claude to read and fix.
# ============================================================================
set -euo pipefail

REPO_DIR="$HOME/Development/agentshroud"
REVIEWS_DIR="$REPO_DIR/reviews"
PYTHON="$HOME/miniforge3/envs/agentshroud/bin/python"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BRANCH=$(cd "$REPO_DIR" && git branch --show-current)
TARGET="${1:-branch}"

export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:$PATH"
[[ -f "$HOME/.llm_env" ]] && source "$HOME/.llm_env"
export GEMINI_API_KEY OPENAI_API_KEY 2>/dev/null || true

mkdir -p "$REVIEWS_DIR"
cd "$REPO_DIR"

echo "============================================================"
echo "  Multi-Model Peer Review"
echo "  Branch: $BRANCH"
echo "  Target: $TARGET"
echo "  Time:   $TIMESTAMP"
echo "============================================================"

# --- Generate diff ---
case "$TARGET" in
  branch)  DIFF=$(git diff main..HEAD 2>/dev/null || git diff HEAD~5..HEAD); DIFF_DESC="branch diff vs main" ;;
  staged)  DIFF=$(git diff --cached); DIFF_DESC="staged changes" ;;
  last)    DIFF=$(git diff HEAD~1..HEAD); DIFF_DESC="last commit" ;;
  *)       echo "Unknown target: $TARGET"; exit 1 ;;
esac

if [[ -z "$DIFF" ]]; then
  echo "No changes to review."
  exit 0
fi

LINES_CHANGED=$(echo "$DIFF" | grep -c '^[+-]' || true)
echo "Changes: $LINES_CHANGED lines ($DIFF_DESC)"
echo ""

# --- Gemini Review (lightweight Python API) ---
echo "🔵 Running Gemini review (API)..."
GEMINI_FILE="$REVIEWS_DIR/gemini-review-$TIMESTAMP.md"
{
  echo "# Gemini Peer Review"
  echo ""
  echo "**Branch:** $BRANCH"
  echo "**Date:** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "**Changes:** $LINES_CHANGED lines ($DIFF_DESC)"
  echo "**Model:** gemini-2.5-flash (API)"
  echo ""
  echo "---"
  echo ""
  echo "$DIFF" | ~/miniforge3/envs/agentshroud/bin/python scripts/gemini-review.py 2>/dev/null || echo "ERROR: Gemini review failed"
} > "$GEMINI_FILE"
echo "   ✅ Saved: $GEMINI_FILE"

# --- Codex Review ---
echo "🟢 Running Codex review..."
CODEX_FILE="$REVIEWS_DIR/codex-review-$TIMESTAMP.md"

REVIEW_PROMPT="You are a senior code reviewer for AgentShroud, a security proxy for OpenClaw AI agents.

Review the following code changes. Focus on:
1. Security: credential handling, injection, PII leaks, container security
2. Correctness: logic errors, edge cases, error handling
3. Testing: are changes tested? coverage gaps?
4. Style: naming, structure, readability
5. Performance: runs on Raspberry Pi 4 (ARM64, 8GB RAM)

For each finding: [SEVERITY] file:line — description, with suggested fix.
Severities: CRITICAL, HIGH, MEDIUM, LOW, INFO.

Branch: $BRANCH

\`\`\`diff
$DIFF
\`\`\`"

{
  echo "# Codex (OpenAI) Peer Review"
  echo ""
  echo "**Branch:** $BRANCH"
  echo "**Date:** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "**Changes:** $LINES_CHANGED lines ($DIFF_DESC)"
  echo "**Model:** o4-mini"
  echo ""
  echo "---"
  echo ""
  timeout 180 codex exec "$REVIEW_PROMPT" 2>/dev/null | grep -v "^OpenAI Codex\|^--------\|^workdir:\|^model:\|^provider:\|^approval:\|^sandbox:\|^reasoning\|^session id:\|^mcp:\|^deprecated:\|^tokens used\|^[0-9,]*$\|^user$\|^codex$\|^ERROR.*rollout\|^$" || echo "ERROR: Codex review failed or timed out"
} > "$CODEX_FILE"
echo "   ✅ Saved: $CODEX_FILE"

# --- Summary ---
echo ""
echo "============================================================"
echo "  ✅ Review Complete"
echo "============================================================"
echo ""
echo "  Gemini: $GEMINI_FILE"
echo "  Codex:  $CODEX_FILE"
echo ""
echo "  Next — have Claude fix the findings:"
echo ""
echo "  claude -p \"Read reviews/gemini-review-$TIMESTAMP.md and"
echo "  reviews/codex-review-$TIMESTAMP.md. List all findings by"
echo "  severity. Fix CRITICAL and HIGH items. Create a TODO list"
echo "  for MEDIUM and LOW. Run tests after fixes.\""
echo ""
echo "============================================================"
