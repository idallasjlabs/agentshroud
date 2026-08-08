---
type: community
cohesion: 0.67
members: 3
---

# examples/agentshroud-with-tool-risk.yaml

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[AgentShroud Config with Tool Risk Tiers (example)]] - document - examples/agentshroud-with-tool-risk.yaml
- [[PII confidence 0.8 (example) vs 0.9 floor (CLAUDE.md §7) discrepancy]] - rationale - examples/agentshroud-with-tool-risk.yaml
- [[Tool Risk Tier Policy (criticalhighmediumlow)]] - concept - examples/agentshroud-with-tool-risk.yaml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/examples/agentshroud-with-tool-riskyaml
SORT file.name ASC
```
