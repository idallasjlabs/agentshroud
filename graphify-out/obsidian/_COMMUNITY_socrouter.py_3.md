---
type: community
cohesion: 1.00
members: 2
---

# soc/router.py

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[Response from SSH command execution]] - rationale - gateway/ingest_api/models.py
- [[SSHExecResponse]] - code - gateway/ingest_api/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc/routerpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_DataLedger]]

## Top bridge nodes
- [[SSHExecResponse]] - degree 3, connects to 2 communities
