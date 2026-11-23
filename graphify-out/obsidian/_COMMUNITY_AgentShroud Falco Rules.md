---
type: community
members: 3
---

# AgentShroud Falco Rules

**Members:** 3 nodes

## Members
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Falco_Rules
SORT file.name ASC
```
