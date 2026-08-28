---
type: community
cohesion: 0.33
members: 6
---

# Community 1124

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[Test approval queue endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1124
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]

## Top bridge nodes
- [[TestApprovalEndpoints]] - degree 5, connects to 2 communities
- [[.test_approval_decision()]] - degree 3, connects to 1 community
- [[.test_approval_queue_list()]] - degree 3, connects to 1 community