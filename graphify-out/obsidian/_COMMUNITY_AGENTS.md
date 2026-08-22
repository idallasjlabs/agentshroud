---
type: community
cohesion: 0.18
members: 11
---

# Agents

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[AGENTS.md — Codex CLI Guidance]] - document - AGENTS.md
- [[Claude Code — Primary Developer]] - concept - AGENTS.md
- [[Codex Configuration (.codexconfig.toml)]] - document - AGENTS.md
- [[Codex Prime Directive Not Primary Developer]] - rationale - AGENTS.md
- [[Codex Safe Refactor Role]] - concept - AGENTS.md
- [[Codex Test Augmenter Role]] - concept - AGENTS.md
- [[Codex Validation Runner Role]] - concept - AGENTS.md
- [[Data Lakehouse Platform (GSDL)]] - concept - AGENTS.md
- [[safe-refactor.agent]] - document - .github/agents/safe-refactor.agent.md
- [[test-augmenter.agent]] - document - .github/agents/test-augmenter.agent.md
- [[validation-runner.agent]] - document - .github/agents/validation-runner.agent.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agents
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Safe Refactor.agent (agents)]]
- 1 edge to [[_COMMUNITY_Augmenter.agent (agents)]]
- 1 edge to [[_COMMUNITY_Validation Runner.agent (agents)]]

## Top bridge nodes
- [[safe-refactor.agent]] - degree 2, connects to 1 community
- [[test-augmenter.agent]] - degree 2, connects to 1 community
- [[validation-runner.agent]] - degree 2, connects to 1 community