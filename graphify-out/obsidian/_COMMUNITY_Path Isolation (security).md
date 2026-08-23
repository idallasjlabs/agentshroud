---
type: community
cohesion: 0.50
members: 4
---

# Path Isolation (security)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[._cleanup_user_directory()]] - code - gateway/security/path_isolation.py
- [[.end_user_session()]] - code - gateway/security/path_isolation.py
- [[Clean up a user's isolated directory.]] - rationale - gateway/security/path_isolation.py
- [[End a user session and optionally clean up their isolated directory.]] - rationale - gateway/security/path_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Path_Isolation_security
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Path Isolation (security)]]

## Top bridge nodes
- [[._cleanup_user_directory()]] - degree 4, connects to 2 communities
- [[.end_user_session()]] - degree 3, connects to 1 community