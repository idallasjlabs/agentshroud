# AI Tools Configuration Summary

**Repository:** LLM_Settings
**Last Updated:** 2026-01-29
**Status:** ✅ Fully Configured

---

## Quick Reference

| Tool | Role | Config Location | Context File | Status |
|------|------|-----------------|--------------|---------|
| **Claude Code** | PRIMARY | `.claude/` | `CLAUDE.md` | ✅ Complete |
| **Gemini CLI** | SECONDARY | `.gemini/` | `GEMINI.md` | ✅ Complete |
| **Codex CLI** | TERTIARY | `.codex/` | `AGENTS.md` | ✅ Complete |
| **GitHub Copilot CLI** | QUATERNARY | `.github/agents/` | Agent profiles | ✅ Complete |

---

## Configuration Structure

```
LLM_Settings/
│
├── .claude/                          # Claude Code (PRIMARY)
│   ├── agents/                       # Subagents (doc-writer, security, tests)
│   ├── scripts/claude-hooks/         # Pre/Post hooks
│   ├── skills/                       # /pr, /tdd, /mcpm-aws-profile, /mcpm-doctor, /mcpm-auth-reset
│   ├── settings.json                 # Team config
│   ├── settings.local.json           # Personal overrides
│   └── statusline.sh                # Custom status line
│
├── .gemini/                          # Gemini CLI (SECONDARY)
│   ├── GEMINI.md                    # Context file (role definition)
│   └── settings.json                 # Gemini config + MCP servers
│
├── .codex/                           # Codex CLI (TERTIARY)
│   ├── AGENTS.md                    # Context file (role definition)
│   └── config.toml                   # TOML config + MCP servers
│
├── .github/                          # GitHub Copilot CLI (QUATERNARY)
│   ├── agents/                       # Custom agent profiles
│   │   ├── test-augmenter.agent.md
│   │   ├── validation-runner.agent.md
│   │   └── safe-refactor.agent.md
│   ├── COPILOT_CLI_SETUP.md         # Setup guide
│   └── copilot-config.json.example  # Config template
│
├── CLAUDE.md                         # Claude Code instructions (PRIMARY)
├── GEMINI.md                         # Gemini CLI instructions (SECONDARY)
├── AGENTS.md                         # Codex CLI instructions (TERTIARY)
│
├── AI_TOOLS_CONFIGURATION_GUIDE.md  # Complete configuration guide
├── CONFIGURATION_SUMMARY.md         # This file
├── TEAMS_MESSAGE.md                 # Team announcement
├── MCP_README.md                    # MCP OAuth setup
└── .mcp.json                        # MCP servers config
```

---

## Role Hierarchy

### PRIMARY: Claude Code
**Responsibilities:**
- ✅ Architectural decisions
- ✅ Feature implementation
- ✅ Complex refactors
- ✅ Documentation creation
- ✅ Pull requests and commits

**Unique Capabilities:**
- Subagents system (doc-writer, security-reviewer, testrunner)
- Skills system (/pr, /tdd)
- Hooks system (PreToolUse, PostToolUse)
- Most advanced configuration

### SECONDARY: Gemini CLI
**Responsibilities:**
- ✅ Test augmentation
- ✅ Validation runs
- ✅ Safe local refactors (after tests pass)

**Restrictions:**
- ❌ No architectural decisions
- ❌ No feature implementation
- ❌ No large refactors
- ❌ No documentation (unless requested)

### TERTIARY: Codex CLI
**Responsibilities:**
- ✅ Test augmentation
- ✅ Validation runs
- ✅ Safe local refactors (after tests pass)

**Restrictions:**
- ❌ No architectural decisions
- ❌ No feature implementation
- ❌ No large refactors
- ❌ No documentation (unless requested)

### QUATERNARY: GitHub Copilot CLI
**Responsibilities:**
- ✅ Test augmentation (test-augmenter agent)
- ✅ Validation runs (validation-runner agent)
- ✅ Safe local refactors (safe-refactor agent)

**Restrictions:**
- ❌ No architectural decisions
- ❌ No feature implementation
- ❌ No large refactors
- ❌ No documentation (unless requested)

---

## Configuration Highlights

### Claude Code ('.claude/')
- **Format:** JSON
- **Agents:** Subagents (doc-writer, security-reviewer, testrunner)
- **Skills:** 36 skills (`/8d`, `/aws`, `/browser`, `/bs`, `/cicd`, `/cr`, `/data`, `/env`, `/gg`, `/icloud`, `/mac`, `/mc`, `/mcpm`, `/mcpm-auth-reset`, `/mcpm-aws-profile`, `/mcpm-doctor`, `/mm`, `/pm`, `/pr`, `/production`, `/ps`, `/qa`, `/sec`, `/sec-defense`, `/sec-offense`, `/tdd`, `/ti`, `/tw`, plus 9 podcast pipeline skills)
- **Hooks:** 3 hooks (warn_dangerous_bash, auto_format_python, run_targeted_tests)
- **Context:** CLAUDE.md loaded automatically
- **MCP:** Via .mcp.json (GitHub, Atlassian, AWS API, XMind Generator)

### Gemini CLI ('.gemini/')
- **Format:** JSON
- **Agents:** 38 reference files in `.gemini/agents/` — paste content to use (no native invocation)
- **Skills:** No native support
- **Hooks:** None (not supported)
- **Context:** GEMINI.md loaded via /memory refresh
- **MCP:** Via settings.json

### Codex CLI ('.codex/')
- **Format:** TOML
- **Agents:** 38 reference files in `.codex/agents/` — paste content to use (no native invocation)
- **Skills:** No native support (`/skills` not a Codex feature)
- **Hooks:** None (not supported)
- **Context:** AGENTS.md loaded via model_instructions_file
- **MCP:** Via config.toml (aws-api server, github, atlassian)
- **Features:** Feature flags enabled (shell_snapshot, web_search=disabled)

### GitHub Copilot CLI ('.github/agents/')
- **Format:** JSON (config) + Markdown (agent profiles)
- **Custom Agents:** 3 agent profiles (test-augmenter, validation-runner, safe-refactor)
- **Built-in Agents:** Explore, Task, Plan, Code-review
- **Skills:** None (not supported)
- **Hooks:** None (not supported)
- **Context:** Agent profiles loaded from .github/agents/
- **MCP:** Via ~/.copilot/mcp-config.json
- **URL Control:** allowed_urls / denied_urls in config.json

---

## Key Differences Between Tools

| Feature | Claude | Gemini | Codex | Copilot |
|---------|--------|--------|-------|---------|
| **Config Format** | JSON | JSON | TOML | JSON |
| **Custom Agents** | Subagents (MD) | Library only (paste to use) | Library only (paste to use) | Agent profiles (.agent.md) |
| **Skills** | ✅ /skill | ❌ (no native syntax) | ❌ (no native syntax) | ❌ |
| **Hooks** | ✅ Pre/Post | ❌ | ❌ | ❌ |
| **Context File** | Auto-load | Manual refresh | Auto-load | Agent profiles |
| **MCP Servers** | ✅ | ✅ | ✅ | ✅ |
| **Feature Flags** | ❌ | ❌ | ✅ | ❌ |
| **URL Control** | ✅ | ❌ | ❌ | ✅ |

---

## Documentation Files

| File | Purpose |
|------|---------|
| `AI_TOOLS_CONFIGURATION_GUIDE.md` | Complete guide to all four tools |
| `CLAUDE.md` | Claude Code instructions (PRIMARY role) |
| `GEMINI.md` | Gemini CLI instructions (SECONDARY role) |
| `AGENTS.md` | Codex CLI instructions (TERTIARY role) |
| `.github/COPILOT_CLI_SETUP.md` | GitHub Copilot CLI setup guide |
| `.github/copilot-config.json.example` | Copilot config template |
| `.llm_settings/docs/MCP_README.md` | MCP OAuth setup (Atlassian, GitHub) |
| `.llm_settings/docs/CONFIGURATION_SUMMARY.md` | This file - quick reference |

---

## Installation

### Claude Code
```bash
# Visit https://claude.ai/code for installation instructions
```

### Gemini CLI
```bash
# Install from GitHub
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
npm install -g .
```

### Codex CLI
```bash
# Visit https://developers.openai.com/codex/quickstart/
```

### GitHub Copilot CLI
```bash
# macOS/Linux
brew install copilot-cli

# Windows
winget install GitHub.Copilot

# npm
npm install -g @github/copilot
```

---

## MCP Integration

| MCP Server | Status | Configuration |
|------------|--------|---------------|
| **Atlassian** | ✅ Working | See MCP_README.md |
| **GitHub** | ✅ Working | See MCP_README.md |
| **AWS API** | ✅ Working | See MCP_README.md |
| **XMind Generator** | ✅ Working | `npx xmind-generator-mcp` — outputs `.xmind` files to `~/Desktop` |

All tools support MCP servers but configure them differently:
- **Claude:** `.mcp.json`
- **Gemini:** `settings.json` mcpServers section
- **Codex:** `config.toml` [mcp_servers] section
- **Copilot:** `~/.copilot/mcp-config.json`

### MCP Prerequisites

**For AWS MCP Server:**
```bash
brew install uv
hash -r
which uvx  # Should show /opt/homebrew/bin/uvx
```

See `MCP_README.md` for complete setup instructions.

---

## Getting Started

### 1. Install Tools
Install Claude Code, Gemini CLI, Codex CLI, and GitHub Copilot CLI using the links above.

### 2. Authenticate
```bash
# Claude Code
claude  # Follow prompts

# Gemini CLI
# Add GOOGLE_API_KEY to .env

# Codex CLI
codex  # Follow prompts

# GitHub Copilot CLI
copilot  # Follow prompts or gh auth login
```

### 3. Verify Configuration
```bash
# Claude Code
claude
# Verify CLAUDE.md loaded, test /tdd and /pr skills

# Gemini CLI
gemini
/memory refresh

# Codex CLI
codex
# Verify AGENTS.md loaded

# GitHub Copilot CLI
copilot
/agent
# Verify custom agents available
```

### 4. Review Role Definitions
- Read `CLAUDE.md` for primary developer role
- Read `GEMINI.md` for secondary agent role
- Read `AGENTS.md` for tertiary agent role
- Read `.github/COPILOT_CLI_SETUP.md` for quaternary agent role

---

## Best Practices

### Use the Right Tool for the Job

**Claude Code (PRIMARY):**
- New features
- Bug fixes
- Refactoring (any size)
- Architecture decisions
- Documentation
- PRs and commits

**Gemini/Codex/Copilot (SECONDARY/TERTIARY/QUATERNARY):**
- Test coverage after Claude implements
- Validation runs and result reporting
- Small, safe refactors (< 50 lines, tests passing)

### Never
- ❌ Use secondary agents for architectural decisions
- ❌ Use secondary agents to implement features
- ❌ Use secondary agents for large refactors
- ❌ Copy configurations between tools (each has native format)
- ❌ Assume feature parity (each tool is different!)

### Always
- ✅ Use Claude Code as primary developer
- ✅ Configure each tool according to its native format
- ✅ Review role definitions in context files
- ✅ Keep tests passing before using safe-refactor agents
- ✅ Run validation before committing

---

## Troubleshooting

### Claude Code Not Loading CLAUDE.md
- Ensure file is in repository root
- Check that CLAUDE.md is not gitignored
- Restart Claude Code

### Gemini CLI Not Loading Context
- Run `/memory refresh` to load GEMINI.md
- Verify GEMINI.md exists in root
- Check settings.json contextFileName

### Codex CLI Not Loading AGENTS.md
- Verify model_instructions_file in config.toml
- Check AGENTS.md exists in root
- Restart Codex CLI

### GitHub Copilot CLI Agents Not Found
- Verify .github/agents/ directory exists
- Check that agent files have .agent.md extension
- Verify YAML frontmatter is valid
- Run `copilot` and use `/agent` to list available agents

---

## Sources

This configuration was created based on official documentation:

- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Gemini CLI Configuration](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html)
- [Codex CLI Configuration](https://developers.openai.com/codex/config-reference/)
- [GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

---

## Questions?

See `AI_TOOLS_CONFIGURATION_GUIDE.md` for comprehensive documentation or:

- **Claude Code:** `CLAUDE.md`
- **Gemini CLI:** `GEMINI.md`
- **Codex CLI:** `AGENTS.md`
- **GitHub Copilot CLI:** `.github/COPILOT_CLI_SETUP.md`
- **MCP Setup:** `MCP_README.md`
- **Team Info:** `TEAMS_MESSAGE.md`
