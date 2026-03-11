# GitHub Copilot CLI Setup Guide

## Overview

GitHub Copilot CLI is configured as a **SECONDARY/TERTIARY agent** in this repository for test augmentation, validation runs, and safe refactors.

**Claude Code is the PRIMARY developer.**

---

## Installation

### Windows
```bash
winget install GitHub.Copilot
```

### macOS / Linux
```bash
brew install copilot-cli
```

### npm (Cross-platform)
```bash
npm install -g @github/copilot
```

### Install Script
```bash
curl -fsSL https://cli.github.com/copilot/install.sh | sh
```

---

## Authentication

### Option 1: GitHub Login
```bash
copilot
# Follow prompts to authenticate
```

### Option 2: Personal Access Token
1. Create PAT with "Copilot Requests" permission
2. Set environment variable:
   ```bash
   export GITHUB_ASKPASS=/path/to/script/returning/token
   ```

---

## Configuration Files

### User-Level Config
**Location:** `~/.copilot/config.json`

Create this file based on `.github/copilot-config.json.example`:

```bash
# Create .copilot directory
mkdir -p ~/.copilot

# Copy example config
cp .github/copilot-config.json.example ~/.copilot/config.json

# Edit as needed
nano ~/.copilot/config.json
```

### MCP Servers
**Location:** `~/.copilot/mcp-config.json`

Configure Model Context Protocol servers for extended functionality.

---

## Custom Agents

This repository includes three custom agents for GitHub Copilot CLI:

### 1. test-augmenter
**Purpose:** Add test coverage, identify edge cases, improve test quality

**Usage:**
```bash
# Interactive
copilot
/agent test-augmenter

# Command-line
copilot --agent=test-augmenter --prompt "Add tests for data parser"

# Natural language
copilot
> Use the test-augmenter agent to add edge case tests
```

**Capabilities:**
- Identifies missing test coverage
- Adds targeted, deterministic tests
- Ensures ≥80% coverage target
- Focuses on edge cases and error paths

### 2. validation-runner
**Purpose:** Execute validation scripts, run tests, report results

**Usage:**
```bash
# Interactive
copilot
/agent validation-runner

# Command-line
copilot --agent=validation-runner --prompt "Run full validation suite"

# Natural language
copilot
> Use the validation-runner agent to validate Stage 1 changes
```

**Capabilities:**
- Executes test suites and quality checks
- Runs pytest, ruff, black, mypy
- Reports pass/fail with actionable next steps
- Validates data pipeline correctness

### 3. safe-refactor
**Purpose:** Safe, local refactorings ONLY after tests pass

**Usage:**
```bash
# Interactive
copilot
/agent safe-refactor

# Command-line
copilot --agent=safe-refactor --prompt "Improve variable naming in parser.py"

# Natural language
copilot
> Use the safe-refactor agent to extract helper functions
```

**Capabilities:**
- Variable renaming and clarity improvements
- Extract small helper functions
- Remove code duplication
- Simplify conditionals
- **Only operates when tests are green**

---

## Agent Files Location

Custom agent profiles are stored in:
```
.github/agents/
├── test-augmenter.agent.md
├── validation-runner.agent.md
└── safe-refactor.agent.md
```

These agents are automatically available when running Copilot CLI in this repository.

---

## Basic Usage

### Start Interactive Session
```bash
copilot
```

### Run with Specific Agent
```bash
copilot --agent=test-augmenter --prompt "Add tests for module X"
```

### Select Model
```bash
copilot
/model
# Choose from: claude-sonnet-4-5, claude-sonnet-4, gpt-5
```

### Check Context Usage
```bash
copilot
/usage    # View session statistics
/context  # Visual token usage
/compact  # Manually compress history
```

---

## Role & Restrictions

### What Copilot CLI CAN Do (in this repo)
✅ Add test coverage (test-augmenter agent)
✅ Run validation scripts (validation-runner agent)
✅ Safe refactors after tests pass (safe-refactor agent)
✅ Execute commands and report results
✅ Analyze code for test gaps
✅ Identify edge cases

### What Copilot CLI CANNOT Do (in this repo)
❌ Make architectural decisions → Defer to Claude Code
❌ Implement new features → Defer to Claude Code
❌ Perform large refactors → Defer to Claude Code
❌ Create documentation → Defer to Claude Code (unless requested)
❌ Modify schemas or APIs → Defer to Claude Code

**Claude Code is the PRIMARY developer** - use it for feature work, architecture, and complex refactors.

---

## Security & Permissions

### Trusted Folders
Configure in `~/.copilot/config.json`:
```json
{
  "trusted_folders": [
    "/Users/username/Development/LLM_Settings"
  ]
}
```

### URL Access Control
```json
{
  "allowed_urls": [
    "https://api.github.com/*",
    "https://docs.github.com/*"
  ],
  "denied_urls": [
    "http://*"
  ]
}
```

### Path Permissions
By default, Copilot CLI can access:
- Current working directory
- Subdirectories
- System temp directory

To allow all paths (use with caution):
```bash
copilot --allow-all-paths
```

### Tool Approval
Allow specific tools without prompting:
```bash
copilot --allow-tool 'write'  # Allow file edits
copilot --allow-tool 'bash'   # Allow command execution
```

---

## Repository Context

This repository implements a **Data Lakehouse platform** for distributed energy storage systems.

### Primary Focus
- Data pipelines (Central DAS → S3 lakehouse)
- Schema validation and partitioning
- Data quality checks

### Key Testing Requirements
- ≥80% code coverage
- Fast, deterministic unit tests
- Isolated tests (no network, no sleeps)
- Data validation correctness

### Environment
```bash
# Activate conda environment
conda activate gsdl

# Run tests
pytest -q

# Check coverage
pytest --cov=.
```

---

## Common Workflows

### 1. Add Test Coverage
```bash
# Start Copilot with test-augmenter
copilot --agent=test-augmenter

# Prompt
> Analyze test coverage for src/parser.py and add missing tests
```

### 2. Run Validation Suite
```bash
# Start Copilot with validation-runner
copilot --agent=validation-runner

# Prompt
> Run full validation: pytest, ruff, black, and report results
```

### 3. Safe Refactor
```bash
# Ensure tests pass first!
pytest -q

# Start Copilot with safe-refactor
copilot --agent=safe-refactor

# Prompt
> Extract helper function for data validation in process.py
```

---

## Built-in Default Agents

In addition to custom agents, Copilot CLI includes built-in agents:

| Agent | Purpose |
|-------|---------|
| **Explore** | Quick codebase analysis without cluttering main context |
| **Task** | Execute commands like tests and builds |
| **Plan** | Create implementation plans based on code structure |
| **Code-review** | Review changes focusing on genuine issues |

Usage:
```bash
copilot
/agent explore

# Or
/agent plan
```

---

## Context Management

### Auto-Compaction
- Automatically compresses history at 95% token limit
- Warns when < 20% tokens remain

### Manual Controls
```bash
/usage    # View token usage, premium requests, duration
/context  # Visual token usage overview
/compact  # Manually compress conversation history
```

---

## MCP Server Integration

Configure MCP servers in `~/.copilot/mcp-config.json`:

```json
{
  "servers": {
    "github": {
      "command": "node",
      "args": ["/path/to/github-mcp-server.js"]
    }
  }
}
```

See `MCP_README.md` for OAuth setup.

---

## Troubleshooting

### Authentication Issues
```bash
# Check GitHub CLI auth
gh auth status

# Re-authenticate
gh auth login
```

### Agent Not Found
```bash
# Verify agent files exist
ls -la .github/agents/

# Check for .agent.md extension
# Files must be: name.agent.md
```

### Configuration Not Loading
```bash
# Verify config location
ls -la ~/.copilot/config.json

# Check JSON syntax
cat ~/.copilot/config.json | python -m json.tool
```

### Path Permission Denied
```bash
# Add to trusted folders
nano ~/.copilot/config.json
# Add path to "trusted_folders" array
```

---

## References

- [GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Custom Agents Configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Creating Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
- [GitHub Copilot CLI Changelog](https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install/)
- [Install Guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli)

---

## Questions?

- **Copilot CLI issues:** See this file
- **Claude Code (primary):** See `CLAUDE.md`
- **Gemini CLI:** See `GEMINI.md`
- **Codex CLI:** See `AGENTS.md`
- **Multi-agent setup:** See `AI_TOOLS_CONFIGURATION_GUIDE.md`
- **MCP integration:** See `MCP_README.md`
