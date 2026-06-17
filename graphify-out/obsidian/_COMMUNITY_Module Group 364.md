---
type: community
cohesion: 0.24
members: 10
---

# Module Group 364

**Cohesion:** 0.24 - loosely connected
**Members:** 10 nodes

## Members
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_3]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/approval.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Request_1]] - code - gateway/ingest_api/routes/approval.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_364
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]

## Top bridge nodes
- [[decide_approval()]] - degree 6, connects to 2 communities
- [[submit_approval_request()]] - degree 6, connects to 2 communities
- [[Request_1]] - degree 4, connects to 1 community
- [[list_pending_approvals()]] - degree 4, connects to 1 community