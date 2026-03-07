#!/bin/bash
# AgentShroud pre-commit hook — runs gitleaks on staged changes
# Install: cp scripts/pre-commit-hook.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

set -e

# Check if gitleaks is installed
if ! command -v gitleaks &> /dev/null; then
    echo "⚠️  gitleaks not found — skipping secret scan"
    echo "   Install: brew install gitleaks"
    exit 0
fi

echo "🔐 Running gitleaks on staged changes..."

# Scan only staged changes (not entire history)
gitleaks protect --staged --config gitleaks.toml --verbose

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ BLOCKED: Secrets detected in staged files!"
    echo ""
    echo "Options:"
    echo "  1. Remove the secret and use env vars / 1Password instead"
    echo "  2. Add a false positive to gitleaks.toml [allowlist]"
    echo "  3. Skip this check (NOT recommended): git commit --no-verify"
    echo ""
    exit 1
fi

echo "✅ No secrets found — commit allowed"
