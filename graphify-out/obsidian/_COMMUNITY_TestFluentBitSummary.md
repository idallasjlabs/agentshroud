---
type: community
cohesion: 0.67
members: 3
---

# TestFluentBitSummary

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.get_stats()_1]] - code - gateway/ingest_api/ledger.py
- [[Any_7]] - code - gateway/ingest_api/ledger.py
- [[Get aggregate statistics          Returns             Dictionary with total ent]] - rationale - gateway/ingest_api/ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestFluentBitSummary
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[Any_7]] - degree 4, connects to 2 communities
- [[.get_stats()_1]] - degree 3, connects to 1 community