---
type: community
cohesion: 1.00
members: 2
---

# Approval Hardening

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.config()]] - code - gateway/tests/test_approval_hardening.py
- [[Create test configuration.]] - rationale - gateway/tests/test_approval_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Approval_Hardening
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Approval Hardening]]

## Top bridge nodes
- [[.config()]] - degree 3, connects to 2 communities