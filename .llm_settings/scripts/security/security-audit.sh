#!/usr/bin/env bash
# security-audit.sh
# Initial security audit and setup for a repository

set -e

echo "🔍 Running initial security audit..."
echo ""

# Step 1: Check for gitleaks
echo "1️⃣  Checking for gitleaks..."
if ! command -v gitleaks &> /dev/null; then
    echo "📦 Installing gitleaks..."
    if command -v brew &>/dev/null; then
        brew install gitleaks && echo "   ✅ gitleaks installed"
    elif command -v go &>/dev/null; then
        go install github.com/gitleaks/gitleaks/v8@latest && echo "   ✅ gitleaks installed via go"
    else
        echo "   ⚠️  gitleaks not found — install manually and re-run:"
        echo "      macOS:  brew install gitleaks"
        echo "      Linux:  go install github.com/gitleaks/gitleaks/v8@latest"
        echo "      Binary: https://github.com/gitleaks/gitleaks/releases"
        echo "   Skipping gitleaks checks."
        SKIP_GITLEAKS=true
    fi
else
    echo "✅ gitleaks already installed"
fi
echo ""

# Step 2: Check for git-secrets
echo "2️⃣  Checking for git-secrets..."
if ! command -v git-secrets &> /dev/null; then
    echo "📦 Installing git-secrets..."
    if command -v brew &>/dev/null; then
        brew install git-secrets && echo "   ✅ git-secrets installed"
    elif command -v git &>/dev/null && command -v make &>/dev/null; then
        _tmp=$(mktemp -d)
        git clone --depth 1 https://github.com/awslabs/git-secrets.git "$_tmp/git-secrets" 2>/dev/null \
            && (cd "$_tmp/git-secrets" && sudo make install 2>/dev/null) \
            && echo "   ✅ git-secrets installed from source" \
            || { echo "   ⚠️  git-secrets source install failed. See: https://github.com/awslabs/git-secrets#installing-git-secrets"; SKIP_GIT_SECRETS=true; }
        rm -rf "$_tmp"
    else
        echo "   ⚠️  git-secrets not found — install manually and re-run:"
        echo "      macOS: brew install git-secrets"
        echo "      Linux: https://github.com/awslabs/git-secrets#installing-git-secrets"
        SKIP_GIT_SECRETS=true
    fi
else
    echo "✅ git-secrets already installed"
fi
echo ""

# Step 3: Scan repository history
echo "3️⃣  Scanning repository history for secrets..."
if [ "${SKIP_GITLEAKS:-false}" = "true" ]; then
    echo "⚠️  Skipping (gitleaks not installed)"
elif [ -d ".git" ]; then
    echo "   This may take a while for large repositories..."
    if gitleaks detect --report-path gitleaks-report.json --verbose; then
        echo "✅ No secrets detected in repository history"
        rm -f gitleaks-report.json
    else
        echo "❌ SECRETS DETECTED in repository history!"
        echo ""
        echo "📄 Full report saved to: gitleaks-report.json"
        echo ""
        echo "⚠️  CRITICAL: You must clean these secrets from git history"
        echo "   Options:"
        echo "   1. Use BFG Repo-Cleaner: https://rtyley.github.io/bfg-repo-cleaner/"
        echo "   2. Use git-filter-repo: pip install git-filter-repo"
        echo "   3. Manual: git filter-branch (not recommended)"
        echo ""
        read -p "   View report now? [y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            cat gitleaks-report.json | jq '.' 2>/dev/null || cat gitleaks-report.json
        fi
        exit 1
    fi
else
    echo "⚠️  Not a git repository - skipping history scan"
fi
echo ""

# Step 4: Check .gitignore
echo "4️⃣  Checking .gitignore coverage..."
if [ -f ".gitignore" ]; then
    MISSING_PATTERNS=()
    
    # Critical patterns to check
    grep -q "^\.env$" .gitignore || MISSING_PATTERNS+=(".env")
    grep -q "\.pem$" .gitignore || MISSING_PATTERNS+=("*.pem")
    grep -q "\.key$" .gitignore || MISSING_PATTERNS+=("*.key")
    grep -q "password" .gitignore || MISSING_PATTERNS+=("*password*")
    
    if [ ${#MISSING_PATTERNS[@]} -eq 0 ]; then
        echo "✅ .gitignore has good security coverage"
    else
        echo "⚠️  .gitignore missing critical patterns:"
        for pattern in "${MISSING_PATTERNS[@]}"; do
            echo "      - $pattern"
        done
        echo "   Consider using the comprehensive template from llm_settings"
    fi
else
    echo "❌ No .gitignore file found!"
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    TEMPLATES_DIR="$(cd "$SCRIPT_DIR/../../templates" 2>/dev/null && pwd || echo '<llm_settings>/templates')"
    echo "   Create one with: cp $TEMPLATES_DIR/.gitignore ."
fi
echo ""

# Step 5: Check for existing secrets in working directory
echo "5️⃣  Scanning working directory for secrets..."
if [ "${SKIP_GITLEAKS:-false}" = "true" ]; then
    echo "⚠️  Skipping (gitleaks not installed)"
elif gitleaks protect --staged --verbose; then
    echo "✅ No secrets in current working directory"
else
    echo "⚠️  Potential secrets found in working directory"
    echo "   Review and remove before committing"
fi
echo ""

# Step 6: Summary and recommendations
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Security Audit Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "✅ Recommended next steps:"
echo "   1. Install git hooks: .llm_settings/git-hooks/install.sh"
echo "   2. Or use pre-commit: pip install pre-commit && pre-commit install"
echo "   3. Set up direnv: .llm_settings/scripts/security/setup-direnv.sh"
echo "   4. Configure pgpass: .llm_settings/scripts/security/setup-pgpass.sh"
echo "   5. Test hooks: echo 'password=test' > test.txt && git add test.txt"
echo ""

echo "🔒 Security best practices:"
echo "   - Never commit .env files"
echo "   - Use AWS Secrets Manager / SSM for credentials"
echo "   - Use ~/.pgpass for PostgreSQL passwords"
echo "   - Review all files before committing"
echo "   - Run 'gitleaks detect' periodically"
echo ""

