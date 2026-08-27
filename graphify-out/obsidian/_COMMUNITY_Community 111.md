---
type: community
members: 4
---

# Community 111

**Members:** 4 nodes

## Members
- [[.test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[Test POST manageegressapprove{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressdeny{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_111
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 21]]

## Top bridge nodes
- [[.test_deny_endpoint_logic()]] - degree 3, connects to 1 community
- [[.test_approve_endpoint_logic()]] - degree 2, connects to 1 community