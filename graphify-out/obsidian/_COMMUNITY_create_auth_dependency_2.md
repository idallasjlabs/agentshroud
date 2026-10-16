---
type: community
cohesion: 0.20
members: 12
---

# create_auth_dependency

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_2]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/approval.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Request_6]] - code - gateway/ingest_api/routes/approval.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/approval.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[list_pending_approvals()_1]] - code - gateway/ingest_api/routes/approval.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_auth_dependency
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[decide_approval()]] - degree 6, connects to 2 communities
- [[submit_approval_request()]] - degree 6, connects to 2 communities
- [[auth_dep()_3]] - degree 4, connects to 2 communities
- [[list_pending_approvals()_1]] - degree 4, connects to 1 community
