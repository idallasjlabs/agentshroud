---
type: community
cohesion: 0.50
members: 4
---

# TestPathIsolationManager

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/models.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]

## Top bridge nodes
- [[EmailSendRequest_1]] - degree 6, connects to 3 communities
