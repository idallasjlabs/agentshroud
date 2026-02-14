#!/bin/bash
# llm-init.sh
#
# Deploy LLM AI tool configurations to a repository
# This sets up Claude Code (PRIMARY), Gemini CLI (SECONDARY),
# Codex CLI (TERTIARY), and GitHub Copilot CLI (QUATERNARY)
# Plus comprehensive security infrastructure
#
# Usage:
#   source llm-init.sh              # Load function into shell
#   llm-init                        # Deploy to current directory
#   llm-init /path/to/repo          # Deploy to specific directory

llm-init() {
    local target_dir="${1:-.}"
    local source_dir="$HOME/Development/LLM_Settings"

    echo "🚀 Deploying LLM AI tool configurations..."
    echo "   Source: $source_dir"
    echo "   Target: $target_dir"
    echo ""

    # Verify source directory exists
    if [ ! -d "$source_dir" ]; then
        echo "❌ Error: Source directory not found: $source_dir"
        return 1
    fi

    # Create target directory if it doesn't exist
    if [ ! -d "$target_dir" ]; then
        echo "❌ Error: Target directory not found: $target_dir"
        return 1
    fi

    # Navigate to target directory
    cd "$target_dir" || return 1

    # Migration: Clean up old deployment structure
    echo "🧹 Checking for old deployment structure..."
    local cleaned=false

    # Old files/directories to remove
    local old_items=(
        "github-mcp-server"
        "AI_TOOLS_CONFIGURATION_GUIDE.md"
        "CONFIGURATION_SUMMARY.md"
        "MCP_README.md"
        "MCP_ADDITIONAL_SERVICES.md"
        "GEMINI.md"
        ".llm_env_example"
    )

    for item in "${old_items[@]}"; do
        if [ -e "$item" ]; then
            if git ls-files --error-unmatch "$item" >/dev/null 2>&1; then
                echo "   🗑️  Removing tracked: $item"
                git rm -rf "$item" 2>/dev/null
                cleaned=true
            elif [ -d "$item" ]; then
                echo "   🗑️  Removing directory: $item"
                rm -rf "$item"
                cleaned=true
            elif [ -f "$item" ]; then
                echo "   🗑️  Removing file: $item"
                rm -f "$item"
                cleaned=true
            fi
        fi
    done

    if [ "$cleaned" = true ]; then
        echo "   ✅ Old deployment cleaned up"
    else
        echo "   ✅ No old deployment found (clean target)"
    fi
    echo ""

    # Check prerequisites
    echo "📋 Checking prerequisites..."
    echo ""

    # Check for uvx (required for AWS MCP)
    if command -v /opt/homebrew/bin/uvx &> /dev/null; then
        echo "   ✅ uvx found at /opt/homebrew/bin/uvx"
    elif command -v uvx &> /dev/null; then
        echo "   ⚠️  uvx found but not at /opt/homebrew/bin/uvx"
        echo "      AWS MCP may need path adjustment in .mcp.json"
    else
        echo "   ⚠️  uvx not found - AWS MCP will not work"
        echo "      Install with: brew install uv && hash -r"
    fi

    # Check for gh CLI (helpful for GitHub MCP)
    if command -v gh &> /dev/null; then
        echo "   ✅ gh CLI found"
    else
        echo "   ⚠️  gh CLI not found - GitHub MCP token setup may be manual"
        echo "      Install with: brew install gh"
    fi

    # Check for AWS CLI
    if command -v aws &> /dev/null; then
        echo "   ✅ aws CLI found"
    else
        echo "   ⚠️  aws CLI not found - AWS MCP requires AWS credentials"
        echo "      Install with: brew install awscli"
    fi

    # Check for git security tools
    if command -v gitleaks &> /dev/null; then
        echo "   ✅ gitleaks found"
    else
        echo "   ⚠️  gitleaks not found - Install with: brew install gitleaks"
    fi

    if command -v git-secrets &> /dev/null; then
        echo "   ✅ git-secrets found"
    else
        echo "   ⚠️  git-secrets not found - Install with: brew install git-secrets"
    fi

    # Check for pre-commit framework
    if command -v pre-commit &> /dev/null; then
        echo "   ✅ pre-commit found"
    else
        echo "   ⚠️  pre-commit not found - Install with: pip install pre-commit"
        echo "      (Will fall back to manual git hooks)"
    fi

    # Check for direnv
    if command -v direnv &> /dev/null; then
        echo "   ✅ direnv found"
    else
        echo "   ⚠️  direnv not found - Install with: brew install direnv"
        echo "      (Recommended for secure environment variables)"
    fi
    echo ""

    echo "📦 Copying configurations..."
    echo ""

    # 1. Claude Code (PRIMARY Developer)
    echo "1️⃣  Claude Code (PRIMARY)"
    if [ -d "$source_dir/.claude" ]; then
        cp -i -pr "$source_dir/.claude" .
        # Remove local/sensitive files that should not be deployed
        rm -f .claude/settings.local.json 2>/dev/null
        find .claude -name '*.local.*' -delete 2>/dev/null
        rm -rf .claude/.cache .claude/tmp .claude/logs 2>/dev/null
        echo "   ✅ .claude/ directory copied"
    else
        echo "   ⚠️  .claude/ directory not found in source"
    fi

    if [ -f "$source_dir/CLAUDE.md" ]; then
        cp -i -a "$source_dir/CLAUDE.md" .
        echo "   ✅ CLAUDE.md copied"
    else
        echo "   ⚠️  CLAUDE.md not found in source"
    fi

    # Run skills deployment scripts if they exist
    if [ -f ".claude/scripts/deploy-claude-skills.sh" ]; then
        echo "   📚 Regenerating Claude skills..."
        chmod +x .claude/scripts/deploy-claude-skills.sh 2>/dev/null || true
        (cd .claude/scripts && ./deploy-claude-skills.sh 2>/dev/null || true)
    fi

    if [ -f ".claude/scripts/missing/deploy-claude-skills.sh" ]; then
        echo "   📚 Deploying additional skills..."
        chmod +x .claude/scripts/missing/deploy-claude-skills.sh 2>/dev/null || true
        (cd .claude/scripts/missing && ./deploy-claude-skills.sh 2>/dev/null || true)
    fi
    echo ""

    # 2. Gemini CLI (SECONDARY Agent)
    echo "2️⃣  Gemini CLI (SECONDARY)"
    if [ -d "$source_dir/.gemini" ]; then
        cp -i -pr "$source_dir/.gemini" .
        # Remove local/sensitive files that should not be deployed
        rm -f .gemini/settings.local.json 2>/dev/null
        find .gemini -name '*.local.*' -delete 2>/dev/null
        echo "   ✅ .gemini/ directory copied"
    else
        echo "   ⚠️  .gemini/ directory not found in source"
    fi
    echo ""

    # 3. Codex CLI (TERTIARY Agent)
    echo "3️⃣  Codex CLI (TERTIARY)"
    if [ -d "$source_dir/.codex" ]; then
        cp -i -pr "$source_dir/.codex" .
        # Remove local/sensitive files that should not be deployed
        rm -f .codex/config.local.toml 2>/dev/null
        find .codex -name '*.local.*' -delete 2>/dev/null
        echo "   ✅ .codex/ directory copied"
    else
        echo "   ⚠️  .codex/ directory not found in source"
    fi

    if [ -f "$source_dir/AGENTS.md" ]; then
        cp -i -a "$source_dir/AGENTS.md" .
        echo "   ✅ AGENTS.md copied"
    else
        echo "   ⚠️  AGENTS.md not found in source"
    fi
    echo ""

    # 4. GitHub Copilot CLI (QUATERNARY Agent)
    echo "4️⃣  GitHub Copilot CLI (QUATERNARY)"
    if [ -d "$source_dir/.github" ]; then
        # Only copy .github if it doesn't exist, or merge agents/ subdirectory
        if [ ! -d ".github" ]; then
            cp -i -pr "$source_dir/.github" .
            echo "   ✅ .github/ directory copied"
        else
            # Merge agents directory
            if [ -d "$source_dir/.github/agents" ]; then
                mkdir -p .github/agents
                cp -i -pr "$source_dir/.github/agents/"* .github/agents/ 2>/dev/null
                echo "   ✅ .github/agents/ merged"
            fi

            # Copy setup documentation
            if [ -f "$source_dir/.github/COPILOT_CLI_SETUP.md" ]; then
                cp -i -a "$source_dir/.github/COPILOT_CLI_SETUP.md" .github/
                echo "   ✅ .github/COPILOT_CLI_SETUP.md copied"
            fi

            # Copy config example
            if [ -f "$source_dir/.github/copilot-config.json.example" ]; then
                cp -i -a "$source_dir/.github/copilot-config.json.example" .github/
                echo "   ✅ .github/copilot-config.json.example copied"
            fi
        fi
    else
        echo "   ⚠️  .github/ directory not found in source"
    fi
    echo ""

    # 5. MCP Configuration
    echo "5️⃣  MCP Servers"
    if [ -f "$source_dir/.mcp.json" ]; then
        cp -i -a "$source_dir/.mcp.json" .
        echo "   ✅ .mcp.json copied"
    else
        echo "   ⚠️  .mcp.json not found in source"
    fi
    echo ""

    # 6. LLM Settings (all subdirectories deployed recursively)
    echo "6️⃣  LLM Settings Directory"
    if [ -d "$source_dir/llm_settings" ]; then
        # Create llm_settings directory structure
        mkdir -p llm_settings

        # Define all subdirectories to deploy recursively
        local llm_subdirs=(
            "docs"
            "env"
            "git-hooks"
            "mcp-servers"
            "scripts"
            "skills"
            "templates"
        )

        for subdir in "${llm_subdirs[@]}"; do
            if [ -d "$source_dir/llm_settings/$subdir" ]; then
                cp -i -pr "$source_dir/llm_settings/$subdir" llm_settings/
                echo "   ✅ llm_settings/$subdir/ copied (recursive)"
            else
                echo "   ⚠️  llm_settings/$subdir/ not found in source"
            fi
        done

        # Also copy any loose files at the llm_settings root level
        find "$source_dir/llm_settings" -maxdepth 1 -type f -print0 2>/dev/null | while IFS= read -r -d '' file; do
            cp -i -a "$file" llm_settings/
            echo "   ✅ llm_settings/$(basename "$file") copied"
        done

        # Post-copy cleanup: remove sensitive/local files
        echo ""
        echo "   🧹 Cleaning sensitive files..."

        # Remove .env files from mcp-servers (keep .env.example)
        find llm_settings/mcp-servers -name '.env' -delete 2>/dev/null
        find llm_settings/mcp-servers -name '.env.*' ! -name '.env.example' -delete 2>/dev/null
        rm -rf llm_settings/mcp-servers/github/.claude 2>/dev/null

        # Remove any local/sensitive files across all subdirs
        find llm_settings -name '*.local.*' -delete 2>/dev/null
        find llm_settings -name '.DS_Store' -delete 2>/dev/null

        # Make scripts executable
        find llm_settings/scripts -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true
        find llm_settings/git-hooks -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true

        echo "   ✅ Sensitive files cleaned, scripts made executable"
    else
        echo "   ⚠️  llm_settings/ directory not found in source"
    fi
    echo ""

    # 7. Git Security Configuration
    echo "7️⃣  Git Security Configuration"

    # Deploy .gitignore
    if [ -f "$source_dir/llm_settings/templates/.gitignore" ]; then
        if [ -f ".gitignore" ]; then
            echo "   ⚠️  .gitignore already exists"
            read -p "   Replace with comprehensive template? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                cp -a "$source_dir/llm_settings/templates/.gitignore" .
                echo "   ✅ .gitignore replaced with template"
            else
                echo "   ⏭️  Skipped .gitignore (kept existing)"
            fi
        else
            cp -a "$source_dir/llm_settings/templates/.gitignore" .
            echo "   ✅ .gitignore copied from template"
        fi
    else
        echo "   ⚠️  .gitignore template not found in source"
    fi

    # Deploy .pre-commit-config.yaml
    if [ -f "$source_dir/llm_settings/templates/.pre-commit-config.yaml" ]; then
        if [ -f ".pre-commit-config.yaml" ]; then
            echo "   ⚠️  .pre-commit-config.yaml already exists"
            read -p "   Replace with template? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                cp -a "$source_dir/llm_settings/templates/.pre-commit-config.yaml" .
                echo "   ✅ .pre-commit-config.yaml replaced"
            else
                echo "   ⏭️  Skipped .pre-commit-config.yaml (kept existing)"
            fi
        else
            cp -a "$source_dir/llm_settings/templates/.pre-commit-config.yaml" .
            echo "   ✅ .pre-commit-config.yaml copied"
        fi
    else
        echo "   ⚠️  .pre-commit-config.yaml template not found in source"
    fi

    # Deploy .gitallowed
    if [ -f "$source_dir/llm_settings/templates/.gitallowed" ]; then
        if [ -f ".gitallowed" ]; then
            echo "   ⚠️  .gitallowed already exists"
            read -p "   Merge with template? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                # Append template patterns if not already present
                cat "$source_dir/llm_settings/templates/.gitallowed" >> .gitallowed
                # Remove duplicates while preserving comments
                awk '!seen[$0]++' .gitallowed > .gitallowed.tmp && mv .gitallowed.tmp .gitallowed
                echo "   ✅ .gitallowed merged with template"
            else
                echo "   ⏭️  Skipped .gitallowed (kept existing)"
            fi
        else
            cp -a "$source_dir/llm_settings/templates/.gitallowed" .
            echo "   ✅ .gitallowed copied from template"
        fi
    else
        echo "   ⚠️  .gitallowed template not found in source"
    fi

    # Check if this is a git repository
    if [ -d ".git" ]; then
        # Install pre-commit hooks if pre-commit is available
        if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
            echo "   🔒 Installing pre-commit hooks..."
            pre-commit install --install-hooks 2>/dev/null || pre-commit install

            # Create secrets baseline if detect-secrets is configured
            if grep -q "detect-secrets" ".pre-commit-config.yaml" 2>/dev/null; then
                if command -v detect-secrets &> /dev/null; then
                    if [ ! -f ".secrets.baseline" ]; then
                        echo "   📊 Creating secrets baseline..."
                        detect-secrets scan > .secrets.baseline 2>/dev/null || true
                        echo "   ✅ .secrets.baseline created"
                    fi
                fi
            fi

            echo "   ✅ Pre-commit hooks installed"

            # Optional: Run once to verify
            read -p "   Run pre-commit on all files now? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                echo "   🔍 Running pre-commit checks..."
                pre-commit run --all-files || true
                echo ""
            fi
        else
            # Fall back to manual git hooks
            if [ -f "llm_settings/git-hooks/install.sh" ]; then
                echo "   🔒 Installing fallback git hooks..."
                chmod +x llm_settings/git-hooks/install.sh
                llm_settings/git-hooks/install.sh
                echo "   ✅ Fallback git hooks installed"
            else
                echo "   ⚠️  Git hooks installer not found"
            fi

            if ! command -v pre-commit &> /dev/null; then
                echo "   💡 Tip: Install pre-commit for better security"
                echo "      pip install pre-commit"
            fi
        fi
    else
        echo "   ⚠️  Not a git repository - hooks not installed"
        echo "      Run 'pre-commit install' or 'llm_settings/git-hooks/install.sh' after git init"
    fi
    echo ""

    # 8. Security Scripts & Audit
    echo "8️⃣  Security Setup"
    if [ -d "llm_settings/scripts/security" ]; then
        echo "   ✅ Security scripts available:"
        echo "      - setup-direnv.sh      (secure environment variables)"
        echo "      - setup-pgpass.sh      (PostgreSQL passwords)"
        echo "      - security-audit.sh    (scan for secrets in history)"
        echo "      - quick-setup.sh       (run all security setup)"

        # Optionally run security audit
        if [ -d ".git" ]; then
            read -p "   Run security audit now? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                echo ""
                llm_settings/scripts/security/security-audit.sh
                echo ""
            fi
        fi
    else
        echo "   ⚠️  Security scripts not found in source"
    fi
    echo ""

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ LLM AI tool configurations deployed successfully!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📁 Files deployed:"
    echo "   - .claude/                      (agents, skills, hooks, settings)"
    echo "   - .gemini/                      (settings.json with MCP + GEMINI.md context)"
    echo "   - .codex/                       (config.toml with MCP)"
    echo "   - .github/agents/               (custom agent profiles)"
    echo "   - .mcp.json                     (MCP servers for Claude Code)"
    echo "   - .gitignore                    (comprehensive security template)"
    echo "   - .pre-commit-config.yaml       (secret detection framework)"
    echo "   - .gitallowed                   (false positive patterns)"
    if [ -f ".git/hooks/pre-commit" ]; then
        echo "   - .git/hooks/pre-commit         (secret scanning protection)"
    fi
    echo "   - CLAUDE.md                     (primary developer context)"
    echo "   - AGENTS.md                     (secondary/tertiary agent context)"
    echo "   - llm_settings/                 (organized LLM configuration)"
    echo "     ├── docs/                     (documentation files)"
    echo "     ├── scripts/                  (deployment & security scripts)"
    echo "     │   ├── llm-init.sh"
    echo "     │   └── security/             (direnv, pgpass, audit)"
    echo "     ├── env/                      (environment templates)"
    echo "     ├── git-hooks/                (fallback security hooks)"
    echo "     ├── templates/                (.gitignore, pre-commit, .gitallowed)"
    echo "     ├── skills/                   (LLM skill definitions)"
    echo "     └── mcp-servers/              (GitHub & Atlassian MCP servers)"
    echo ""
    echo "📝 Next steps:"
    echo "   1. 📖 Read: llm_settings/docs/SECURITY_GUIDE.md"
    echo "   2. 📖 Read: llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo "   3. 🔒 Security: llm_settings/scripts/security/quick-setup.sh"
    echo "   4. 🔌 MCP GitHub: cp llm_settings/mcp-servers/github/.env.example .env"
    echo "   5. 🔌 MCP User: llm_settings/scripts/setup-mcp-user.sh (global config)"
    echo "   6. ☁️  AWS: export AWS_PROFILE=default AWS_REGION=us-east-1"
    echo "   7. 🤖 Test tools:"
    echo "      - claude      (PRIMARY developer)"
    echo "      - gemini      (SECONDARY agent)"
    echo "      - codex       (TERTIARY agent)"
    echo "      - copilot     (QUATERNARY agent)"
    echo ""
    echo "🔌 MCP Servers configured:"
    echo "   - GitHub     (llm_settings/mcp-servers/github/)"
    echo "   - Atlassian  (llm_settings/mcp-servers/atlassian/)"
    echo "   - AWS API    (via uvx awslabs.aws-api-mcp-server)"
    echo ""
    echo "   📝 Project-level: .mcp.json (works in this repo only)"
    echo "   💡 User-level: Run setup-mcp-user.sh to enable 'claude mcp list'"
    echo ""

    # Offer to configure user-level MCP servers
    if [ -f "llm_settings/scripts/setup-mcp-user.sh" ]; then
        read -p "   Configure MCP servers globally (user-level)? [y/N] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            llm_settings/scripts/setup-mcp-user.sh
            echo ""
        else
            echo "   ⏭️  Skipped user-level MCP setup"
            echo "      Run later with: llm_settings/scripts/setup-mcp-user.sh"
            echo ""
        fi
    fi

    # Security status
    echo "🔒 Security features installed:"
    if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
        echo "   ✅ Pre-commit framework (gitleaks + detect-secrets + validators)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Pre-commit commands:"
        echo "      pre-commit run --all-files    # Run all hooks manually"
        echo "      pre-commit autoupdate         # Update hook versions"
        echo "      git commit --no-verify        # Skip hooks (emergency only)"
    elif [ -f ".git/hooks/pre-commit" ]; then
        echo "   ✅ Git hooks (gitleaks + git-secrets)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Upgrade to pre-commit framework:"
        echo "      pip install pre-commit"
        echo "      pre-commit install"
    else
        echo "   ⚠️  No hooks installed (not a git repository)"
    fi
    echo ""

    echo "🧪 Test git security:"
    echo "   echo 'password=secret123' > test.txt"
    echo "   git add test.txt"
    echo "   git commit -m 'test'  # Should be blocked!"
    echo "   rm test.txt"
    echo ""
    echo "🔒 Security best practices:"
    echo "   ✅ Never commit .env files (use direnv instead)"
    echo "   ✅ Never commit API keys (use AWS Secrets Manager)"
    echo "   ✅ Never commit passwords (use ~/.pgpass for PostgreSQL)"
    echo "   ✅ Run security audit periodically"
    echo "   ✅ Review all files before committing"
    echo ""
    echo "📚 Documentation:"
    echo "   - Security Guide:     llm_settings/docs/SECURITY_GUIDE.md"
    echo "   - AI Tools Guide:     llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md"
    echo "   - Quick Reference:    llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo ""
}

# Export function if script is sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    export -f llm-init
    echo "✅ llm-init function loaded"
    echo "   Usage: llm-init [target_directory]"
fi

# If script is executed (not sourced), run the function
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    llm-init "$@"
fi
