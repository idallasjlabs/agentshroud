---
type: community
cohesion: 0.06
members: 48
---

# Community 123

**Cohesion:** 0.06 - loosely connected
**Members:** 48 nodes

## Members
- [[.__init__()_4]] - code - gateway/approval_queue/group_router.py
- [[._build_group_reply_text()]] - code - gateway/approval_queue/group_router.py
- [[._build_owner_dm_text()]] - code - gateway/approval_queue/group_router.py
- [[._default_send()]] - code - gateway/approval_queue/group_router.py
- [[.extract_group_chat_id()]] - code - gateway/approval_queue/group_router.py
- [[.is_group_context()]] - code - gateway/approval_queue/group_router.py
- [[.route_approval()]] - code - gateway/approval_queue/group_router.py
- [[.test_default_send_stub_returns_ok()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_extract_chat_id_from_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_extract_chat_id_returns_none_for_non_group()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_false_for_collab_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_false_for_default()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_is_group_context_true_for_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_route_approval_auto_detects_group_context()]] - code - gateway/tests/test_group_approval_routing.py
- [[.test_router_works_without_send_fn()]] - code - gateway/tests/test_group_approval_routing.py
- [[Any_1]] - code - gateway/approval_queue/group_router.py
- [[ApprovalRequest_1]] - code - gateway/approval_queue/group_router.py
- [[Build the group thread reply notification text.]] - rationale - gateway/approval_queue/group_router.py
- [[Build the owner DM notification text.]] - rationale - gateway/approval_queue/group_router.py
- [[Cover the no-op _default_send stub used when no transport is injected.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Extract the raw chat_id from a group-{chat_id} agent_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Extract the raw chat_id from a group-{chat_id} agent_id.          Returns None i]] - rationale - gateway/approval_queue/group_router.py
- [[GroupApprovalRouter]] - code - gateway/approval_queue/group_router.py
- [[GroupApprovalRouter must correctly distinguish group vs DM context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[GroupApprovalRouter wired with a mock Telegram send function.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[GroupApprovalRouter._default_send returns {ok True} without raising.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Mock async Telegram sendMessage to capture DM and group notifications.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[No-op send stub — used when no transport is injected.]] - rationale - gateway/approval_queue/group_router.py
- [[Return (router, sent_list) tuple for assertion convenience.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Return True if agent_id represents a Telegram group workspace.]] - rationale - gateway/approval_queue/group_router.py
- [[Route an approval notification to the appropriate recipients.          Routing l]] - rationale - gateway/approval_queue/group_router.py
- [[Router with no send_message_fn uses the default stub (no network calls).]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Routes approval notifications to owner DM and (optionally) group thread.      Ar]] - rationale - gateway/approval_queue/group_router.py
- [[TestGroupApprovalRouterContextDetection]] - code - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalRouterDefaultSend]] - code - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'collab-' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'group-' is recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id='default' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[extract_group_chat_id returns None for non-group agent IDs.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[gatewayapproval_queuegroup_router.py (group-{chatId} agent-id scheme, referenced)]] - code - gateway/approval_queue/group_router.py
- [[group_router.py]] - code - gateway/approval_queue/group_router.py
- [[group_router.py (GroupApprovalRouter)]] - code - gateway/approval_queue/group_router.py
- [[ingest_api models.py (ApprovalRequest)]] - code - gateway/ingest_api/models.py
- [[mock_send_message()]] - code - gateway/tests/test_group_approval_routing.py
- [[route_approval auto-detects group context when group_chat_id not explicitly pass]] - rationale - gateway/tests/test_group_approval_routing.py
- [[router()]] - code - gateway/tests/test_group_approval_routing.py
- [[router_with_sent()]] - code - gateway/tests/test_group_approval_routing.py
- [[test_group_approval_routing.py]] - code - gateway/tests/test_group_approval_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_123
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_Community 56]]
- 1 edge to [[_COMMUNITY_Community 255]]
- 1 edge to [[_COMMUNITY_Community 23]]

## Top bridge nodes
- [[group_router.py]] - degree 4, connects to 3 communities
- [[GroupApprovalRouter]] - degree 23, connects to 1 community
- [[test_group_approval_routing.py]] - degree 12, connects to 1 community
- [[TestGroupApprovalRouterContextDetection]] - degree 10, connects to 1 community
- [[TestGroupApprovalRouterDefaultSend]] - degree 6, connects to 1 community