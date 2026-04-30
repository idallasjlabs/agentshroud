#!/bin/bash
# clean-env-quick-keep-local.sh
# Quick: Remove .env from git tracking and history, keep locally

set -e

echo "🧹 Stop tracking .env files (keep local copies)"
echo ""

# Must be in git repo
[ ! -d ".git" ] && echo "❌ Not a git repo" && exit 1

REPO=$(basename "$(pwd)")
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")

echo "📂 Repo: $REPO"
echo "🌿 Branch: $BRANCH"
echo ""

# Backup
BACKUP="../${REPO}-backup-$(date +%Y%m%d-%H%M%S)"
echo "📦 Backup: $BACKUP"
git clone . "$BACKUP" 2>/dev/null
echo ""

# Find and untrack .env files
echo "🔓 Removing .env files from git (keeping local)..."
git ls-files | grep -E '(^|/)\..env' | while read f; do
    [ -f "$f" ] && git rm --cached "$f" 2>/dev/null && echo "   Untracked: $f"
done
echo ""

# Add to .gitignore
if ! grep -q "^\.env$" .gitignore 2>/dev/null; then
    cat >> .gitignore << 'EOF'

# Environment files
.env
.env.*
.env-*
EOF
    git add .gitignore
    echo "✅ Updated .gitignore"
fi

# Commit
git commit -m "chore: Stop tracking .env files" 2>/dev/null || true

echo ""
echo "✅ Done! Local .env files preserved"
echo "   Push with: git push origin $BRANCH"
echo ""
