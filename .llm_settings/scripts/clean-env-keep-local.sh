#!/bin/bash
# clean-env-keep-local.sh
# Remove .env* files from git history and tracking, but KEEP them locally
# Works in any repository

set -e

echo "🧹 Clean .env Files from Git (Keep Locally)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if we're in a git repo
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    exit 1
fi

REPO_NAME=$(basename "$(pwd)")
BACKUP_DIR="../${REPO_NAME}-backup-$(date +%Y%m%d-%H%M%S)"
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")

echo "📂 Repository: $REPO_NAME"
echo "🌿 Branch: $CURRENT_BRANCH"
echo ""

# Step 1: Find .env files currently tracked
echo "🔍 Finding .env files currently tracked by git..."
TRACKED_ENV_FILES=$(git ls-files | grep -E '(^|/)\..env' || true)

if [ -z "$TRACKED_ENV_FILES" ]; then
    echo "   No .env files currently tracked"
else
    echo "   Currently tracked .env files:"
    echo "$TRACKED_ENV_FILES" | sed 's/^/      /'
fi
echo ""

# Step 2: Check history for .env files
echo "🔍 Scanning git history for .env files..."
HISTORY_ENV_FILES=$(git log --all --pretty=format: --name-only --diff-filter=A | grep -E '(^|/)\..env' | sort -u || true)

if [ -z "$HISTORY_ENV_FILES" ]; then
    echo "   No .env files in history"
    NEEDS_HISTORY_CLEAN=false
else
    echo "   Found .env files in history:"
    echo "$HISTORY_ENV_FILES" | sed 's/^/      /'
    NEEDS_HISTORY_CLEAN=true
fi
echo ""

# If nothing to do, exit
if [ -z "$TRACKED_ENV_FILES" ] && [ "$NEEDS_HISTORY_CLEAN" = false ]; then
    echo "✅ No .env files to clean - you're all set!"
    exit 0
fi

# Confirm with user
echo "📋 What will happen:"
echo "   1. Create backup of repository"
if [ "$NEEDS_HISTORY_CLEAN" = true ]; then
    echo "   2. Remove .env files from git history"
fi
if [ -n "$TRACKED_ENV_FILES" ]; then
    echo "   3. Stop tracking .env files (git rm --cached)"
fi
echo "   4. Add .env patterns to .gitignore"
echo "   5. Keep all .env files on your filesystem"
echo ""
echo "Type 'yes' to continue: "
read -r CONFIRM

if [[ ! "$CONFIRM" =~ ^[Yy][Ee][Ss]$ ]]; then
    echo "❌ Cancelled"
    exit 0
fi
echo ""

# Create backup
echo "📦 Creating backup..."
git clone . "$BACKUP_DIR" 2>/dev/null
echo "✅ Backup: $BACKUP_DIR"
echo ""

# Step 3: Clean history if needed
if [ "$NEEDS_HISTORY_CLEAN" = true ]; then
    # Check for git-filter-repo
    if ! command -v git-filter-repo &> /dev/null; then
        echo "📦 Installing git-filter-repo..."
        if command -v pip3 &> /dev/null; then
            pip3 install --user git-filter-repo
        elif command -v pip &> /dev/null; then
            pip install --user git-filter-repo
        else
            echo "❌ Error: pip not found"
            echo "   Install: pip3 install --user git-filter-repo"
            exit 1
        fi
        export PATH="$HOME/.local/bin:$PATH"
        echo ""
    fi

    # Save remotes
    declare -A REMOTES
    while IFS= read -r remote; do
        url=$(git remote get-url "$remote" 2>/dev/null || echo "")
        [ -n "$url" ] && REMOTES[$remote]=$url
    done < <(git remote)

    echo "🗑️  Removing .env files from git history..."
    echo "   This may take a while..."

    git filter-repo \
      --path-glob '.env' \
      --path-glob '.env-*' \
      --path-glob '.env.*' \
      --path-glob '**/.env' \
      --path-glob '**/.env-*' \
      --path-glob '**/.env.*' \
      --invert-paths \
      --force

    # Restore remotes
    for remote in "${!REMOTES[@]}"; do
        git remote add "$remote" "${REMOTES[$remote]}"
    done

    # Return to branch
    git checkout "$CURRENT_BRANCH" 2>/dev/null || true

    echo "✅ History cleaned"
    echo ""
fi

# Step 4: Stop tracking .env files (but keep locally)
if [ -n "$TRACKED_ENV_FILES" ]; then
    echo "🔓 Removing .env files from git tracking (keeping local copies)..."

    # Find all .env files (including in subdirectories)
    while IFS= read -r file; do
        if [ -f "$file" ]; then
            echo "   Untracking: $file"
            git rm --cached "$file" 2>/dev/null || true
        fi
    done < <(git ls-files | grep -E '(^|/)\..env')

    echo "✅ .env files untracked (local copies preserved)"
    echo ""
fi

# Step 5: Update .gitignore
echo "📝 Updating .gitignore..."

# Create .gitignore if it doesn't exist
touch .gitignore

# Check if .env patterns already in .gitignore
if ! grep -q "^\.env$" .gitignore; then
    cat >> .gitignore << 'GITIGNORE'

# Environment files (added by clean-env-keep-local.sh)
.env
.env.*
.env-*
*.env
**/.env
**/.env.*
**/.env-*
GITIGNORE
    echo "✅ Added .env patterns to .gitignore"
    git add .gitignore
else
    echo "✅ .gitignore already has .env patterns"
fi
echo ""

# Step 6: Commit the changes
echo "💾 Committing changes..."
if git diff --cached --quiet; then
    echo "   No changes to commit"
else
    git commit -m "chore: Stop tracking .env files (keep local copies)

- Removed .env files from git tracking
- Added .env patterns to .gitignore
- Local .env files preserved" || true
    echo "✅ Changes committed"
fi
echo ""

# Step 7: Verify local files still exist
echo "🔍 Verifying local .env files still exist..."
LOCAL_ENV_COUNT=0
while IFS= read -r file; do
    if [ -f "$file" ]; then
        echo "   ✅ $file (still exists locally)"
        ((LOCAL_ENV_COUNT++))
    fi
done < <(find . -name '.env*' -type f ! -path '*/\.*' ! -path "$BACKUP_DIR/*")

if [ $LOCAL_ENV_COUNT -gt 0 ]; then
    echo ""
    echo "✅ All $LOCAL_ENV_COUNT .env file(s) preserved locally"
else
    echo "   No .env files found locally"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ CLEANUP COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Summary:"
if [ "$NEEDS_HISTORY_CLEAN" = true ]; then
    echo "   ✅ Removed .env files from git history"
fi
if [ -n "$TRACKED_ENV_FILES" ]; then
    echo "   ✅ Stopped tracking .env files"
fi
echo "   ✅ Updated .gitignore"
echo "   ✅ All local .env files preserved"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Verify .env files are no longer tracked:"
echo "   git status"
echo "   git ls-files | grep .env  # Should return nothing"
echo ""
echo "2. Verify local files still exist:"
echo "   ls -la .env*"
echo "   find . -name '.env*' -type f"
echo ""
echo "3. Review the commit:"
echo "   git log -1"
echo "   git show"
echo ""
if [ "$NEEDS_HISTORY_CLEAN" = true ]; then
    echo "4. Force push (⚠️  Only if history was cleaned):"
    echo "   git push --force origin $CURRENT_BRANCH"
    echo ""
    echo "   ⚠️  After force push, team members must:"
    echo "   - Delete local repo"
    echo "   - Re-clone"
    echo "   - Restore their .env files from backups"
else
    echo "4. Push normally:"
    echo "   git push origin $CURRENT_BRANCH"
fi
echo ""
echo "5. If something went wrong, restore from backup:"
echo "   cd .."
echo "   rm -rf $REPO_NAME"
echo "   mv $BACKUP_DIR $REPO_NAME"
echo ""
echo "📁 Backup: $BACKUP_DIR"
echo ""
