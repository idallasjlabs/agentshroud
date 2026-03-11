# Git Hooks for Secret Protection

Pre-commit hooks to prevent committing secrets across all Fluence GSDE&G repositories.

## Quick Start

### Install to Current Repo
```bash
cd /path/to/your/repo
~/.llm_settings/git-hooks/install.sh
```

### Install Globally (All New Repos)
```bash
~/.llm_settings/git-hooks/install.sh --global
```

## What It Does

- 🔍 Scans staged files for secrets before commit
- 🚫 Blocks commits containing:
  - AWS credentials
  - API keys
  - Passwords
  - Private keys
  - Tokens
- ✅ Allows commit only if clean

## Requirements

Install these tools first:
```bash
brew install gitleaks git-secrets
```

## For GSDE&G Team

Add this to your onboarding checklist:

1. Install tools: `brew install gitleaks git-secrets`
2. Set up global hooks: `~/.llm_settings/git-hooks/install.sh --global`
3. For existing repos: `cd <repo> && ~/.llm_settings/git-hooks/install.sh`

## Manual Installation
```bash
# Copy hook to any repo
cp ~/.llm_settings/git-hooks/pre-commit /path/to/repo/.git/hooks/
chmod +x /path/to/repo/.git/hooks/pre-commit
```

## Testing
```bash
# Test in a repo
echo "password=secret123" > test.txt
git add test.txt
git commit -m "test"  # Should be blocked!
```

## Troubleshooting

**Hook not running?**
- Check it's executable: `ls -la .git/hooks/pre-commit`
- Run manually: `.git/hooks/pre-commit`

**False positives?**
- Create `.gitleaksignore` in repo root
- Add file patterns to ignore

**Skip hook (emergency only):**
```bash
git commit --no-verify -m "message"
```
