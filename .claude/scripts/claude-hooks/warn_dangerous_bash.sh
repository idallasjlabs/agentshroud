#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
set -euo pipefail

cmd="${CLAUDE_TOOL_INPUT:-}"

# Patterns we want to WARN about (not block)
dangerous_patterns=(
  "rm -rf /"
  "rm -rf ~"
  "rm -rf \\*"
  "curl .*\\|.*sh"
  "wget .*\\|.*sh"
  "chmod -R 777"
  "dd if="
  ":(){ :|:& };:"   # fork bomb
)

for pattern in "${dangerous_patterns[@]}"; do
  if [[ "$cmd" =~ $pattern ]]; then
    echo "⚠️  WARNING: Potentially dangerous command detected:"
    echo "    $cmd"
    echo ""
    echo "Confirm intent before proceeding. Prefer safer alternatives."
    exit 0
  fi
done
