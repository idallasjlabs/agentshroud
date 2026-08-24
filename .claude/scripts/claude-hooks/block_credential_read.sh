#!/usr/bin/env bash
# block_secret_read.sh — PreToolUse hook (BashTool)
#
# Blocks shell read commands (cat, head, tail, grep, etc.) from reading
# secret files. When a secret needs to be inspected, give the user the
# retrieval command to run locally — never echo the value into the transcript.
#
# Exit 0  = allow
# Exit 2  = block

set -euo pipefail

cmd="${CLAUDE_TOOL_INPUT:-}"

# Only trigger on commands that can print file contents
if ! [[ "$cmd" =~ (^|[[:space:];|&])(cat|head|tail|less|more|grep|awk|sed|xxd|od|strings|base64|printf|echo)[[:space:]] ]]; then
    exit 0
fi

# Secret path patterns to protect
deny_patterns=(
    "docker/secrets/"
    "\.agentshroud/secrets/"
    "/run/secrets/"
    "history\.env"
    "(^|[[:space:]\"'/])\.env([[:space:]\"'$]|\.)"
)

for pattern in "${deny_patterns[@]}"; do
    if [[ "$cmd" =~ $pattern ]]; then
        cat >&2 <<BLOCKED
BLOCKED by block_secret_read.sh:

  Do NOT read secret files into the transcript. Give the user the
  retrieval command to run locally instead:

    # To copy the value to clipboard:
    tail -1 ~/.agentshroud/secrets/<name>.txt | pbcopy   # macOS
    tail -1 ~/.agentshroud/secrets/<name>.txt | xclip    # Linux

    # To inspect without clipboard:
    wc -c ~/.agentshroud/secrets/<name>.txt              # check length only

  Matched pattern: $pattern
BLOCKED
        exit 2
    fi
done

exit 0
