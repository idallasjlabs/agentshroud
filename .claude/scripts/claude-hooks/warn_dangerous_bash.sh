#!/usr/bin/env bash
set -euo pipefail

cmd="${CLAUDE_TOOL_INPUT:-}"

dangerous_patterns=(
  "rm -rf /"
  "rm -rf ~"
  "rm -rf \*"
  "curl .*\|.*sh"
  "wget .*\|.*sh"
  "chmod -R 777"
  "dd if="
  ":(){ :|:& };:"
  "eval \"\$("
  "sudo rm"
  "mkfs"
  "> /dev/sd"
  "> /dev/nvme"
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
