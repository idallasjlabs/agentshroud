---
type: community
members: 11
---

# gh-issues/SKILL.md

**Members:** 11 nodes

## Members
- [[Conditional memory writes (memoryYYYY-MM-DD.md, MEMORY.md)]] - concept - skills/openclaw/healthcheck/SKILL.md
- [[Stable-named cron scheduling for periodic audits]] - concept - skills/openclaw/healthcheck/SKILL.md
- [[gh CLI (GitHub)]] - concept - skills/openclaw/github/SKILL.md
- [[gh-issues Claims File (dedup tracking)]] - concept - skills/openclaw/gh-issues/SKILL.md
- [[gh-issues Cursor File (cron sequential tracking)]] - concept - skills/openclaw/gh-issues/SKILL.md
- [[gh-issues PR Review Handler (Phase 6)]] - concept - skills/openclaw/gh-issues/SKILL.md
- [[gh-issues Sub-agent Spawn (Phase 5)]] - concept - skills/openclaw/gh-issues/SKILL.md
- [[gh-issuesSKILL]] - document - skills/openclaw/gh-issues/SKILL.md
- [[githubSKILL]] - document - skills/openclaw/github/SKILL.md
- [[healthcheckSKILL]] - document - skills/openclaw/healthcheck/SKILL.md
- [[openclaw security audit command family]] - concept - skills/openclaw/healthcheck/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gh-issues/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Coding Agent (bash-first)]]
- 1 edge to [[_COMMUNITY_gh-issues — Auto-fix GitHub Issues with Parallel Sub-agents]]
- 1 edge to [[_COMMUNITY_GitHub Skill]]
- 1 edge to [[_COMMUNITY_Workflow (follow in order)]]

## Top bridge nodes
- [[gh-issuesSKILL]] - degree 7, connects to 2 communities
- [[githubSKILL]] - degree 4, connects to 2 communities
- [[healthcheckSKILL]] - degree 4, connects to 1 community
