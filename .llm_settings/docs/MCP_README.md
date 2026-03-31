# MCP / OAuth Environment Configuration Guide

This document explains **how to obtain and configure all environment variables**
used for:

- MCP OAuth preflight testing
- Claude Code MCP integrations
- GitHub, Atlassian (Jira/Confluence), and Microsoft Entra (Office 365)

⚠️ **Security Notice**
- The `.env` file **must never be committed**
- All secrets belong in `.env` only
- `.env` should be listed in `.gitignore`

---

## Overview

We use **OAuth-based authentication** for MCP integrations.
Before enabling MCP, we validate that OAuth works in our enterprise environment
using the script:

```bash
python3 mcp_oauth_preflight.py oauth
```

This README explains where to get each value required by that script.

---

## Prerequisites

### UV Package Manager (Required for AWS MCP)

The AWS MCP server uses `uvx` from the `uv` package manager to run Python packages without installing them globally.

**macOS Installation:**
```bash
# Install uv via Homebrew
brew install uv

# Refresh shell's command hash table
hash -r

# Verify installation
which uvx
# Expected: /opt/homebrew/bin/uvx

uvx --version
# Expected: uvx 0.x.x
```

**Linux Installation:**
```bash
# Install via curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.cargo/bin:$PATH"

# Verify installation
which uvx
uvx --version
```

**Windows Installation:**
```powershell
# Install via PowerShell
irm https://astral.sh/uv/install.ps1 | iex

# Verify installation
uvx --version
```

**Troubleshooting UV:**
- If `uvx` is not found after installation, run `hash -r` to refresh your shell's cache
- On macOS, ensure `/opt/homebrew/bin` is in your PATH
- The `.mcp.json` uses absolute path `/opt/homebrew/bin/uvx` to avoid PATH issues

---

## Environment File Layout

All values live in a single file:

```text
.env
```

Load it with:

```bash
set -a
source .env
set +a
```

---

## 1. GitHub OAuth (Device Authorization Flow)

Used to validate **direct GitHub MCP OAuth**.

### Variables

```dotenv
GITHUB_CLIENT_ID=
GITHUB_SCOPES=read:user repo
```

### Where to get them

1. Go to GitHub Developer Settings:  
   https://github.com/settings/developers
2. Select **OAuth Apps**
3. Click **New OAuth App**
4. Fill in:
   - **Application name**: `Claude MCP Preflight`
   - **Homepage URL**: `http://localhost`
   - **Authorization callback URL**: `http://localhost`
5. Create the app
6. Copy:
   - **Client ID** → `GITHUB_CLIENT_ID`

### Notes
- Device Flow does **not** require a client secret
- GitHub will prompt you in the browser during the test

---

## 2. Atlassian OAuth 2.0 (3LO)
(Jira + Confluence Cloud)

Used to validate **direct Atlassian MCP OAuth**.

### Variables

```dotenv
ATLASSIAN_CLIENT_ID=
ATLASSIAN_CLIENT_SECRET=
ATLASSIAN_SCOPES=read:jira-user read:jira-work write:jira-work read:confluence-content.summary write:confluence-content
# ATLASSIAN_REDIRECT_URI=http://127.0.0.1:8000/callback
```

### Where to get them

1. Go to Atlassian Developer Console:  
   https://developer.atlassian.com/console/myapps/
2. Click **Create → OAuth 2.0 (3LO) app**
3. App settings:
   - **Name**: `Claude MCP Preflight`
   - **Callback URL**:
     ```
     http://127.0.0.1/callback
     ```
4. Permissions:
   - Jira:
     - `read:jira-user`
     - `read:jira-work`
     - `write:jira-work`
   - Confluence:
     - `read:confluence-content.summary`
     - `write:confluence-content`
5. Save the app
6. Copy:
   - **Client ID** → `ATLASSIAN_CLIENT_ID`
   - **Client Secret** → `ATLASSIAN_CLIENT_SECRET`

### Important Enterprise Note
- Atlassian OAuth does **not** authenticate via your site domain
  (`fluenceenergy.atlassian.net`)
- Authentication occurs via:
  ```
  https://auth.atlassian.com
  ```
- Loopback callbacks (`127.0.0.1`) must be allowed by policy

---

## 3. AWS MCP Server (awslabs.aws-api-mcp-server)

The AWS API MCP server enables Claude Code to interact with AWS services via the AWS CLI.

### Configuration

The server is pre-configured in `.mcp.json`:

```json
{
  "mcpServers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "awslabs.aws-api-mcp-server@latest",
        "--readonly"
      ],
      "env": {
        "AWS_PROFILE": "${AWS_PROFILE:-default}",
        "AWS_REGION": "${AWS_REGION:-us-east-1}",
        "FASTMCP_LOG_LEVEL": "${FASTMCP_LOG_LEVEL:-ERROR}"
      }
    }
  }
}
```

### Setup Steps

1. **Install UV package manager** (see Prerequisites above)

2. **Configure AWS credentials:**
   ```bash
   # If you haven't configured AWS CLI yet
   aws configure

   # Or use a named profile
   aws configure --profile myprofile

   # List available profiles
   aws configure list-profiles
   ```

3. **Set environment variables:**
   ```bash
   # Add to .env or shell profile
   export AWS_PROFILE=default
   export AWS_REGION=us-east-1
   ```

4. **Verify the server starts:**
   ```bash
   # Test uvx can run the server
   /opt/homebrew/bin/uvx awslabs.aws-api-mcp-server@latest --readonly --help
   ```

5. **Restart Claude Code** and run `/mcp` to verify the AWS server is connected.

### Available Tools

The AWS MCP server provides two main tools:

| Tool | Description |
|------|-------------|
| `suggest_aws_commands` | Get AWS CLI command suggestions from natural language |
| `call_aws` | Execute AWS CLI commands with validation |

### Usage Examples

```
# Ask for AWS CLI suggestions
"How do I list all S3 buckets?"

# Execute AWS commands
"Run: aws s3 ls"
"List my EC2 instances in us-east-1"
```

### Security Note

The server runs with `--readonly` flag by default, which prevents write operations. Remove this flag only if you need to perform write operations and understand the risks.

---

## 4. Microsoft Entra ID (Office 365 / Internal Gateway)

Used to validate **enterprise OAuth policy** for an internal MCP gateway.

### Variables

```dotenv
ENTRA_CLIENT_ID=
ENTRA_TENANT=organizations
ENTRA_SCOPES=openid profile offline_access
```

### Where to get them

1. Go to Microsoft Entra Portal:  
   https://entra.microsoft.com/
2. Navigate to:  
   **Microsoft Entra ID → App registrations**
3. Click **New registration**
4. Fill in:
   - **Name**: `Claude MCP Preflight`
   - **Supported account types**:
     - Accounts in this organizational directory only
5. Register the app

### After registration

1. Go to **Authentication**
   - Enable:
     - ✅ **Allow public client flows**
2. Go to **Overview**
   - Copy:
     - **Application (client) ID** → `ENTRA_CLIENT_ID`

### Tenant value options

You may use:
- `organizations` (recommended default)
- Your tenant GUID
- Your tenant domain (`company.onmicrosoft.com`)

---

## 5. Legacy Tokens (Optional / Not Used for MCP)

These values are **not used by MCP or OAuth**, but may exist for
older scripts or automation.

```dotenv
# GITHUB_TOKEN=
# ATLASSIAN_API_TOKEN=
# API_ACCESS_ID=
# API_ACCESS_KEY=
```

If you do not know what uses them, leave them commented out.

---

## 6. Validating OAuth

Once `.env` is populated:

```bash
python3 mcp_oauth_preflight.py oauth
```

Expected behavior:
- Browser opens
- You authenticate interactively
- Script prints:

```
PASS: OAuth SUCCESS
```

Failures indicate policy, app approval, or network restrictions and should
be shared with IT/IAM.

---

## 7. Relationship to MCP Configuration

This README and `.env` are **only for validation**.

If OAuth succeeds:
- Claude Code MCP is configured using **only the MCP server URL**
- OAuth credentials are handled interactively by Claude Code

### Examples

```bash
# GitHub and Atlassian use HTTP transport with OAuth
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --scope project
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp --scope project

# AWS MCP is configured via .mcp.json (local uvx-based server)
# See .mcp.json for AWS configuration
```

---

## Summary

- `.env` contains all OAuth preflight configuration
- Values come from:
  - GitHub Developer Settings
  - Atlassian Developer Console
  - Microsoft Entra App Registrations
- OAuth is validated **before** enabling MCP
- Secrets never enter the repository

If in doubt: **do not guess — ask IT or the app owner**.
