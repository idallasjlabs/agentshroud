---
type: community
members: 12
---

# Community 68

**Members:** 12 nodes

## Members
- [[.test_both_owner_dm_and_group_notified()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_group_chat_receives_thread_reply()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_owner_dm_contains_action_type()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_owner_dm_references_group_chat_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_owner_receives_dm_for_group_approval()]] - code - gateway/tests/test_group_approval_routing.py
- [[A single group-context approval triggers both owner DM AND group reply.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner DM message text must reference the originating group chat_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner DM must describe the action_type that requires approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner must receive a DM when an approval originates from a group chat.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalOwnerDM]] - code - gateway/tests/test_group_approval_routing.py
- [[The originating group chat must receive a thread-reply notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[owner_chat_id receives a DM notification for every group-context approval.]] - rationale - gateway/tests/test_group_approval_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_68
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 30]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 1560]]

## Top bridge nodes
- [[TestGroupApprovalOwnerDM]] - degree 9, connects to 3 communities
- [[.test_owner_receives_dm_for_group_approval()]] - degree 3, connects to 1 community
- [[.test_owner_dm_references_group_chat_id()]] - degree 3, connects to 1 community
- [[.test_group_chat_receives_thread_reply()]] - degree 3, connects to 1 community
- [[.test_both_owner_dm_and_group_notified()]] - degree 3, connects to 1 community