---
type: community
members: 4
---

# i-release-gate — Release gate and operational readiness (release / post-deploy)

**Members:** 4 nodes

## Members
- [[Playbook_19]] - document - .github/agents/i-release-gate.agent.md
- [[Testing types owned (priority order)_19]] - document - .github/agents/i-release-gate.agent.md
- [[i-release-gate — Release gate and operational readiness (release  post-deploy)_2]] - document - .github/agents/i-release-gate.agent.md
- [[i-release-gate.agent]] - document - .github/agents/i-release-gate.agent.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/i-release-gate__Release_gate_and_operational_readiness_release_/_post-deploy
SORT file.name ASC
```
