# Upgrade Log

## 2026-05-05 (Part 2) — Agent Cleanup, Gemini Recursion Fix, `.env.example` Fixes

### Summary

Removed 160 stub/duplicate files from the agent layer, fixed a Gemini Command-Line Interface (CLI)
"unexpected tool call" recursion error, and corrected incorrect variable names
in the per-account GitHub Model Context Protocol (MCP) `.env.example` files.

### Agent Cleanup

All 52 auto-generated stub agents in `.llm_settings/agents/` were deleted. The stubs
were placeholder files with no real content ("Purpose: X agent agent. Responsibilities:
- Perform X agent-specific tasks"). The only real agent (`i-security-reviewer.md`) was kept.

Additionally, 109 pre-committed `.llm_settings/.gemini/agents/` templates were removed —
they were artifacts from a prior self-deploy and were never used by the `llm-init`
deployment pipeline. `_llm_init_convert_for_gemini()` regenerates them on every run.

| Change | Count |
|--------|-------|
| Stub agents deleted from `.llm_settings/agents/` | 51 |
| Stale `.llm_settings/.gemini/agents/` templates deleted | 109 |
| Real agents kept (`i-security-reviewer.md`) | 1 |

**After cleanup, each platform receives:**

| Platform | Directory | Count |
|----------|-----------|-------|
| Claude | `.claude/skills/` + `.claude/agents/` | 57 skills + 1 agent |
| Gemini | `.gemini/agents/` | 58 agents |
| Codex | `.codex/agents/` | 58 agents |

### Gemini Standalone Mode Fix

Gemini CLI loads every file in `.gemini/agents/` as a callable subagent tool. When running
a skill (e.g. `@i-aws`), all 58 other agents become registered tools. The model tried to
invoke one → `LocalAgentExecutor` blocked it as recursion → response stopped with
"unexpected tool call" error.

**Fix:** `_llm_init_convert_for_gemini()` in `llm-init.sh` now injects a constraint block
at the top of every agent body. All 58 Gemini templates were updated:

```markdown
> **[Gemini Standalone Mode]** Complete this task using direct MCP tool calls.
> Do **not** invoke or reference other agents by name — all capabilities are
> available through the MCP tools configured in `.gemini/settings.json`.
```

Target repos need `llm-init` re-run to pick up the updated templates.

### `.env.example` Variable Name Fix

All three per-account GitHub MCP wrappers had `GITHUB_PERSONAL_ACCESS_TOKEN` in their
`.env.example` files (copied from the generic default wrapper template). Each wrapper
resolves its own account-specific env var, causing `.env` copies to silently fail.

| File | Old variable | New variable |
|------|-------------|-------------|
| `github/fluence/.env.example` | `GITHUB_PERSONAL_ACCESS_TOKEN` | `GITHUB_TOKEN_FLUENCE` |
| `github/idallasj/.env.example` | `GITHUB_PERSONAL_ACCESS_TOKEN` | `GITHUB_TOKEN_IDALLASJ` |
| `github/agentshroud/.env.example` | `GITHUB_PERSONAL_ACCESS_TOKEN` | `GITHUB_TOKEN_AGENTSHROUD` |

---

## 2026-05-05 — Skills `i-` Prefix, MCP Expansion, `--mcp` Flag

### Summary

All 58 custom slash commands renamed with `i-` prefix (e.g. `/pr` → `/i-pr`, `/tdd` → `/i-tdd`,
`/cr` → `/i-cr`, `/gg` → `/i-gg`, `/browser` → `/i-browser`) to avoid collisions with Claude Code
built-ins. MCP server count expanded from 3 to 11 with per-account GitHub and Atlassian instances.
`--mcp` flag added to `llm-init` for per-repo server selection. `--jira` flag removed (replaced by
`--mcp atlassian-*`). `--allow-self-deploy` flag removed — `llm-init` now deploys to any repo without it.

### Skills Renamed (all 58)

All skills under `.llm_settings/skills/` now carry the `i-` prefix. Skill profile files
(`all.txt`, `development.txt`, `podcast.txt`) updated to match.

| Old | New |
|-----|-----|
| `pr` | `i-pr` |
| `tdd` | `i-tdd` |
| `cr` | `i-cr` |
| `gg` | `i-gg` |
| `browser` | `i-browser` |
| *(all 58 skills)* | *(all prefixed `i-`)* |

### MCP Servers Expanded

| Server Key | Path |
|------------|------|
| `github` (default/legacy) | `mcp-servers/github/default/github-mcp-wrapper.sh` |
| `github-idallasj` | `mcp-servers/github/idallasj/github-mcp-wrapper.sh` |
| `github-fluence` | `mcp-servers/github/fluence/github-mcp-wrapper.sh` |
| `github-agentshroud` | `mcp-servers/github/agentshroud/github-mcp-wrapper.sh` |
| `atlassian-fluence` | `mcp-servers/atlassian/fluence/mcp-atlassian.sh` |
| `atlassian-agentshroud` | `mcp-servers/atlassian/agentshroud/mcp-atlassian.sh` |
| `atlassian-idallasj` | `mcp-servers/atlassian/idallasj/mcp-atlassian.sh` |
| `awslabs.aws-api-mcp-server` | `uvx awslabs.aws-api-mcp-server@latest` |
| `xmind` | `npx xmind-generator-mcp` |
| `safari` | `npx safari-mcp` |
| `home-assistant` | `mcp-servers/home-assistant/mcp-ha.sh` |

### `llm-init` Flag Changes

| Flag | Change |
|------|--------|
| `--mcp <server>` | **Added** — select MCP servers per-repo (repeatable); valid values: `github \| github-idallasj \| github-fluence \| github-agentshroud \| aws \| xmind \| safari \| home-assistant \| atlassian-fluence \| atlassian-agentshroud \| atlassian-idallasj \| all` |
| `--jira` | **Removed** — use `--mcp atlassian-fluence` / `--mcp atlassian-agentshroud` instead |
| `--allow-self-deploy` | **Removed** — `llm-init` now deploys to any repo unconditionally |

### Three-Way Config Sync

`.mcp.json`, `.gemini/settings.json`, and `.codex/config.toml` are all filtered together
when `--mcp` is specified. Unselected servers are removed from all three files.

---

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
