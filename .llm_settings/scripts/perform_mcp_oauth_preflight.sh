#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/mcp_oauth_preflight.py" reachability \
  --url https://login.microsoftonline.com \
  --url https://github.com/login \
  --url https://api.github.com \
  --url https://mcp.atlassian.com/v1/mcp
