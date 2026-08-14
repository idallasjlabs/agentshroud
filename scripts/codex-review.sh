#!/usr/bin/env bash
# codex-review.sh — OpenAI code review via REST API (bypasses Codex CLI WebSocket issues)
#
# Usage: codex-review.sh <diff_file> [model]
#
# Reads the OpenAI API key from ~/.codex/auth.json and calls the
# chat/completions REST API directly. This bypasses the Codex CLI's
# WebSocket connection which fails from certain networks.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™.

set -euo pipefail

DIFF_FILE="${1:?Usage: codex-review.sh <diff_file> [model]}"
MODEL="${2:-gpt-4o}"
MAX_CHARS=80000

if [ ! -f "$DIFF_FILE" ]; then
    echo "ERROR: File not found: $DIFF_FILE" >&2
    exit 1
fi

# Extract API key from Codex auth
AUTH_FILE="$HOME/.codex/auth.json"
if [ ! -f "$AUTH_FILE" ]; then
    echo "ERROR: No Codex auth file at $AUTH_FILE" >&2
    exit 1
fi

API_KEY=$(python3 -c "import json; print(json.load(open('$AUTH_FILE'))['OPENAI_API_KEY'])")
if [ -z "$API_KEY" ]; then
    echo "ERROR: Could not extract OPENAI_API_KEY from $AUTH_FILE" >&2
    exit 1
fi

# Truncate diff if too large
DIFF_CONTENT=$(head -c "$MAX_CHARS" "$DIFF_FILE")
DIFF_SIZE=$(wc -c < "$DIFF_FILE")

if [ "$DIFF_SIZE" -gt "$MAX_CHARS" ]; then
    echo "WARNING: Diff truncated from $DIFF_SIZE to $MAX_CHARS bytes" >&2
fi

# Escape for JSON
ESCAPED_DIFF=$(python3 -c "
import json, sys
with open('$DIFF_FILE', 'r', errors='replace') as f:
    content = f.read()[:$MAX_CHARS]
print(json.dumps(content))
")

# Call OpenAI REST API
RESPONSE=$(curl -s --max-time 120 \
    https://api.openai.com/v1/chat/completions \
    -H "Authorization: Bearer $API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
        \"model\": \"$MODEL\",
        \"messages\": [
            {\"role\": \"system\", \"content\": \"You are a senior security engineer reviewing code changes for an AI agent security platform (AgentShroud). Review the git diff for: 1) Security vulnerabilities, 2) Bugs, 3) Logic errors, 4) Missing error handling, 5) Performance issues. Be concise — numbered findings only.\"},
            {\"role\": \"user\", \"content\": $ESCAPED_DIFF}
        ],
        \"max_tokens\": 2000,
        \"temperature\": 0.1
    }")

# Extract the response text
echo "$RESPONSE" | python3 -c "
import json, sys
data = json.load(sys.stdin)
if 'choices' in data:
    print(data['choices'][0]['message']['content'])
elif 'error' in data:
    print(f\"ERROR: {data['error']['message']}\", file=sys.stderr)
    sys.exit(1)
else:
    print(json.dumps(data, indent=2))
"
