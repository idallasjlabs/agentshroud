---
type: community
cohesion: 0.50
members: 4
---

# .record()

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[._hash_content()]] - code - gateway/ingest_api/ledger.py
- [[.record()_2]] - code - gateway/ingest_api/ledger.py
- [[Create a new ledger entry          Args             source Source identifier (]] - rationale - gateway/ingest_api/ledger.py
- [[SHA-256 hash of content string          Args             content Text to hash]] - rationale - gateway/ingest_api/ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[.record()_2]] - degree 4, connects to 2 communities
- [[._hash_content()]] - degree 3, connects to 1 community