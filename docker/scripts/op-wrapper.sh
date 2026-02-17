#!/bin/bash
# Wrapper script for 1Password CLI that handles authentication
# Usage: op-wrapper.sh <op command arguments>

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=op-auth-common.sh
source "$SCRIPT_DIR/op-auth-common.sh"

if op_authenticate; then
    op --session "$OP_SESSION" "$@"
else
    echo "[ERROR] Failed to sign in to 1Password" >&2
    exit 1
fi
