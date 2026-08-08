---
type: community
cohesion: 0.15
members: 16
---

# AGENTS.md

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Members
- [[AGENTS.md — Codex CLI Guidance]] - document - AGENTS.md
- [[CLAUDE.md — AgentShroud Governance]] - document - CLAUDE.md
- [[Claude Code Prime Directive (No New Files)]] - rationale - CLAUDE.md
- [[Claude Code — Primary Developer]] - concept - AGENTS.md
- [[Codex Configuration (.codexconfig.toml)]] - document - AGENTS.md
- [[Codex Prime Directive Not Primary Developer]] - rationale - AGENTS.md
- [[Codex Safe Refactor Role]] - concept - AGENTS.md
- [[Codex Test Augmenter Role]] - concept - AGENTS.md
- [[Codex Validation Runner Role]] - concept - AGENTS.md
- [[Data Lakehouse Platform (GSDL)]] - concept - AGENTS.md
- [[Multi-Agent Hierarchy (ClaudeGeminiCodex)]] - concept - CLAUDE.md
- [[No Security Theater Rule]] - rationale - CLAUDE.md
- [[Test-Driven Development Default]] - concept - CLAUDE.md
- [[safe-refactor.agent]] - document - .github/agents/safe-refactor.agent.md
- [[test-augmenter.agent]] - document - .github/agents/test-augmenter.agent.md
- [[validation-runner.agent]] - document - .github/agents/validation-runner.agent.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AGENTSmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_.githubagents]]
- 1 edge to [[_COMMUNITY_.githubagents]]
- 1 edge to [[_COMMUNITY_.githubagents]]
- 1 edge to [[_COMMUNITY_CHANGELOG]]
- 1 edge to [[_COMMUNITY_README]]

## Top bridge nodes
- [[No Security Theater Rule]] - degree 3, connects to 2 communities
- [[safe-refactor.agent]] - degree 3, connects to 1 community
- [[test-augmenter.agent]] - degree 3, connects to 1 community
- [[validation-runner.agent]] - degree 3, connects to 1 community