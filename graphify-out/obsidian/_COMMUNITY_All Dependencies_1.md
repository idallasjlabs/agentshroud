---
type: community
cohesion: 0.21
members: 8
---

# All Dependencies.md

**Cohesion:** 0.21 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-require()]] - code - gateway/soc/auth.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[Action]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[Request to write file content to an allowlisted SSH host.      Unlike SSHExecReq]] - rationale - gateway/ingest_api/models.py
- [[Resource]] - code - gateway/soc/auth.py
- [[SSHWriteFileRequest]] - code - gateway/ingest_api/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/All_Dependenciesmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__FakeRBAC]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[SSHWriteFileRequest]] - degree 5, connects to 2 communities
- [[dot-require()]] - degree 4, connects to 1 community
