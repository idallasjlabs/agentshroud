---
type: community
cohesion: 0.03
members: 84
---

# ApprovalRequest

**Cohesion:** 0.03 - loosely connected
**Members:** 84 nodes

## Members
- [[dot-send_json()_1]] - code - gateway/tests/test_approval_queue.py
- [[dot-test_both_owner_dm_and_group_notified()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_dm_approval_no_group_side_effect()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_dm_approval_routes_only_to_owner()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_group_chat_receives_thread_reply()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_contains_action_type()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_references_group_chat_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_receives_dm_for_group_approval()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_timeout_auto_deny()]] - code - gateway/tests/test_enhanced_approval.py
- [[A WebSocket stand-in whose send_json never returns — models a dead     client (c]] - rationale - gateway/tests/test_approval_queue.py
- [[A single group-context approval triggers both owner DM AND group reply.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[ApprovalRequest_5]] - code - gateway/ingest_api/models.py
- [[Create approval queue configuration for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[DM approval must not send any message to a group chat ID.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[DM-context approvals must not trigger group notifications.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Expired request raises ValueError on decide.]] - rationale - gateway/tests/test_approval_stress.py
- [[Owner DM message text must reference the originating group chat_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner DM must describe the action_type that requires approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner must receive a DM when an approval originates from a group chat.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue store file should persist items and status transitions.]] - rationale - gateway/tests/test_approval_queue.py
- [[Request for human approval of a sensitive action      Submitted by an agent when]] - rationale - gateway/ingest_api/models.py
- [[SCRUM-110 cleanup_decided() must persist the removal, not just mutate     the i]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 writes go through a temp file + os.replace so a crash     mid-write c]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm_1]] - rationale - gateway/tests/test_approval_queue.py
- [[Test WebSocket client connection]] - rationale - gateway/tests/test_approval_queue.py
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
- [[Test timeout with auto-deny.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestDMApprovalOwnerOnly]] - code - gateway/tests/test_group_approval_routing.py
- [[TestGroupApprovalOwnerDM]] - code - gateway/tests/test_group_approval_routing.py
- [[The originating group chat must receive a thread-reply notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[When group_chat_id is None, only the owner receives a notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[_HangingWebSocket_1]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()_1]] - code - gateway/tests/test_approval_queue.py
- [[broadcast() bounds each client's send with a timeout — defense in     depth so a]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() must not remove pending items regardless of age.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should not remove decided items newer than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should remove approvedrejected items older than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[owner_chat_id receives a DM notification for every group-context approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[queue_config()]] - code - gateway/tests/test_approval_queue.py
- [[test_approval_queue.py]] - code - gateway/tests/test_approval_queue.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()_1]] - code - gateway/tests/test_approval_queue.py
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
- [[test_enhanced_tool_call_medium_not_gated()]] - code - gateway/tests/test_mfa_guard.py
- [[test_get_item()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item_nonexistent()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_pending_excludes_decided()]] - code - gateway/tests/test_approval_queue.py
- [[test_persist_pending_store_writes_atomically()]] - code - gateway/tests/test_approval_queue.py
- [[test_request_expiration()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_persists_submit_and_decision()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_approval_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()_1]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_connect()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_disconnect()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalRequest
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 13 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 8 edges to [[_COMMUNITY_ApprovalQueueItem]]
- 8 edges to [[_COMMUNITY_DataLedger]]
- 6 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_ingest_apimodels.py]]
- 1 edge to [[_COMMUNITY_ThreatAssessment]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[ApprovalRequest_5]] - degree 79, connects to 9 communities
- [[TestApprovalTimeout]] - degree 9, connects to 3 communities
- [[test_approval_queue.py]] - degree 30, connects to 2 communities
- [[_HangingWebSocket_1]] - degree 8, connects to 2 communities
- [[test_broadcast_with_failed_client()]] - degree 4, connects to 2 communities
