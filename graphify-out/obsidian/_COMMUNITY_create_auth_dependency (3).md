---
type: community
members: 23
---

# create_auth_dependency (3)

**Members:** 23 nodes

## Members
- [[ApprovalDecision_1]] - code - gateway/ingest_api/routes/approval.py
- [[ApprovalRequest_3]] - code - gateway/ingest_api/routes/approval.py
- [[Approve or reject a pending action      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_2]] - code - gateway/ingest_api/routes/approval.py
- [[List all pending approval requests      Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Request_4]] - code - gateway/ingest_api/routes/approval.py
- [[Submit an action for human approval      Called by agents when attempting sensit]] - rationale - gateway/ingest_api/routes/approval.py
- [[Validate a WebSocket token (single-use, time-limited).]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket_4]] - code - gateway/ingest_api/routes/approval.py
- [[WebSocket_5]] - code - gateway/ingest_api/routes/dashboard.py
- [[WebSocket endpoint for real-time approval notifications      Protocol     1. Cl]] - rationale - gateway/ingest_api/routes/approval.py
- [[WebSocket for real-time activity feed]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[WebSocket stream specialized for egresssecurity dashboard updates.]] - rationale - gateway/ingest_api/routes/dashboard.py
- [[_validate_ws_token()]] - code - gateway/ingest_api/routes/dashboard.py
- [[activity_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[approval_websocket()]] - code - gateway/ingest_api/routes/approval.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/approval.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[egress_websocket()]] - code - gateway/ingest_api/routes/dashboard.py
- [[list_pending_approvals()]] - code - gateway/ingest_api/routes/approval.py
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_auth_dependency_3
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 5 edges to [[_COMMUNITY_test_dashboard.py]]
- 3 edges to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (5)]]

## Top bridge nodes
- [[approval.py]] - degree 15, connects to 8 communities
- [[activity_websocket()]] - degree 6, connects to 2 communities
- [[egress_websocket()]] - degree 6, connects to 2 communities
- [[decide_approval()]] - degree 6, connects to 1 community
- [[submit_approval_request()]] - degree 6, connects to 1 community
