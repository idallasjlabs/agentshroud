# Security Guide - Fluence GSDE&G Team

Comprehensive security configuration for protecting secrets and credentials in git repositories.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Environment Variable Management](#environment-variable-management)
3. [PostgreSQL Password Management](#postgresql-password-management)
4. [Git Security](#git-security)
5. [Security Audit](#security-audit)
6. [Team Standards](#team-standards)

---

## Quick Start

### For New Repositories
```bash
# Deploy LLM settings (includes security)
llm-init

# Run comprehensive security setup
.llm_settings/scripts/security/quick-setup.sh
```

### For Existing Repositories
```bash
# Run security audit
.llm_settings/scripts/security/security-audit.sh

# Fix any issues found, then install hooks
pre-commit install
# OR
.llm_settings/git-hooks/install.sh
```

---

## Environment Variable Management

### Using direnv (Recommended)

direnv automatically loads/unloads environment variables when entering/leaving directories.

**Setup:**
```bash
# Run setup script
.llm_settings/scripts/security/setup-direnv.sh

# Copy template
cp .envrc.example .envrc

# Edit with your values
vim .envrc

# Allow direnv to load
direnv allow
```

**Example .envrc:**
```bash
# AWS Secrets Manager
export DB_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id fluence/db/password \
  --query SecretString \
  --output text)

# AWS SSM Parameter Store
export API_KEY=$(aws ssm get-parameter \
  --name /fluence/api-key \
  --with-decryption \
  --query Parameter.Value \
  --output text)

# Environment settings
export AWS_PROFILE=fluence-dev
export AWS_REGION=us-east-1
```

**Security Features:**

- ✅ Variables only loaded in project directory
- ✅ Automatically unloaded when leaving directory
- ✅ `.envrc` is gitignored automatically
- ✅ Integrates with AWS Secrets Manager/SSM

---

## PostgreSQL Password Management

### Using ~/.pgpass (Recommended)

Never store PostgreSQL passwords in code or `.env` files.

**Setup:**
```bash
# Run setup script
.llm_settings/scripts/security/setup-pgpass.sh

# Edit pgpass file
vim ~/.pgpass
```

**Format:**
```
hostname:port:database:username:password
```

**Examples:**
```
# Production
prod-db.fluence.io:5432:operations:app_user:prod_password

# Development (wildcard for any database)
dev-db.fluence.local:5432:*:fluence_dev:dev_password

# Localhost
localhost:5432:*:postgres:local_password
```

**Python Usage:**
```python
import psycopg2

# Password automatically loaded from ~/.pgpass
conn = psycopg2.connect(
    host="prod-db.fluence.io",
    port=5432,
    database="operations",
    user="app_user"
    # NO password parameter needed!
)
```

### Alternative: AWS RDS IAM Authentication

For AWS RDS databases:
```bash
# Generate temporary token
export PGPASSWORD=$(aws rds generate-db-auth-token \
  --hostname your-db.rds.amazonaws.com \
  --port 5432 \
  --username iam_user \
  --region us-east-1)

# Connect
psql -h your-db.rds.amazonaws.com -U iam_user -d operations
```

---

## Git Security

### Pre-commit Hooks

Two options: **pre-commit framework** (recommended) or **manual git hooks**.

#### Option 1: Pre-commit Framework (Recommended)
```bash
# Install pre-commit
pip install pre-commit

# Install hooks (done automatically by llm-init)
pre-commit install

# Run manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

**What it checks:**

- ✅ Secrets (gitleaks)
- ✅ AWS credentials
- ✅ Private keys
- ✅ Large files (>10MB)
- ✅ YAML/JSON syntax
- ✅ Trailing whitespace
- ✅ Merge conflicts

#### Option 2: Manual Git Hooks
```bash
# Install hooks
.llm_settings/git-hooks/install.sh

# Or globally for all new repos
.llm_settings/git-hooks/install.sh --global
```

### .gitignore Template

Comprehensive template covering:

- Environment files (`.env`, `.env.*`)
- Credentials (`.pem`, `.key`, `*password*`, `*secret*`)
- AWS files (`.aws/`, `credentials`)
- Database files (`*.sql.gz`, `*.dump`, `.pgpass`)
- Platform-specific (macOS, Windows, Linux)
- IDE files (VSCode, PyCharm, etc.)
- Fluence-specific patterns

**Deploy:**
```bash
cp ~/Development/LLM_Settings/.llm_settings/templates/.gitignore .
```

---

## Security Audit

### Initial Repository Scan
```bash
# Run comprehensive audit
.llm_settings/scripts/security/security-audit.sh
```

**What it does:**

1. ✅ Installs gitleaks & git-secrets
2. ✅ Scans entire git history for secrets
3. ✅ Checks .gitignore coverage
4. ✅ Scans working directory
5. ✅ Provides remediation steps

### If Secrets Found in History

**Option 1: BFG Repo-Cleaner (Recommended)**
```bash
# Install
brew install bfg

# Remove secrets
bfg --delete-files secrets.txt
bfg --replace-text passwords.txt

# Clean up
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push (WARNING: rewrites history)
git push --force
```

**Option 2: git-filter-repo**
```bash
# Install
pip install git-filter-repo

# Remove file
git filter-repo --path path/to/secret/file --invert-paths

# Or remove text
git filter-repo --replace-text expressions.txt
```

---

## Team Standards

### GSDE&G Security Requirements

All repositories MUST have:

1. ✅ **Comprehensive .gitignore** (use template)
2. ✅ **Pre-commit hooks** (gitleaks + detect-secrets)
3. ✅ **No secrets in git history** (audit before sharing)
4. ✅ **Environment variables via direnv** (not .env files)
5. ✅ **PostgreSQL passwords via ~/.pgpass** (not in code)

### Onboarding Checklist

For new team members:
```bash
# 1. Install security tools
brew install gitleaks git-secrets direnv

# 2. Set up global git hooks template
~/Development/LLM_Settings/.llm_settings/git-hooks/install.sh --global

# 3. Configure direnv
# (Add hook to ~/.zshrc - done by setup script)

# 4. Set up PostgreSQL
~/Development/LLM_Settings/.llm_settings/scripts/security/setup-pgpass.sh
```

### For Existing Repositories
```bash
# Deploy security config
llm-init

# Run audit
.llm_settings/scripts/security/security-audit.sh

# Fix any issues
# (Remove secrets, update .gitignore, etc.)

# Install hooks
pre-commit install
```

### Code Review Requirements

Before approving PRs, verify:

- ✅ No `.env` files committed
- ✅ No hardcoded passwords/keys
- ✅ No AWS credentials in code
- ✅ Secrets use Secrets Manager/SSM
- ✅ Database passwords use ~/.pgpass or IAM

---

## Emergency Procedures

### Secret Accidentally Committed
```bash
# 1. DO NOT PUSH if not yet pushed
git reset HEAD~1  # Undo commit
git add .gitignore  # Add missing patterns
git commit -m "Add security patterns"

# 2. If already pushed - ROTATE CREDENTIALS IMMEDIATELY
# - Revoke AWS keys in IAM
# - Change database passwords
# - Rotate API tokens

# 3. Clean history (after rotating)
bfg --delete-files .env
git push --force
```

### Pre-commit Hook Bypass

**NEVER bypass hooks except in emergencies:**
```bash
# Emergency only - requires approval
git commit --no-verify -m "Emergency fix"
```

**Then immediately:**

1. File incident report
2. Audit what was committed
3. Rotate any exposed credentials
4. Review with team lead

---

## Additional Resources

- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/)
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [direnv Documentation](https://direnv.net/)
- [PostgreSQL .pgpass](https://www.postgresql.org/docs/current/libpq-pgpass.html)
- [gitleaks](https://github.com/gitleaks/gitleaks)
- [pre-commit](https://pre-commit.com/)

---

## Questions?

Contact: GSDE&G Team Lead
Slack: #gsde-governance
