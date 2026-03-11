# AI Tools Configuration Guide
## Multi-Agent Development Setup - Properly Configured

**Last Updated:** 2026-01-25

---

## ⚠️ CRITICAL: Different Tools, Different Capabilities

**This repository uses FOUR different AI coding tools, each with DIFFERENT configuration formats and capabilities.**

DO NOT assume they all work the same way! Each tool has been configured according to its native format and feature set.

---

## Tool Comparison Matrix

| Feature | Claude Code | Gemini CLI | Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------|-----------|-------------------|
| **Config Format** | JSON | JSON | **TOML** | JSON |
| **Config Location** | `.claude/settings.json` | `.gemini/settings.json` | `.codex/config.toml` | `~/.copilot/config.json` |
| **Context File** | `CLAUDE.md` | `GEMINI.md` | `AGENTS.md` | Custom agents in `.github/agents/` |
| **Custom Agents** | ✅ Yes (subagents) | ❌ No | ❌ No | ✅ Yes (.agent.md files) |
| **Skills System** | ✅ Yes (`/skill`) | ❌ No | ❌ No | ❌ No |
| **Hooks System** | ✅ Yes (Pre/Post) | ❌ No | ❌ No | ❌ No |
| **MCP Servers** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Sandbox Mode** | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Limited (path-based) |
| **Approval Policy** | ✅ Yes | ⚠️ Limited | ✅ Yes | ✅ Yes (tool-based) |
| **Feature Flags** | ❌ No | ❌ No | ✅ Yes | ❌ No |
| **URL Access Control** | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| **Built-in Agents** | ❌ No | ❌ No | ❌ No | ✅ Yes (Explore, Task, Plan, Code-review) |

---

## 1. Claude Code (PRIMARY Developer)

### Overview
Claude Code is the **PRIMARY developer** in this repository. It has the most advanced configuration system with agents, skills, and hooks.

### Configuration Files

```
.claude/
├── agents/                    # Subagent definitions (doc-writer, security-reviewer, testrunner)
│   ├── doc-writer.md
│   ├── security-reviewer.md
│   └── testrunner.md
├── scripts/
│   ├── claude_repo_setup.sh
│   └── claude-hooks/         # Hook scripts (bash)
│       ├── warn_dangerous_bash.sh
│       ├── auto_format_python.sh
│       └── run_targeted_tests.sh
├── skills/                    # Skill definitions (workflows)
│   ├── pr/SKILL.md           # /pr command - PR descriptions
│   ├── tdd/SKILL.md          # /tdd command - TDD workflow
│   ├── mcpm-aws-profile/SKILL.md  # /mcpm-aws-profile - AWS MCP setup
│   ├── mcpm-doctor/SKILL.md       # /mcpm-doctor - Diagnose MCP issues
│   └── mcpm-auth-reset/SKILL.md   # /mcpm-auth-reset - Reset MCP auth
├── settings.json             # Team-shared configuration
├── settings.local.json       # Personal overrides (gitignored)
└── statusline.sh            # Custom status line

CLAUDE.md                     # Context file in project root
.mcp.json                     # MCP servers configuration
```

### Configuration Format

**File:** `.claude/settings.json` (JSON format)

```json
{
  "permissions": {
    "defaultMode": "plan",
    "allow": [
      "Bash(chmod:*)",
      "Bash(python:*)",
      "Bash(pytest:*)"
    ]
  },
  "model": "opusplan",
  "hooks": {
    "PreToolUse": [{
      "matcher": "tools:BashTool",
      "hooks": [{
        "type": "command",
        "command": ".claude/scripts/claude-hooks/warn_dangerous_bash.sh"
      }]
    }]
  }
}
```

### Unique Features

- **Agents**: Specialized subagents for documentation, security, testing
- **Skills**: Custom workflows invoked with `/skill-name`
- **Hooks**: PreToolUse, PostToolUse, SessionStart scripts
- **Context file**: `CLAUDE.md` loaded automatically
- **Local overrides**: `settings.local.json` for personal settings

### Role in Multi-Agent System
- ✅ Makes architectural decisions
- ✅ Implements features
- ✅ Handles refactoring
- ✅ Creates documentation
- ✅ Manages PRs and commits

### Documentation
- [Official Docs](https://code.claude.com/docs/en/settings)
- [Settings Reference](https://www.eesel.ai/blog/settings-json-claude-code)
- [Hooks Mastery](https://github.com/disler/claude-code-hooks-mastery)

---

## 2. Gemini CLI (SECONDARY Agent)

### Overview
Gemini CLI is a **SECONDARY agent** focused on test augmentation and validation. It does NOT have Claude's agents/skills/hooks system.

### Configuration Files

```
.gemini/
├── settings.json             # Gemini-specific configuration (JSON)
└── GEMINI.md                 # Context file for role definition

(NO agents/, skills/, or scripts/ directories - Gemini doesn't support these!)
```

### Configuration Format

**File:** `.gemini/settings.json` (JSON format)

```json
{
  "auth": {
    "selectedType": "USE_API_KEY"
  },
  "memory": {
    "refreshIncludeDirectories": false
  },
  "sandbox": {
    "enabled": true
  },
  "mcpServers": {
    "example": {
      "command": "node",
      "args": ["/path/to/server.js"],
      "enabled": false
    }
  }
}
```

### What Gemini CLI CAN Do
- ✅ Load `GEMINI.md` for context via `/memory refresh`
- ✅ Configure MCP servers
- ✅ Use sandbox execution
- ✅ Run commands and scripts
- ✅ Read and modify files

### What Gemini CLI CANNOT Do
- ❌ Use Claude-style agents (no `.gemini/agents/` support)
- ❌ Use Claude-style skills (no `/skill` commands)
- ❌ Use Claude-style hooks (no PreToolUse/PostToolUse)
- ❌ Load `.claude/` configurations

### Role in Multi-Agent System
- ✅ Test augmentation (add missing tests)
- ✅ Validation runs (execute commands, report results)
- ✅ Safe refactors (small, local changes only)
- ❌ Cannot make architectural decisions
- ❌ Cannot implement features
- ❌ Cannot create documentation (unless requested)

### How to Configure

1. **Set up authentication:**
   ```bash
   # Create or edit ~/.gemini/settings.json
   # OR use project-level .gemini/settings.json
   ```

2. **Add API key to .env:**
   ```bash
   GOOGLE_API_KEY=your_key_here
   ```

3. **Context file:**
   - `GEMINI.md` in project root defines role and responsibilities
   - Loaded via `/memory refresh` command

### Documentation
- [GitHub Repo](https://github.com/google-gemini/gemini-cli)
- [Configuration Guide](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html)
- [Tutorial Series](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-3-configuration-settings-via-settings-json-and-env-files-669c6ab6fd44)

---

## 3. Codex CLI (TERTIARY Agent)

### Overview
Codex CLI is a **TERTIARY agent** focused on test augmentation and validation. It uses **TOML format** (not JSON!) and does NOT have Claude's agents/skills/hooks system.

### Configuration Files

```
.codex/
└── config.toml               # Codex-specific configuration (TOML format!)

AGENTS.md                     # Context file in project root (referenced by config.toml)

(NO agents/, skills/, or scripts/ directories - Codex doesn't support these!)
```

### Configuration Format

**File:** `.codex/config.toml` (**TOML format, NOT JSON!**)

```toml
# Codex CLI Configuration

# Project context file
model_instructions_file = "AGENTS.md"

# Security settings
sandbox_mode = "workspace-write"
approval_policy = "on-request"

# Project identification
project_root_markers = [".git", ".codex"]

# Environment policy
[shell_environment_policy]
include = ["PATH", "HOME", "USER"]
exclude = ["*TOKEN*", "*SECRET*", "*KEY*"]

# Feature flags
[features]
shell_snapshot = true
web_search_request = false

# MCP servers
[mcp_servers.example]
command = "node"
args = ["/path/to/server.js"]
```

### What Codex CLI CAN Do
- ✅ Load `AGENTS.md` for context (via `model_instructions_file`)
- ✅ Configure MCP servers (in config.toml)
- ✅ Use sandbox modes (read-only, workspace-write, full-access)
- ✅ Approval policies (always, on-request, never)
- ✅ Feature flags (experimental capabilities)
- ✅ Environment variable policies

### What Codex CLI CANNOT Do
- ❌ Use Claude-style agents (no `.codex/agents/` support)
- ❌ Use Claude-style skills (no `/skill` commands)
- ❌ Use Claude-style hooks (no PreToolUse/PostToolUse)
- ❌ Load `.claude/` configurations
- ❌ Use JSON format (must use TOML!)

### Role in Multi-Agent System
- ✅ Test augmentation (add missing tests)
- ✅ Validation runs (execute commands, report results)
- ✅ Safe refactors (small, local changes only)
- ❌ Cannot make architectural decisions
- ❌ Cannot implement features
- ❌ Cannot create documentation (unless requested)

### How to Configure

1. **Create config.toml:**
   ```bash
   # Project-level: .codex/config.toml
   # User-level: ~/.codex/config.toml
   ```

2. **Set context file:**
   ```toml
   model_instructions_file = "AGENTS.md"
   ```

3. **Configure sandbox:**
   ```toml
   sandbox_mode = "workspace-write"
   approval_policy = "on-request"
   ```

### Documentation
- [Official Docs](https://developers.openai.com/codex/cli/)
- [Configuration Reference](https://developers.openai.com/codex/config-reference/)
- [Quickstart Guide](https://developers.openai.com/codex/quickstart/)
- [GitHub Repo](https://github.com/openai/codex)

---

## Multi-Agent Hierarchy

### PRIMARY Developer: Claude Code
- **Configuration:** `.claude/` + `CLAUDE.md`
- **Capabilities:** Full development, agents, skills, hooks
- **Role:** Architectural decisions, feature implementation, refactoring

### SECONDARY Agent: Gemini CLI
- **Configuration:** `.gemini/` + `GEMINI.md`
- **Capabilities:** Basic CLI, MCP servers, sandbox
- **Role:** Test augmentation, validation, safe refactors

### TERTIARY Agent: Codex CLI
- **Configuration:** `.codex/config.toml` + `AGENTS.md`
- **Capabilities:** TOML config, MCP servers, feature flags, sandbox
- **Role:** Test augmentation, validation, safe refactors

### QUATERNARY Agent: GitHub Copilot CLI
- **Configuration:** `.github/agents/` + `~/.copilot/config.json`
- **Capabilities:** Custom agents (agent profiles), MCP servers, URL access control, built-in agents
- **Role:** Test augmentation, validation, safe refactors

---

## 4. GitHub Copilot CLI (QUATERNARY Agent)

### Overview
GitHub Copilot CLI is a **QUATERNARY agent** focused on test augmentation, validation, and safe refactors. It uses **custom agent profiles** (.agent.md files) stored in `.github/agents/`.

### Configuration Files

```
.github/
├── agents/                         # Custom agent profiles
│   ├── test-augmenter.agent.md    # Test coverage specialist
│   ├── validation-runner.agent.md  # Validation execution specialist
│   └── safe-refactor.agent.md     # Safe refactoring specialist
├── copilot-config.json.example    # Config template
└── COPILOT_CLI_SETUP.md           # Setup guide

~/.copilot/                         # User-level configuration (not in repo)
├── config.json                     # Main configuration
└── mcp-config.json                # MCP servers
```

### Configuration Format

**File:** `~/.copilot/config.json` (JSON format)

```json
{
  "banner": "always",
  "trusted_folders": [
    "/Users/username/Development/LLM_Settings"
  ],
  "allowed_urls": [
    "https://api.github.com/*",
    "https://docs.github.com/*"
  ],
  "denied_urls": [
    "http://*"
  ]
}
```

### Agent Profile Format

**File:** `.github/agents/name.agent.md` (Markdown with YAML frontmatter)

```markdown
---
name: test-augmenter
description: Specialized agent for adding test coverage and edge cases
tools: ['read', 'search', 'edit', 'bash']
---

# Agent instructions here

Role definition, responsibilities, restrictions, examples...
```

### Custom Agents Included

**1. test-augmenter** (`.github/agents/test-augmenter.agent.md`)
- Purpose: Add test coverage, identify edge cases
- Tools: read, search, edit, bash
- Focus: ≥80% coverage, deterministic tests

**2. validation-runner** (`.github/agents/validation-runner.agent.md`)
- Purpose: Execute validation scripts, report results
- Tools: read, bash, search
- Focus: pytest, ruff, black, mypy execution

**3. safe-refactor** (`.github/agents/safe-refactor.agent.md`)
- Purpose: Safe local refactorings ONLY after tests pass
- Tools: read, search, edit, bash
- Focus: Variable naming, extract helpers, remove duplication

### What GitHub Copilot CLI CAN Do
- ✅ Load custom agent profiles from `.github/agents/`
- ✅ Use built-in agents (Explore, Task, Plan, Code-review)
- ✅ Configure MCP servers
- ✅ URL access control (allowed/denied patterns)
- ✅ Path-based permissions (trusted folders)
- ✅ Tool-based approval (`--allow-tool`)
- ✅ Model selection (Claude Sonnet 4.5, GPT-5)
- ✅ Auto-compaction of conversation history

### What GitHub Copilot CLI CANNOT Do
- ❌ Use Claude-style hooks (no PreToolUse/PostToolUse)
- ❌ Use Claude-style skills (no `/skill` commands)
- ❌ Use Claude-style subagents (different agent system)
- ❌ Use Codex-style TOML config
- ❌ Use feature flags (like Codex)

### Role in Multi-Agent System
- ✅ Test augmentation (add missing tests)
- ✅ Validation runs (execute commands, report results)
- ✅ Safe refactors (small, local changes only)
- ❌ Cannot make architectural decisions
- ❌ Cannot implement features
- ❌ Cannot create documentation (unless requested)

### How to Configure

1. **Install:**
   ```bash
   # macOS/Linux
   brew install copilot-cli

   # Windows
   winget install GitHub.Copilot

   # npm
   npm install -g @github/copilot
   ```

2. **Authenticate:**
   ```bash
   copilot
   # Follow prompts
   ```

3. **Create config:**
   ```bash
   mkdir -p ~/.copilot
   cp .github/copilot-config.json.example ~/.copilot/config.json
   ```

4. **Use custom agents:**
   ```bash
   # Interactive
   copilot
   /agent test-augmenter

   # Command-line
   copilot --agent=test-augmenter --prompt "Add tests for module X"
   ```

### Built-in Agents

| Agent | Purpose |
|-------|---------|
| **Explore** | Fast codebase analysis without cluttering main context |
| **Task** | Execute commands like tests and builds |
| **Plan** | Create implementation plans |
| **Code-review** | Review changes for genuine issues |

### Context Management

- **Auto-compaction**: At 95% token limit
- **Manual controls**:
  - `/usage` - View session statistics
  - `/context` - Visual token usage
  - `/compact` - Manually compress history

### Documentation
- [GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Creating Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [GitHub Copilot CLI Changelog](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)

---

## Common Mistakes to Avoid

### ❌ DON'T: Copy Claude's configuration to other tools
```bash
# WRONG - This doesn't work!
cp -r .claude/agents .gemini/
cp -r .claude/skills .gemini/
```

Gemini and Codex do NOT support Claude's agents/skills/hooks system!

### ❌ DON'T: Use JSON for Codex
```bash
# WRONG - Codex uses TOML, not JSON!
.codex/settings.json
```

Codex requires `config.toml` in TOML format!

### ❌ DON'T: Expect feature parity
Claude's `/tdd` skill → ❌ Not available in Gemini/Codex/Copilot
Claude's hooks → ❌ Not available in Gemini/Codex/Copilot
Claude's subagents → ⚠️ Different in Copilot (custom agent profiles)

### ❌ DON'T: Confuse agent systems
GitHub Copilot's agent profiles (.agent.md) ≠ Claude's subagents (.md with YAML)
They have similar names but different purposes and formats!

### ✅ DO: Configure each tool natively
- Claude → `.claude/settings.json` + agents + skills + hooks
- Gemini → `.gemini/settings.json` + `GEMINI.md`
- Codex → `.codex/config.toml` + `AGENTS.md`
- GitHub Copilot → `.github/agents/*.agent.md` + `~/.copilot/config.json`

### ✅ DO: Use context files for role definition
- Claude: `CLAUDE.md` defines primary developer role
- Gemini: `GEMINI.md` defines secondary agent role
- Codex: `AGENTS.md` defines tertiary agent role
- GitHub Copilot: Custom agent profiles in `.github/agents/` define quaternary roles

---

## Verification Steps

### Test Claude Code (PRIMARY)
```bash
claude                       # Start Claude Code
# Verify CLAUDE.md is loaded
# Test /tdd skill
# Test /pr skill
# Verify hooks run on Python changes
```

### Test Gemini CLI (SECONDARY)
```bash
gemini                       # Start Gemini CLI
/memory refresh             # Load GEMINI.md context
# Verify secondary role is understood
# Test augmentation workflow
```

### Test Codex CLI (TERTIARY)
```bash
codex                        # Start Codex CLI
# Verify AGENTS.md is loaded as context
# Verify tertiary role is understood
# Test validation workflow
```

### Test GitHub Copilot CLI (QUATERNARY)
```bash
copilot                      # Start GitHub Copilot CLI
/agent                       # List available agents
/agent test-augmenter        # Load test-augmenter agent
# Verify custom agents are loaded
# Verify quaternary role is understood
# Test augmentation workflow
```

---

## Environment Setup

### Required Tools
- Claude Code CLI ([install](https://claude.ai/code))
- Gemini CLI ([install](https://github.com/google-gemini/gemini-cli))
- Codex CLI ([install](https://developers.openai.com/codex/quickstart/))
- GitHub Copilot CLI ([install](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli))

### API Keys
```bash
# .env file (gitignored!)
GOOGLE_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key
# Claude uses claude.ai authentication
# GitHub Copilot uses GitHub authentication (gh auth login)
```

### MCP Servers
- Atlassian MCP: ✅ Working
- GitHub MCP: ✅ Working
- AWS API MCP: ✅ Working (requires `uv` installation)

See `MCP_README.md` for OAuth setup and `MCP_ADDITIONAL_SERVICES.md` for AWS details.

---

## MCP Server Integration

### Configured MCP Servers

All AI tools in this repository have access to three MCP servers:

| MCP Server | Purpose | Auth Method |
|------------|---------|-------------|
| **GitHub** | Repos, PRs, issues, code search | OAuth / Token |
| **Atlassian** | Jira issues, Confluence pages | OAuth 2.0 (3LO) |
| **AWS API** | All AWS CLI commands (readonly by default) | AWS credentials |

### AWS MCP Server Setup

**Prerequisites:**
```bash
# Install UV package manager (macOS)
brew install uv
hash -r
which uvx  # Should show /opt/homebrew/bin/uvx
uvx --version
```

**Configuration (in `.mcp.json`):**
```json
{
  "mcpServers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": ["awslabs.aws-api-mcp-server@latest", "--readonly"],
      "env": {
        "AWS_PROFILE": "${AWS_PROFILE:-default}",
        "AWS_REGION": "${AWS_REGION:-us-east-1}"
      }
    }
  }
}
```

**Environment Variables:**
```bash
export AWS_PROFILE=default
export AWS_REGION=us-east-1
```

### Claude Code MCP Skills

Claude Code includes skills for managing MCP servers:

| Skill | Command | Purpose |
|-------|---------|---------|
| AWS MCP Profile | `/mcpm-aws-profile` | Configure AWS profile for MCP |
| MCP Doctor | `/mcpm-doctor` | Diagnose MCP connection issues |
| MCP Auth Reset | `/mcpm-auth-reset` | Reset and re-authenticate MCP |

See `MCP_README.md` for complete setup instructions and `MCP_ADDITIONAL_SERVICES.md` for AWS API MCP server details.

---

## References

### Claude Code
- [Claude Code settings - Claude Code Docs](https://code.claude.com/docs/en/settings)
- [A developer's guide to settings.json in Claude Code (2025)](https://www.eesel.ai/blog/settings-json-claude-code)
- [GitHub - ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase)

### Gemini CLI
- [Gemini CLI Configuration | gemini-cli](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html)
- [GitHub - google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Tutorial Series — Part 3](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-3-configuration-settings-via-settings-json-and-env-files-669c6ab6fd44)

### Codex CLI
- [Codex CLI](https://developers.openai.com/codex/cli/)
- [Configuration Reference](https://developers.openai.com/codex/config-reference/)
- [GitHub - openai/codex](https://github.com/openai/codex)

### GitHub Copilot CLI
- [GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Creating Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [GitHub Copilot CLI Changelog (Jan 2026)](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)
- [Install Guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli)
- [GitHub - github/copilot-cli](https://github.com/github/copilot-cli)

---

## Questions?

- **Claude Code issues:** See `CLAUDE.md`
- **Gemini CLI issues:** See `GEMINI.md`
- **Codex CLI issues:** See `AGENTS.md`
- **GitHub Copilot CLI issues:** See `.github/COPILOT_CLI_SETUP.md`
- **Multi-agent setup:** See this file (`AI_TOOLS_CONFIGURATION_GUIDE.md`)
- **MCP integration:** See `MCP_README.md`
- **Team announcement:** See `TEAMS_MESSAGE.md`
