---
type: community
cohesion: 0.17
members: 16
---

# approval.py

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[ApprovalDecision]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/approval.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Request_3]] - code - gateway/ingest_api/routes/approval.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket_6]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/approval.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/approvalpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_make_event()]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_RateLimiter]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_test_dashboard.py]]

## Top bridge nodes
- [[approval.py]] - degree 16, connects to 6 communities
- [[approval_websocket()]] - degree 5, connects to 2 communities
- [[decide_approval()]] - degree 6, connects to 1 community
- [[submit_approval_request()]] - degree 6, connects to 1 community
- [[auth_dep()_1]] - degree 4, connects to 1 community