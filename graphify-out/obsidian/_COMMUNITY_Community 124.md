---
type: community
members: 16
---

# Community 124

**Members:** 16 nodes

## Members
- [[.test_extract_chat_id_from_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_extract_chat_id_returns_none_for_non_group()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_false_for_collab_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_false_for_default()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_true_for_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_route_approval_auto_detects_group_context()]] - code - gateway/tests/test_group_approval_routing.py
- [[Extract the raw chat_id from a group-{chat_id} agent_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[GroupApprovalRouter]] - code - gateway/approval_queue/group_router.py
- [[GroupApprovalRouter must correctly distinguish group vs DM context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Routes approval notifications to owner DM and (optionally) group thread.      Ar]] - rationale - gateway/approval_queue/group_router.py
- [[TestGroupApprovalRouterContextDetection]] - code - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'collab-' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'group-' is recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id='default' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[extract_group_chat_id returns None for non-group agent IDs.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[route_approval auto-detects group context when group_chat_id not explicitly pass]] - rationale - gateway/tests/test_group_approval_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_124
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 1305]]
- 4 edges to [[_COMMUNITY_Community 1560]]
- 3 edges to [[_COMMUNITY_Community 30]]
- 2 edges to [[_COMMUNITY_Community 2326]]
- 2 edges to [[_COMMUNITY_Community 2120]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 2119]]
- 1 edge to [[_COMMUNITY_Community 68]]

## Top bridge nodes
- [[GroupApprovalRouter]] - degree 23, connects to 8 communities
- [[TestGroupApprovalRouterContextDetection]] - degree 10, connects to 2 communities
- [[.test_route_approval_auto_detects_group_context()]] - degree 3, connects to 1 community