#!/bin/bash
# quick-setup.sh
# Quick security setup for a repository (runs all security scripts)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Quick Security Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Run security audit first
echo "Step 1: Security Audit"
"$SCRIPT_DIR/security-audit.sh"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Set up direnv
read -p "Set up direnv for environment variables? [Y/n] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    echo ""
    echo "Step 2: direnv Setup"
    "$SCRIPT_DIR/setup-direnv.sh"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Set up pgpass
read -p "Set up PostgreSQL password file? [Y/n] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    echo ""
    echo "Step 3: PostgreSQL Password Setup"
    "$SCRIPT_DIR/setup-pgpass.sh"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Quick security setup complete!"
echo ""
echo "📝 Manual steps remaining:"
echo "   1. Copy .envrc.example to .envrc and customize"
echo "   2. Add PostgreSQL entries to ~/.pgpass"
echo "   3. Test git hooks: echo 'password=test' > test.txt && git add test.txt"
echo ""

