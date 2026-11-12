---
type: community
members: 6
---

# Community 2119

**Members:** 6 nodes

## Members
- [[.test_dm_approval_no_group_side_effect()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_dm_approval_routes_only_to_owner()]] - code - gateway/tests/test_group_approval_routing.py
- [[DM approval must not send any message to a group chat ID.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[DM-context approvals must not trigger group notifications.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[TestDMApprovalOwnerOnly]] - code - gateway/tests/test_group_approval_routing.py
- [[When group_chat_id is None, only the owner receives a notification.]] - rationale - gateway/tests/test_group_approval_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2119
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 30]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 1560]]

## Top bridge nodes
- [[TestDMApprovalOwnerOnly]] - degree 6, connects to 3 communities
- [[.test_dm_approval_routes_only_to_owner()]] - degree 3, connects to 1 community
- [[.test_dm_approval_no_group_side_effect()]] - degree 3, connects to 1 community