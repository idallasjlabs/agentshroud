---
type: community
cohesion: 0.50
members: 4
---

# .enforce_retention()

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.enforce_retention()]] - code - gateway/ingest_api/ledger.py
- [[.initialize()_1]] - code - gateway/ingest_api/ledger.py
- [[Create database, tables, and run initial cleanup          Must be called before]] - rationale - gateway/ingest_api/ledger.py
- [[Delete entries older than retention_days          Returns             Number of]] - rationale - gateway/ingest_api/ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/enforce_retention
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[.enforce_retention()]] - degree 3, connects to 1 community
- [[.initialize()_1]] - degree 3, connects to 1 community