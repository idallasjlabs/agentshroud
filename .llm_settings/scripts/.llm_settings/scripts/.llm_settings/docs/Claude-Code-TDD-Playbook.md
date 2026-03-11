# Claude Code: Production-Ready TDD Workflow (Python + Next.js)
**Audience:** Engineering teams using Claude Code for refactors and new development  
**Focus:** TDD (Red → Green → Refactor), fast isolated unit tests, security, and durable documentation  
**Tooling:** Claude Code (Plan Mode, Skills, Subagents/Agents, MCP, Hooks, Plugins), GitHub + Jira + Confluence behind MS Entra (SSO)

---

## Summary (what to do first)
1. **Adopt the repo contract**: commit `CLAUDE.md` (authoritative rules for scope, TDD, security, data-lakehouse guardrails).
2. **Make Plan Mode default** in `.claude/settings.json` so Claude plans before edits.
3. **Enable hooks** in `.claude/settings.json` for safe automation (warn on risky bash, auto-format, fast tests).
4. **Keep personal preferences local** in `.claude/settings.local.json` (Vim mode + custom status line).
5. **Add subagents** in `.claude/agents/` (test runner, doc writer, security reviewer).
6. **Add skills** in `.claude/skills/` (`/tdd`, `/pr`, `/security-check`, etc.).
7. **Connect MCP** via `.mcp.json` (GitHub + Jira/Confluence), using OAuth flows that respect Entra-backed SSO.

---

## 1) Repo setup (what to commit vs ignore)

### Commit these (team-shared, reviewed in PRs)
- `CLAUDE.md` (project rules + workflows)
- `.claude/settings.json` (Plan Mode default, hook configuration, team-safe permissions)
- `.claude/agents/` (shared subagents)
- `.claude/skills/` (shared skills)
- `.mcp.json` (shared MCP integrations)

### Do NOT commit these (add to `.gitignore`)
- `.claude/settings.local.json` (local machine overrides)
- any tokens, PATs, cookies, or tool caches

> Tip: use the provided `scripts/claude_repo_setup.sh` (from this initiative) to stage the right files and update `.gitignore` safely.

---

## 2) The repo “constitution”: `CLAUDE.md`
Your `CLAUDE.md` should be treated as the authoritative operating contract for Claude-assisted development. It should include:
- Prime Directive (no new files/docs unless explicitly requested; no opportunistic refactors)
- Scope awareness (Data Lakehouse is primary; CTA is auxiliary)
- SDLC expectations + Definition of Done (DoD)
- TDD rules (Red → Green → Refactor) with test-quality constraints
- Security and safety requirements
- Claude Code operational rules (Plan Mode, subagents, skills, background tasks)
- Data platform guardrails (schema stability, partitioning, Athena compatibility, controlled reprocess)

✅ **Status:** implemented in your repo as a complete `CLAUDE.md`.

---

## 3) Team settings: `.claude/settings.json` (Plan Mode + hooks + permissions)

### Current team settings (implemented)
Your repo-level `.claude/settings.json` now includes:
- **Plan Mode default** (`permissions.defaultMode = "plan"`)
- **Model strategy** (`opusplan`)
- **Team-safe allowlist permissions** (including `ruff`, `black`, `pytest`)
- **Hooks**:
  - `PreToolUse`: warn on risky bash commands
  - `PostToolUse`: auto-format python (`ruff --fix`, `black`)
  - `PostToolUse`: run fast unit tests (`pytest -q`) on python changes

✅ **Status:** implemented.

**Current `.claude/settings.json` content:**
```json
{
  "permissions": {
    "defaultMode": "plan",
    "allow": [
      "Bash(chmod:*)",
      "Bash(python:*)",
      "Bash(python3:*)",
      "Bash(conda run:*)",
      "Bash(ruff:*)",
      "Bash(black:*)",
      "Bash(pytest:*)"
    ]
  },
  "model": "opusplan",
  "hooks": {
    "PreToolUse": [
      {
        "name": "warn-dangerous-bash",
        "command": "scripts/claude-hooks/warn_dangerous_bash.sh",
        "tools": ["Bash"]
      }
    ],
    "PostToolUse": [
      {
        "name": "auto-format-python",
        "command": "scripts/claude-hooks/auto_format_python.sh",
        "tools": ["Bash"]
      },
      {
        "name": "run-targeted-tests",
        "command": "scripts/claude-hooks/run_targeted_tests.sh",
        "tools": ["Bash"]
      }
    ]
  }
}
```

### Hook scripts (implemented)
These are referenced by the settings above:
- `scripts/claude-hooks/warn_dangerous_bash.sh`
- `scripts/claude-hooks/auto_format_python.sh`
- `scripts/claude-hooks/run_targeted_tests.sh`

---

## 4) Personal settings: `.claude/settings.local.json` (Vim + status line)

### Current personal settings (implemented)
Your local-only settings include:
- **Vim mode default** (editor.vim = true)
- **Custom status line** (powerlevel10k-style) via a local script (`~/.claude/statusline.sh`)
- Local-only allowlist permissions (optional; can be minimal if team settings cover it)

✅ **Status:** implemented.

**Example `.claude/settings.local.json`:**
```json
{
  "permissions": {
    "allow": [
      "Bash(chmod:*)",
      "Bash(python:*)",
      "Bash(python3:*)",
      "Bash(conda run:*)"
    ]
  },
  "editor": {
    "vim": true
  },
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0
  }
}
```

**Status line script:** `~/.claude/statusline.sh` reads JSON context from stdin, then prints a compact line containing:
- git branch + dirty marker
- conda env
- repo/current dir
- model
- context usage %
- cost

---

## 5) TDD workflow (the default loop)

### Red → Green → Refactor (strict)
1. **Red**: smallest failing test capturing intended behavior.
2. **Green**: minimal implementation to pass.
3. **Refactor**: improve structure with tests staying green.

### “High-speed unit tests” requirements
- No real network
- No real AWS
- No real DB
- No time-based sleeps

### Data lakehouse supplement
For pipeline changes, do BOTH:
- unit tests (transform logic)
- data validation (schema/partition correctness)

---

## 6) Subagents (agents) and skills (recommended team additions)

### Suggested subagents
Add as Markdown files in `.claude/agents/`:
- `test-runner` (runs tests and reports only failures)
- `doc-writer` (updates docs / Confluence-ready release notes when explicitly requested)
- `security-reviewer` (flags common risk classes and suggests tests)

### Suggested skills
Add skills in `.claude/skills/<name>/SKILL.md`:
- `/tdd` (enforce Red-Green-Refactor)
- `/pr` (generate PR description: summary, risk, how tested, rollback)
- `/security-check` (authz/injection/secrets/logging checklist)
- `/pipeline-check` (schema drift, partitions, Athena compatibility checklist)

---

## 7) MCP (GitHub + Jira + Confluence behind Entra SSO)

You said you want to configure MCP later because your IT department may block OAuth and you’ve had trouble before. That’s a smart sequencing choice.

This section is written so you can:
1) **Preflight-test** whether OAuth / browser-based auth flows will work in your environment *before* you change any Claude configuration.
2) **Collect the correct MCP server URLs** from authoritative sources (vendor docs / IT admins).
3) Choose between (A) vendor MCP servers or (B) an internal MCP gateway pattern if policy blocks direct OAuth.

---

### 7.1 What MCP configuration needs (and why OAuth matters)
To connect Claude Code to systems like GitHub and Jira/Confluence, you generally need:

- An **MCP server URL** (HTTP endpoint)
- An **auth method** (often OAuth via browser)
- A **policy decision**: are direct vendor OAuth apps allowed from developer machines?

If OAuth is blocked or restricted (common in enterprise SSO setups), you’ll usually see:
- Browser auth page fails to load (blocked domains)
- SSO completes but token exchange fails
- OAuth app approvals/scopes blocked at org level
- Corporate proxy / TLS interception breaks the flow

---

### 7.2 Preflight: test OAuth reachability BEFORE changing config
Run this preflight from the same machine/network where you use Claude Code.

#### A) Use the provided script (recommended)
This playbook includes a Python preflight checker:

- `mcp_oauth_preflight.py`

It validates:
- DNS resolution
- TLS handshake
- HTTPS status codes + redirect chains
- Whether your environment can reach the candidate MCP endpoints

It does **not** authenticate or request tokens (so it’s safe to run without changing anything).

**How to run:**
```bash
python3 mcp_oauth_preflight.py \
  --url "https://mcp.atlassian.com/v1/mcp" \
  --url "https://api.github.com" \
  --url "https://github.com/login" \
  --url "https://login.microsoftonline.com"
```

If your org uses a proxy, use:
```bash
python3 mcp_oauth_preflight.py --use-env-proxy --url "https://mcp.atlassian.com/v1/mcp"
```

**How to interpret results:**
- ✅ **200/204/401/403** can still be OK (reachable; auth may be required).
- ⚠️ **302/307** is normal (redirect to SSO).
- ❌ DNS failures, TLS failures, or timeouts are strong evidence IT/proxy blocks access.

#### B) Optional: quick CLI checks
```bash
curl -I https://mcp.atlassian.com/v1/mcp
curl -I https://github.com/login
curl -I https://login.microsoftonline.com
```

---

### 7.3 Where to get the MCP server URLs you need
There are three common cases. Your IT policy determines which one applies.

#### Case 1: Vendor-hosted MCP servers (simplest)
You get the URL from:
- Official vendor documentation (Atlassian / GitHub)
- Your internal platform/security team’s approved integrations list

**Atlassian (Jira/Confluence Cloud):**
- Atlassian provides a “Rovo MCP” endpoint in their docs. Many orgs use a URL of the form:
  - `https://mcp.atlassian.com/v1/mcp`
**BUT:** do not assume — confirm with Atlassian docs or your admins.

**GitHub:**
- GitHub MCP might be:
  - a vendor endpoint (for GitHub.com), or
  - an internal endpoint if you run GitHub Enterprise Server, or
  - a self-hosted/community MCP server approved by IT.
Ask your GitHub org admins which MCP server is approved and what URL to use.

#### Case 2: Managed MCP configuration (IT-controlled)
If IT wants strict governance, they may deploy a managed MCP configuration file
(e.g., `managed-mcp.json`) and disallow per-repo MCP servers.

In this case, the URLs come from IT, not from developers.

#### Case 3: Internal “MCP Gateway” (enterprise pattern)
If direct OAuth / vendor endpoints are blocked:
- Your org can host an **internal MCP gateway**.
- The gateway authenticates users with **Microsoft Entra**.
- The gateway calls GitHub/Jira/Confluence APIs using **approved app credentials**
  with minimal scopes and strong audit logs.

In this case, the URL you configure is your internal gateway, e.g.:
- `https://mcp-gateway.<company>.com`

---

### 7.4 Recommended rollout plan (low risk)
1) Run the preflight script against:
   - candidate MCP endpoints (vendor or internal)
   - Microsoft login endpoints
2) If reachability looks good, do a “dry run” in a throwaway repo:
   - add MCP config there first
3) Only then commit `.mcp.json` into production repos

---

### 7.5 If OAuth is blocked: what to ask IT for
If preflight fails, send IT a short request:

- “We need outbound HTTPS access to these domains for Claude Code MCP OAuth flows”
- Provide:
  - the list of URLs/domains that failed
  - the error mode (DNS/TLS/timeout/blocked)
- Ask whether:
  - OAuth apps are allowed for GitHub/Atlassian
  - SSO device/browser flows are allowed
  - TLS interception is in place (and whether it breaks cert validation)
  - A corporate proxy must be configured via environment variables

---

### 7.6 When you’re ready to actually configure MCP
When preflight is green and you have approved URLs from IT/vendor docs:
- Add them in `.mcp.json` (repo) OR user settings (personal).
- Authenticate using the in-tool flow (usually browser OAuth).
- Validate by performing a read-only action (list repos, fetch a Jira issue, read a Confluence page).

(We’ll do this step together later, once your IT constraints are known.)


## 8) Hooks: why we started with “warn” hooks
Hooks are powerful. Start with **warnings** before enforcing blocks to avoid interrupting developer flow.
- Current state: warn on risky bash; do not block.
- Next state (optional): block or require explicit confirmation for certain patterns.

---

## 9) Future hardening steps (for later)
When you’re ready, the natural next upgrades are:

1. 🔒 **Convert dangerous-command warnings → blocks**
2. 🧩 **Add schema / Parquet validation hooks**
3. 🧼 **Add Next.js hooks** (prettier, vitest)
4. 🔐 **Add security hooks** (bandit, trivy, pip-audit)
5. 📊 **Add coverage gate** for new code only

---

## Appendix A: Recommended repo structure
```
.
├─ CLAUDE.md
├─ .mcp.json
└─ .claude/
   ├─ settings.json
   ├─ agents/
   └─ skills/
```

---

## Appendix B: Quick “How we work with Claude” checklist (team)
- Always start with a plan (Plan Mode default)
- Tests first (TDD)
- Keep tests fast and isolated
- Run formatters + unit tests frequently (hooks help)
- Keep changes minimal and scoped
- Always summarize: what changed, how tested, risks, rollback

