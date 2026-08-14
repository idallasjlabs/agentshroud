---
type: community
members: 3
---

# scripts/export-telegram-history.py

**Members:** 3 nodes

## Members
- [[1. Security Module Analysis]] - document - docs/planning/reviews/blue-team-audit-v0.7.0.md
- [[1.1 Module Integration Status]] - document - docs/planning/reviews/blue-team-audit-v0.7.0.md
- [[1.2 Critical Security Pipeline Flow]] - document - docs/planning/reviews/blue-team-audit-v0.7.0.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/export-telegram-historypy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_CLAUDE]]

## Top bridge nodes
- [[1. Security Module Analysis]] - degree 3, connects to 1 community