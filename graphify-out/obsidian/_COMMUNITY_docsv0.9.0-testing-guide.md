---
type: community
members: 6
---

# docs/v0.9.0-testing-guide.md

**Members:** 6 nodes

## Members
- [[1. Agent Trust Levels]] - document - docs/flows/state-diagrams.md
- [[2. Kill Switch States]] - document - docs/flows/state-diagrams.md
- [[3. Approval Queue States]] - document - docs/flows/state-diagrams.md
- [[4. Gateway Operational Modes]] - document - docs/flows/state-diagrams.md
- [[AgentShroud State Diagrams]] - document - docs/flows/state-diagrams.md
- [[state-diagrams]] - document - docs/flows/state-diagrams.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docs/v090-testing-guidemd
SORT file.name ASC
```
