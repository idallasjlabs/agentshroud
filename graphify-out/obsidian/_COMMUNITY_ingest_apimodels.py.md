---
type: community
cohesion: 0.50
members: 4
---

# ingest_api/models.py

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - rationale - gateway/ingest_api/models.py
- [[SSHWriteFileRequest]] - code - gateway/ingest_api/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingest_api/modelspy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_DataLedger]]

## Top bridge nodes
- [[SSHWriteFileRequest]] - degree 5, connects to 2 communities
