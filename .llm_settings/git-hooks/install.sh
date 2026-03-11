#!/bin/bash

# Install git hooks to current repository
# Usage: ./install.sh [--global]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOK_SOURCE="$SCRIPT_DIR/pre-commit"
GITLEAKS_CONFIG="$SCRIPT_DIR/gitleaks.toml"

if [ "$1" == "--global" ]; then
    # Set up global git template
    echo "📦 Setting up global git hooks template..."

    TEMPLATE_DIR="${GIT_TEMPLATE_DIR:-$HOME/.git-templates}"
    HOOKS_DIR="$TEMPLATE_DIR/hooks"

    mkdir -p "$HOOKS_DIR"
    cp "$HOOK_SOURCE" "$HOOKS_DIR/pre-commit"
    chmod +x "$HOOKS_DIR/pre-commit"

    # Note: gitleaks.toml cannot be placed in template (it goes to repo root)
    # It will be copied by llm-init.sh when deploying to repos

    git config --global init.templateDir "$TEMPLATE_DIR"

    echo "✅ Global template configured at $TEMPLATE_DIR"
    echo "   All NEW repos will automatically get hooks"
    echo "   Note: gitleaks.toml must be deployed per-repo (use llm-init.sh)"
    echo ""
    echo "To apply to existing repos, run:"
    echo "   cd <repo> && git init"
    
elif [ -d ".git" ]; then
    # Install to current repo
    echo "📦 Installing hooks to current repository..."

    cp "$HOOK_SOURCE" .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit

    # Copy gitleaks.toml to repo root if it exists
    if [ -f "$GITLEAKS_CONFIG" ]; then
        cp "$GITLEAKS_CONFIG" gitleaks.toml
        echo "✅ gitleaks.toml copied to repo root"
    fi

    echo "✅ Pre-commit hook installed to $(pwd)/.git/hooks/"
    
    # Optionally set up git-secrets
    if command -v git &> /dev/null && command -v git-secrets &> /dev/null; then
        read -p "Configure git-secrets for AWS patterns? [y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git secrets --install --force 2>/dev/null || true
            git secrets --register-aws
            echo "✅ git-secrets configured"
        fi
    fi
else
    echo "❌ Error: Not in a git repository"
    echo ""
    echo "Usage:"
    echo "  ./install.sh          # Install to current repo"
    echo "  ./install.sh --global # Set up global template for all new repos"
    exit 1
fi

echo ""
echo "🔍 Checking for required tools..."
if command -v gitleaks &>/dev/null; then
    echo "✅ gitleaks installed"
elif command -v brew &>/dev/null; then
    echo "⚠️  gitleaks missing: brew install gitleaks"
else
    echo "⚠️  gitleaks missing: https://github.com/gitleaks/gitleaks#installing"
fi
if command -v git-secrets &>/dev/null; then
    echo "✅ git-secrets installed"
elif command -v brew &>/dev/null; then
    echo "⚠️  git-secrets missing: brew install git-secrets"
else
    echo "⚠️  git-secrets missing: https://github.com/awslabs/git-secrets#installing-git-secrets"
fi
