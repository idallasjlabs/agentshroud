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

## 8. Teamwork Graph CLI (Atlassian, non-MCP)

[TWG CLI](https://teamworkgraph.com/cli) ([developer docs](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/)) is
Atlassian's own official agent-integration tool. It is **not an MCP server** —
do not add it to `.mcp.json` / `.gemini/settings.json` / `.codex/config.toml` /
`.github/mcp.json`. It complements, and does not replace, the `atlassian-*`
`mcp-atlassian` servers documented above (broader graph across Jira +
Confluence + Bitbucket + code + Teams + Drive vs. direct Jira/Confluence API
access).

### Install (once per machine)

```bash
curl -fsSL --retry 2 https://teamwork-graph.atlassian.com/cli/install | bash
```

First-time setup requires a controlling terminal (interactive OAuth 2.1
browser login). To repair/verify later: `twg setup` / `twg doctor`.

`llm-init --mcp twg .` never runs the installer — it only detects `twg` on
`PATH` and runs `twg doctor` to report status (see `_llm_init_check_twg` in
`llm-init.sh`).

### Account separation (Fluence vs personal) and auth checks

twg keeps **one** OAuth login per machine (`~/.config/twg`) with no profile
switching, and the Fluence and personal Atlassian accounts must never be mixed.
`llm-init` therefore detects rather than switches:

| `--mcp` selection | Repo scope | twg check | sf check |
|---|---|---|---|
| `fluence` | fluence | `twg whoami` email domain must be Fluence, else **MISMATCH** warning | org `fluence` must be `Connected` |
| `personal` | personal | email domain must NOT be Fluence, else **MISMATCH** warning | skipped (org is Fluence-only) |
| `all` / both | mixed | informational — reports the active scope (one login can't serve both) | org `fluence` check |
| neither (e.g. `aws` only) | none | only if `--mcp twg` was given | skipped |

- Scope is derived from the selection (or the sticky `.llm_settings/repo-mcp-servers`
  marker); no new marker values.
- Checks are **warn-only and read-only**: they never log in, never switch
  accounts, and never fail `llm-init`. On a mismatch or missing login they print
  the fix (`twg setup`; `sf org login web -a fluence --instance-url <url>`) for
  you to run in your own terminal.
- Fluence domain defaults to `fluenceenergy.com`; override with
  `LLM_INIT_FLUENCE_EMAIL_DOMAIN`. Salesforce org alias/URL: `SFQ_ORG`,
  `SFQ_INSTANCE_URL`.
- **Agent rule:** before any twg work, run `twg whoami` and confirm the email
  domain matches the repo scope; on a mismatch stop and ask the user to
  re-authenticate. The `i-sf` skill applies the same guard to Salesforce.

### Skills install globally, not per-repo

The installer drops its own "skills" (context files) into **home-directory**
locations:
- `~/.agents/skills` — universal layout read by Codex, Gemini CLI, GitHub
  Copilot, Cursor, Rovo Dev
- `~/.claude/skills` — Claude Code

These are distinct from the **per-repo** `.claude/skills/` (and per-CLI
equivalents) that `llm-init.sh` deploys from `.llm_settings/skills/` — nothing
here needs conversion or rsync-ing.

### Permissions

Configured org-wide in Atlassian Administration → Rovo → Teamwork Graph CLI,
across three categories: Read, Write and manage, Delete. Enforced
server-side by Atlassian (not bypassable via the local binary/config).

### Network allowlist (only if Claude Code sandboxing is enabled)

This repo's `.claude/settings.json` does not currently set
`network.allowedDomains`. If that setting is ever enabled, TWG's whiteboard/
attachment tools additionally need:

```
api.media.atlassian.com
*.frontend.public.atl-paas.net
```

---

## 9. Gmail (workspace-mcp, many accounts)

[`workspace-mcp`](https://github.com/taylorwilsdon/google_workspace_mcp) runs as one
**stdio** MCP server **per Gmail account** (`gmail-<alias>`), so it works unchanged in
every client that can launch a stdio command (Claude Code, Gemini CLI, Codex, GitHub
Copilot, Hermes, OpenClaw, …). Each account has its own token store, so tokens cannot
collide. The claude.ai Gmail connector is not used (one Google account per connector).

```bash
llm-init --mcp gmail .       # standalone
llm-init --mcp personal .    # included in the personal group
llm-init --mcp all .         # included in all (never in --mcp fluence)
```

### One-time setup

1. **OAuth client (shared by all accounts):** Google Cloud Console → enable the Gmail API →
   Credentials → Create OAuth client ID → *Desktop app*. Add each Gmail address as a test
   user, or publish the app — in "Testing" status tokens expire after 7 days.
2. **Store the client** (never in a repo or config file):
   ```bash
   security add-generic-password -U -T "" -s "Google Workspace MCP" -a "client-id"     -w "<id>"
   security add-generic-password -U -T "" -s "Google Workspace MCP" -a "client-secret" -w "<secret>"
   ```
   (or `GOOGLE_OAUTH_CLIENT_ID` / `GOOGLE_OAUTH_CLIENT_SECRET` env vars, or 1Password
   `op://Personal/Google Workspace MCP/client-id|client-secret`; resolution is handled by
   `scripts/security/resolve-cred.sh`).
3. **List your accounts** — one alias per line (lowercase letters, digits, `-`), non-secret:
   `~/.config/llm-settings/gmail-accounts` (override with `LLM_INIT_GMAIL_ACCOUNTS`).
4. Run `llm-init --mcp gmail .`. It renders `gmail-<alias>` into `.mcp.json`,
   `.gemini/settings.json`, `.github/mcp.json` and `.codex/config.toml`. Re-running is
   idempotent; deleting an alias removes its entry. Missing/empty accounts file → a
   warning, no entries.
5. **First use of each account:** call a Gmail tool; the server returns a Google consent
   URL — open it and pick the matching address. Tokens land in
   `~/.config/llm-settings/gmail/<alias>/` (mode 700).

### Safety: send is off by default

`GMAIL_MCP_LEVEL` sets the cumulative access level passed as `--permissions gmail:<level>`:

| Level | Allows |
|---|---|
| `readonly` | read / search |
| `organize` (**default**) | + labels, filters, archive |
| `drafts` | + create drafts |
| `send`, `full` | + send — **refused unless `GMAIL_MCP_ALLOW_SEND=1` is also set** |

Email, docs and events can contain hidden instructions aimed at the agent; keep send
disabled unless you need it.

### Hermes and OpenClaw

`llm-init` does not manage their config, so it **prints** the per-account command to add
(`gmail-<alias> → <abs path>/mcp-gmail.sh <alias>`). Hermes runs in a container and OpenClaw
under the `agentshroud-bot` account: each needs its own accounts, `uvx`, OAuth client
credentials and consent run — this Mac's Keychain is not visible there. Their MCP key names
are not verified in this repo; confirm them against each tool's docs.

### Verify

```bash
bash tests/test-gmail-mcp.sh      # wrapper, renderer, group integration (stubbed, no Google calls)
```

## 10. Additional CLIs: OpenCode, Crush, Antigravity, Grok Build, Pi, Oh My Pi

`llm-init` deploys the same skills, agents and MCP servers to six more CLIs, **per repo**
(nothing is written to your home directory). Select them with `--tools` (default `all`):

```bash
llm-init --mcp personal .                       # all 10 tools
llm-init --mcp fluence --tools opencode,pi .    # Claude (always) + OpenCode + Pi only
llm-init --mcp fluence .                        # sticky: keeps the previous --tools selection
```

`--tools` accepts `claude codex gemini copilot opencode crush agy grok pi omp cursor` (or `all`).
Claude is always deployed because its `.mcp.json` and skills feed the others. The selection is
stored in `.llm_settings/repo-tools`; deselecting a tool never deletes its existing files.

**One source of truth:** each tool's MCP file is *derived* from the final `.mcp.json` (after
`--mcp` filtering and `gmail-<alias>` rendering), so every tool always has the same servers.
Claude-only keys (`timeout`, `trust`) are dropped.

| Tool | Skills | Agents | MCP file | Schema notes |
|---|---|---|---|---|
| OpenCode | `.agents/skills` (also reads `.claude/skills`) | `.opencode/agents/` | `opencode.json` → `mcp` | `type: local`, `command` is an array incl. args, `environment`, `${VAR}`→`{env:VAR}`; other keys preserved |
| Crush | `.agents/skills` | — (none documented) | `.crush.json` → `mcp` | `type: stdio`, `command`, `args`, `env`, `${VAR}`→`$VAR`; sets `options.context_paths`; other keys preserved |
| Antigravity (`agy`) | `.agents/skills` | `.agents/agents/` | `.agents/plugins/llm-settings/mcp_config.json` → `mcpServers` (workspace plugin; agy ignores `.agents/mcp_config.json`; tools appear as `llm-settings_<server>`) | `command` (repo-relative made plugin-relative `../../../…`: agy starts plugin servers in the plugin folder), `args`, `env` |
| Grok Build | `.claude/skills` (native) | `.claude/agents` (native) | `.grok/config.toml` → `[mcp_servers.<n>]` | only the block between `# >>> llm-init mcp >>>` / `# <<< llm-init mcp <<<` is managed |
| Pi | `.agents/skills` | — (no sub-agents) | `.pi/mcp.json` → `mcpServers` | `.pi/` needs a one-time project trust prompt |
| Oh My Pi (`omp`) | `.agents/skills` (also `.claude/skills`) | `.omp/agents/` | `.omp/mcp.json` → `mcpServers` | |
| Cursor CLI (`cursor-agent`) | `.agents/skills` (also `.claude/skills`) | `.cursor/agents/` | `.cursor/mcp.json` → `mcpServers` | `${VAR}`→`${env:VAR}` |

All of them read `AGENTS.md`, which `llm-init` already syncs.

**Skills:** `.agents/skills/<name>/` is copied with the same profile filter as `.claude/skills`, with
the same folder names (see below). Directories other tools placed in `.agents/skills` are never removed.

**Known caveats (verify on first use):**
- Several tools also scan `.claude/skills` and require the folder to be named after the skill. Every
  managed skill is therefore deployed under its effective **name** (frontmatter `name`, else the source
  folder) in both `.claude/skills/<name>/` and `.agents/skills/<name>/` (`i-aws` → `aws`). Claude Code's
  commands are unchanged (it already uses the frontmatter name), the two trees are identical, and
  nothing is hidden. A name that is invalid or already taken falls back to the source folder with a
  warning. Legacy `.agents/skills/i-*` folders are removed on the next run; unmanaged skills are kept.
  Still possible: duplicates from user-level skills (`~/.claude/skills`, `~/.config/crush/skills`).
- MCP `command` paths are relative to the repo root (`.llm_settings/mcp-servers/...`); start each
  tool from the repo root.
- OpenCode agent frontmatter is minimal (`description`, `mode: subagent`); Crush's JSON config
  format is marked deprecated upstream in favor of `crushrc`.
- Pi and Grok ask you to trust project-level config/hooks once.

## Summary

- `.env` contains all OAuth preflight configuration
- Values come from:
  - GitHub Developer Settings
  - Atlassian Developer Console
  - Microsoft Entra App Registrations
- OAuth is validated **before** enabling MCP
- Secrets never enter the repository

If in doubt: **do not guess — ask IT or the app owner**.
