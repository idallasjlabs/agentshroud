#!/usr/bin/env bash
# .claude/scripts/claude-hooks/block_credential_write.sh
#
# PreToolUse hook for EditTool and WriteTool.
# Scans the content being written for high-entropy strings matching common
# credential patterns. Blocks the tool call with exit 2 if a match is found.
#
# Patterns are derived from .semgrep.yml (CWE-798) and common credential formats
# seen in this repo.
#
# Override: CLAUDE_ALLOW_CREDENTIAL_WRITE=1 (emergency use only — documented action required)

set -euo pipefail

# The content to be written is passed as the CLAUDE_TOOL_INPUT_FILE env var
# (a temp file), or as a JSON fragment via CLAUDE_TOOL_INPUT.
# Parse from CLAUDE_TOOL_INPUT (JSON string) via the new_string / content field.
input="${CLAUDE_TOOL_INPUT:-}"

# If no input, nothing to scan
[[ -z "$input" ]] && exit 0

# Override escape hatch
if [[ "${CLAUDE_ALLOW_CREDENTIAL_WRITE:-}" == "1" ]]; then
    echo "[block_credential_write] CLAUDE_ALLOW_CREDENTIAL_WRITE=1 override active — proceeding"
    exit 0
fi

# Secret patterns to detect in written content
# Ordered from most specific to most general
declare -a PATTERNS=(
    # Slack tokens
    "xoxb-[0-9A-Za-z-]+"
    "xapp-[0-9A-Za-z-]+"
    # GitHub tokens
    "ghp_[0-9A-Za-z]{36}"
    "github_pat_[0-9A-Za-z_]+"
    # OpenAI / Anthropic keys
    "sk-[A-Za-z0-9]{20,}"
    "sk-ant-[A-Za-z0-9-]+"
    # AWS access keys
    "AKIA[0-9A-Z]{16}"
    "ASIA[0-9A-Z]{16}"
    # 1Password / secret manager references that contain the value inline
    # (op:// refs are OK — they're pointers, not values)
    # JWT (three base64url segments separated by dots)
    "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
    # Telegram bot tokens (digits:alphanum, 45+ chars)
    "[0-9]{8,12}:[A-Za-z0-9_-]{35,}"
    # 40-character hex strings (common secret/key format)
    "[0-9a-f]{40}"
    "[0-9A-F]{40}"
)

for pattern in "${PATTERNS[@]}"; do
    if echo "$input" | grep -qE "$pattern" 2>/dev/null; then
        echo ""
        echo "BLOCKED [block_credential_write]: potential secret detected in written content."
        echo "  Matched pattern: $pattern"
        echo ""
        echo "  Rule R2 — Never write secret values into source files."
        echo "  Use environment variables, Docker secrets, or op:// references instead."
        echo ""
        echo "  If this is a test fixture (fake token for unit tests):"
        echo "    Use an obviously-fake value like 'xoxb-test-123' that does NOT"
        echo "    match the length/entropy of a real token, or set:"
        echo "    CLAUDE_ALLOW_CREDENTIAL_WRITE=1 (document why in the commit message)"
        echo ""
        exit 2
    fi
done

exit 0
