---
title: gitleaks.toml
type: config
file_path: gitleaks.toml
tags: [security, secrets, git]
related: [Configuration/All Environment Variables]
status: documented
---

# gitleaks.toml

**Location:** `gitleaks.toml` (repo root)
**Tool:** gitleaks — secret detection in git history

## Purpose

Configuration for gitleaks, which scans git commits and staged changes for accidentally committed secrets. Prevents API keys, tokens, and credentials from entering the repository.

## Usage

```bash
# Scan entire repo history
gitleaks detect

# Scan staged changes (pre-commit hook)
gitleaks protect --staged
```

## Integration

Configured in `.pre-commit-config.yaml` to run on every commit. If a secret is detected, the commit is rejected with details about the finding.

## What It Checks

- Anthropic API keys
- OpenAI API keys
- Telegram bot tokens
- Generic high-entropy strings
- AWS credentials
- GitHub tokens
- 1Password tokens

## Related Notes

- [[Configuration/All Environment Variables]] — Vars that must NOT be in code
- [[Runbooks/First Time Setup]] — Secret management practices
