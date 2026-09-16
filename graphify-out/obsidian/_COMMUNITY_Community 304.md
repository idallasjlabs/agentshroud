---
type: community
cohesion: 0.11
members: 27
---

# Community 304

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-claudesettings.json (hook + permission wiring)]] - code - .claude/settings.json
- [[dot-geminisettings.json (Gemini CLI MCP config)]] - code - .gemini/settings.json
- [[_install_hint() (nested helper)]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_convert_for_gemini()]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_ensure_production_gate_marker()]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_merge_claude_md()]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_reconcile_settings_local()]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_render_mcp()]] - code - .llm_settings/scripts/llm-init.sh
- [[_llm_init_skill_allowed()]] - code - .llm_settings/scripts/llm-init.sh
- [[auto_format_python.sh (PostToolUse hook)]] - code - .claude/scripts/claude-hooks/auto_format_python.sh
- [[block_credential_read.sh (PreToolUse hook)]] - code - .claude/scripts/claude-hooks/block_credential_read.sh
- [[block_credential_write.sh (PreToolUse hook)]] - code - .claude/scripts/claude-hooks/block_credential_write.sh
- [[block_main_commits.sh (PreToolUse hook)]] - code - .claude/scripts/claude-hooks/block_main_commits.sh
- [[install.sh (git pre-commit hook installer)]] - code - .llm_settings/git-hooks/install.sh
- [[llm-init() (main deployment function)]] - code - .llm_settings/scripts/llm-init.sh
- [[llm-init.sh]] - code - .llm_settings/scripts/llm-init.sh
- [[llm-init.sh script]] - code - .llm_settings/scripts/llm-init.sh
- [[pre-commit (gitleaks + git-secrets gate)]] - code - .llm_settings/git-hooks/pre-commit
- [[quick-setup.sh (security bootstrap orchestrator)]] - code - .llm_settings/scripts/security/quick-setup.sh
- [[remind_proposal_review.sh (PostToolUse hook)]] - code - .claude/scripts/claude-hooks/remind_proposal_review.sh
- [[require_impact_analysis.sh (PreToolUse hook, referenced)]] - code - .claude/scripts/claude-hooks/require_impact_analysis.sh
- [[run_targeted_tests.sh (PostToolUse hook)]] - code - .claude/scripts/claude-hooks/run_targeted_tests.sh
- [[security-audit.sh (gitleaksgit-secrets audit)]] - code - .llm_settings/scripts/security/security-audit.sh
- [[setup-direnv.sh (direnv env-var setup)]] - code - .llm_settings/scripts/security/setup-direnv.sh
- [[setup-env-store.sh (local MCP secrets store setup, referenced)]] - code - .llm_settings/scripts/security/setup-env-store.sh
- [[setup-pgpass.sh (PostgreSQL password file setup, referenced)]] - code - .llm_settings/scripts/security/setup-pgpass.sh
- [[warn_dangerous_bash.sh (PreToolUse hook)]] - code - .claude/scripts/claude-hooks/warn_dangerous_bash.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_304
SORT file.name ASC
```
