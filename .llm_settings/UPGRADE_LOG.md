# Upgrade Log

## 2026-03-08 — AI Engineering OS v1.0 Integration

### Summary

Merged `ai_engineering_os/` tarball into this repository. Renamed internal
settings subdirectory from `llm_settings/` → `.llm_settings/` to keep the
working tree clean while preserving all git history via `git mv`.

### Source

- **Tarball:** `/tmp/ai_engineering_operating_system.tgz`
- **Contents:** `ai_engineering_os/` — 52 agents, 16 new skills (+ tdd update),
  2 new scripts, 3 new directories, WORKFLOW.md, .claude/ORCHESTRATOR.md

---

### Files Added

| Path | Description |
|------|-------------|
| `.llm_settings/agents/*.md` | 52 flat agents (replaced 9 podcast-pipeline agents) |
| `.llm_settings/agents/README.md` | Agents directory README |
| `.llm_settings/skills/agile/` | New skill |
| `.llm_settings/skills/architecture-review/` | New skill |
| `.llm_settings/skills/bdd/` | New skill |
| `.llm_settings/skills/cd/` | New skill |
| `.llm_settings/skills/chaos-engineering/` | New skill |
| `.llm_settings/skills/ci/` | New skill |
| `.llm_settings/skills/devsecops/` | New skill |
| `.llm_settings/skills/gitops/` | New skill |
| `.llm_settings/skills/incident-response/` | New skill |
| `.llm_settings/skills/kaizen/` | New skill |
| `.llm_settings/skills/kanban/` | New skill |
| `.llm_settings/skills/observability/` | New skill |
| `.llm_settings/skills/scrum/` | New skill |
| `.llm_settings/skills/sdlc/` | New skill |
| `.llm_settings/skills/sre/` | New skill |
| `.llm_settings/skills/value-stream-mapping/` | New skill |
| `.llm_settings/skills/tdd/SKILL.md` | Updated (replaced) |
| `.llm_settings/scripts/ci_self_heal.sh` | New script |
| `.llm_settings/scripts/run_agents.sh` | New script |
| `.llm_settings/scripts/README.md` | New scripts README |
| `.llm_settings/ci-cd/` | New directory |
| `.llm_settings/podcast/` | New directory |
| `.llm_settings/sre/` | New directory |
| `.llm_settings/WORKFLOW.md` | Multi-agent workflow guide |
| `.claude/ORCHESTRATOR.md` | Orchestrator context for Claude Code |

### Files Modified (path reference updates)

All `llm_settings/` → `.llm_settings/` references updated in 29 files:

**Root / config:**
`.mcp.json`, `.gemini/settings.json`, `.gemini/GEMINI.md`,
`.codex/config.toml`, `.claude/skills/mcpm-auth-reset/SKILL.md`,
`.claude/skills/mcpm-doctor/SKILL.md`, `.claude/skills/reference/SKILLS_GUIDE.md`,
`.gemini/agents/mcpm-auth-reset.md`, `.gemini/agents/mcpm-doctor.md`,
`.codex/agents/mcpm-auth-reset.md`, `.codex/agents/mcpm-doctor.md`

**Docs:**
`README.md`, `CHANGELOG.md`, `AGENTS.md`, `ADMIN_COLLABORATOR_GUIDE.md`,
`COLLABORATOR_QUICK_START.md`, `COLLABORATOR_SETUP.md`, `continue-20260215-0932.md`

**Internal .llm_settings:**
`scripts/llm-init.sh`, `scripts/security/security-audit.sh`,
`scripts/setup-mcp-user.sh`, `docs/CONFIGURATION_SUMMARY.md`,
`docs/SECURITY_GUIDE.md`, `docs/SKILLS_REFERENCE.md`,
`git-hooks/README.md`, `mcp-servers/github/test-github.sh`,
`skills/mcpm-auth-reset/SKILL.md`, `skills/mcpm-doctor/SKILL.md`,
`skills/reference/SKILLS_GUIDE.md`

### Files Removed

| Path | Reason |
|------|--------|
| `.llm_settings/agents/podcast-pipeline/` | Replaced by 52 flat agents |
| `.llm_settings/skills-20260211-0935.tgz` | Stale archive |

### Rollback Reference

To rollback the directory rename:
```bash
git mv .llm_settings llm_settings
# Then reverse all .llm_settings/ → llm_settings/ substitutions in affected files
```

The 9 original podcast-pipeline agents are preserved in git history at commit
prior to this upgrade (tag or SHA recorded in CHANGELOG.md).

---

### Counts After Upgrade

| Asset | Before | After |
|-------|--------|-------|
| Agents | 9 (nested under podcast-pipeline/) | 52 (flat) |
| Skills | 38 | 54 |
| Scripts | 6 | 8 |
| Directories | docs/, env/, git-hooks/, mcp-servers/, scripts/, templates/ | + ci-cd/, podcast/, sre/ |
