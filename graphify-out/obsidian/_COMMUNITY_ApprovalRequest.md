---
type: community
members: 130
---

# ApprovalRequest

**Members:** 130 nodes

## Members
- [[dot-__init__()_20]] - code - gateway/approval_queue/group_router.py
- [[dot-_build_group_reply_text()]] - code - gateway/approval_queue/group_router.py
- [[dot-_build_owner_dm_text()]] - code - gateway/approval_queue/group_router.py
- [[dot-_default_send()]] - code - gateway/approval_queue/group_router.py
- [[dot-extract_group_chat_id()]] - code - gateway/approval_queue/group_router.py
- [[dot-is_group_context()]] - code - gateway/approval_queue/group_router.py
- [[dot-route_approval()]] - code - gateway/approval_queue/group_router.py
- [[dot-send_json()]] - code - gateway/tests/test_approval_queue.py
- [[dot-test_both_owner_dm_and_group_notified()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_default_send_stub_returns_ok()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_dm_approval_no_group_side_effect()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_dm_approval_routes_only_to_owner()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_extract_chat_id_from_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_extract_chat_id_returns_none_for_non_group()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_group_chat_receives_thread_reply()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_is_group_context_false_for_collab_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_is_group_context_false_for_default()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_is_group_context_true_for_group_agent_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_contains_action_type()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_references_group_chat_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_receives_dm_for_group_approval()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_route_approval_auto_detects_group_context()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_router_works_without_send_fn()]] - code - gateway/tests/test_group_approval_routing.py
- [[A WebSocket stand-in whose send_json never returns — models a dead client…]] - rationale - gateway/tests/test_approval_queue.py
- [[A single group-context approval triggers both owner DM AND group reply.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Any_8]] - code
- [[ApprovalRequest]] - code - gateway/ingest_api/models.py
- [[Build the group thread reply notification text.]] - rationale - gateway/approval_queue/group_router.py
- [[Build the owner DM notification text.]] - rationale - gateway/approval_queue/group_router.py
- [[Cover the no-op _default_send stub used when no transport is injected.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Create approval queue configuration for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[DM approval must not send any message to a group chat ID.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[DM-context approvals must not trigger group notifications.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Extract the raw chat_id from a group-{chat_id} agent_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Extract the raw chat_id from a group-{chat_id} agent_id. Returns None if the…]] - rationale - gateway/approval_queue/group_router.py
- [[Group-aware Approval Router (v1.2.0 Workstream A). When an approval request…]] - rationale - gateway/approval_queue/group_router.py
- [[GroupApprovalRouter]] - code - gateway/approval_queue/group_router.py
- [[GroupApprovalRouter must correctly distinguish group vs DM context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[GroupApprovalRouter wired with a mock Telegram send function.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[GroupApprovalRouter._default_send returns {ok True} without raising.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Mock async Telegram sendMessage to capture DM and group notifications.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[No-op send stub — used when no transport is injected.]] - rationale - gateway/approval_queue/group_router.py
- [[Owner DM message text must reference the originating group chat_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner DM must describe the action_type that requires approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner must receive a DM when an approval originates from a group chat.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue store file should persist items and status transitions.]] - rationale - gateway/tests/test_approval_queue.py
- [[Request for human approval of a sensitive action Submitted by an agent when…]] - rationale - gateway/ingest_api/models.py
- [[Return (router, sent_list) tuple for assertion convenience.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Return True if agent_id represents a Telegram group workspace.]] - rationale - gateway/approval_queue/group_router.py
- [[Route an approval notification to the appropriate recipients. Routing logic -…]] - rationale - gateway/approval_queue/group_router.py
- [[Router with no send_message_fn uses the default stub (no network calls).]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Routes approval notifications to owner DM and (optionally) group thread. Args…]] - rationale - gateway/approval_queue/group_router.py
- [[SCRUM-110 cleanup_decided() must persist the removal, not just mutate the in-…]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 writes go through a temp file + os.replace so a crash mid-write can…]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.…]] - rationale - gateway/tests/test_approval_queue.py
- [[TDD — Workstream A (v1.2.0) Group approval routing. Tests that - When an…]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Test WebSocket client connection]] - rationale - gateway/tests/test_approval_queue.py
- [[Test WebSocket client disconnection]] - rationale - gateway/tests/test_approval_queue.py
- [[Test approving a pending request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test broadcast handles failed client sends]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on already-decided request raises ValueError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on an expired request raises ValueError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on nonexistent request raises KeyError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting a specific item by ID]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting all pending requests]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting nonexistent item returns None]] - rationale - gateway/tests/test_approval_queue.py
- [[Test rejecting a pending request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test submitting an approval request]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that concurrent decision attempts are handled correctly]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that get_pending excludes decided requests]] - rationale - gateway/tests/test_approval_queue.py
- [[Test that requests expire after timeout]] - rationale - gateway/tests/test_approval_queue.py
- [[TestDMApprovalOwnerOnly]] - code - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalOwnerDM]] - code - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalRouterContextDetection]] - code - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalRouterDefaultSend]] - code - gateway/tests/test_group_approval_routing.py
- [[Tests for approval queue]] - rationale - gateway/tests/test_approval_queue.py
- [[The originating group chat must receive a thread-reply notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[When group_chat_id is None, only the owner receives a notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[_HangingWebSocket]] - code - gateway/tests/test_approval_queue.py
- [[_send()]] - code - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'collab-' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id starting with 'group-' is recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[agent_id='default' is NOT recognized as group context.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[asyncio_10]] - code
- [[asyncio_11]] - code
- [[broadcast() bounds each client's send with a timeout — defense in depth so an…]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() must not remove pending items regardless of age.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should not remove decided items newer than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should remove approvedrejected items older than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[decide_approve()]] - code - gateway/tests/test_approval_queue.py
- [[decide_reject()]] - code - gateway/tests/test_approval_queue.py
- [[extract_group_chat_id returns None for non-group agent IDs.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[fixture_16]] - code
- [[fixture_17]] - code
- [[group_router.py]] - code - gateway/approval_queue/group_router.py
- [[mock_send_message()]] - code - gateway/tests/test_group_approval_routing.py
- [[owner_chat_id receives a DM notification for every group-context approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[queue_config()]] - code - gateway/tests/test_approval_queue.py
- [[route_approval auto-detects group context when group_chat_id not explicitly…]] - rationale - gateway/tests/test_group_approval_routing.py
- [[router()]] - code - gateway/tests/test_group_approval_routing.py
- [[router_with_sent()]] - code - gateway/tests/test_group_approval_routing.py
- [[test_approval_queue.py]] - code - gateway/tests/test_approval_queue.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - code - gateway/tests/test_approval_queue.py
- [[test_broadcast_with_failed_client()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_keeps_pending_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_keeps_recent_decided_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_persists_removal_to_disk()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_removes_old_decided_items()]] - code - gateway/tests/test_approval_queue.py
- [[test_concurrent_decisions()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_already_decided()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_approval_approve()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_approval_reject()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_expired_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_nonexistent_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item_nonexistent()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending_excludes_decided()]] - code - gateway/tests/test_approval_queue.py
- [[test_group_approval_routing.py]] - code - gateway/tests/test_group_approval_routing.py
- [[test_persist_pending_store_writes_atomically()]] - code - gateway/tests/test_approval_queue.py
- [[test_request_expiration()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_persists_submit_and_decision()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_approval_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_connect()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_disconnect()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalRequest
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 10 edges to [[_COMMUNITY_ApprovalStore]]
- 10 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 9 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[ApprovalRequest]] - degree 74, connects to 6 communities
- [[test_approval_queue.py]] - degree 35, connects to 3 communities
- [[test_group_approval_routing.py]] - degree 12, connects to 1 community
- [[test_cleanup_decided_persists_removal_to_disk()]] - degree 5, connects to 1 community
- [[test_persist_pending_store_writes_atomically()]] - degree 5, connects to 1 community
