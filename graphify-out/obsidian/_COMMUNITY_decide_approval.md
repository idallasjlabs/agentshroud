---
type: community
members: 12
---

# decide_approval

**Members:** 12 nodes

## Members
- [[Approve or reject a pending action Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/approval.py
- [[AuthRequired_2]] - code
- [[List all pending approval requests Authentication required.]] - rationale - gateway/ingest_api/routes/approval.py
- [[Request_2]] - code
- [[Submit an action for human approval Called by agents when attempting sensitive…]] - rationale - gateway/ingest_api/routes/approval.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/approval.py
- [[decide_approval()]] - code - gateway/ingest_api/routes/approval.py
- [[get_3]] - code
- [[list_pending_approvals()_1]] - code - gateway/ingest_api/routes/approval.py
- [[post_1]] - code
- [[submit_approval_request()]] - code - gateway/ingest_api/routes/approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/decide_approval
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]

## Top bridge nodes
- [[decide_approval()]] - degree 7, connects to 3 communities
- [[submit_approval_request()]] - degree 7, connects to 3 communities
- [[list_pending_approvals()_1]] - degree 5, connects to 1 community
- [[auth_dep()_2]] - degree 4, connects to 1 community
