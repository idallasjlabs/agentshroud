---
type: community
cohesion: 0.18
members: 11
---

# ADR-002: Default-Allow Security Philosophy

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[AGENTS]] - document - AGENTS.md
- [[AGENTS.md — Codex CLI Guidance]] - document - AGENTS.md
- [[Codex Configuration (.codexconfig.toml)]] - document - AGENTS.md
- [[Codex Safe Refactor Role]] - concept - AGENTS.md
- [[Codex Test Augmenter Role]] - concept - AGENTS.md
- [[Codex Validation Runner Role]] - concept - AGENTS.md
- [[Data Lakehouse Platform (GSDL)]] - concept - AGENTS.md
- [[Guidance for ChatGPT Codex CLI when working in this repository.]] - document - AGENTS.md
- [[safe-refactor.agent]] - document - .github/agents/safe-refactor.agent.md
- [[test-augmenter.agent]] - document - .github/agents/test-augmenter.agent.md
- [[validation-runner.agent]] - document - .github/agents/validation-runner.agent.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ADR-002_Default-Allow_Security_Philosophy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_OpenClaw Skill Metadata Schema (frontmatter conv]]
- 1 edge to [[_COMMUNITY_v0.8.0 — Watchtower (Complete Security + Every]]
- 1 edge to [[_COMMUNITY_session-prompt-setup.sh]]
- 1 edge to [[_COMMUNITY_SOCWebSocketHandler]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]

## Top bridge nodes
- [[AGENTS.md — Codex CLI Guidance]] - degree 8, connects to 2 communities
- [[AGENTS]] - degree 2, connects to 1 community
- [[safe-refactor.agent]] - degree 2, connects to 1 community
- [[test-augmenter.agent]] - degree 2, connects to 1 community
- [[validation-runner.agent]] - degree 2, connects to 1 community