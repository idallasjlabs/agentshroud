---
type: community
members: 79
---

# ApprovalQueueConfig (4)

**Members:** 79 nodes

## Members
- [[dot-_notify_telegram()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_schedule_timeout()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-_timeout_request()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-broadcast()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-decide()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_item()_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_pending()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_policy_for_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-get_tool_risk_tier()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-initialize()_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-requires_approval()]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-submit()_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-submit_tool_request()_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[dot-test_100_concurrent_submissions()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_both_owner_dm_and_group_notified()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_concurrent_submit_and_decide()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_double_decide_raises()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_expired_request_cannot_be_decided()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_get_pending_expires_stale()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_group_chat_receives_thread_reply()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_contains_action_type()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_dm_references_group_chat_id()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_owner_receives_dm_for_group_approval()]] - code - gateway/tests/test_group_approval_routing.py
- [[dot-test_store_expires_old_items()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_persists_across_reopen()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_save_and_load()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_store_update_status()]] - code - gateway/tests/test_approval_stress.py
- [[dot-test_timeout_auto_deny()]] - code - gateway/tests/test_enhanced_approval.py
- [[100 concurrent approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[A pending approval request in the queue]] - rationale - gateway/ingest_api/models.py
- [[A single group-context approval triggers both owner DM AND group reply.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Add an action to the approval queue with policy-based timeout.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Any_64]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_2]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalQueueItem_3]] - code - gateway/ingest_api/models.py
- [[ApprovalRequest_3]] - code - gateway/approval_queue/enhanced_queue.py
- [[ApprovalRequest_4]] - code - gateway/ingest_api/models.py
- [[Auto-expire old requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[Check if a tool requires approval based on risk tier and policy.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Deciding on already-decided request raises ValueError.]] - rationale - gateway/tests/test_approval_stress.py
- [[Expired request raises ValueError on decide.]] - rationale - gateway/tests/test_approval_stress.py
- [[Fetch a single queue item by ID.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get all pending approval items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the policy for a risk tier.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Get the risk tier for a tool.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Handle timeout for a pending request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Initialize the store and restore pending items.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Items saved to store can be reloaded.]] - rationale - gateway/tests/test_approval_stress.py
- [[Items survive store closereopen cycle.]] - rationale - gateway/tests/test_approval_stress.py
- [[Owner DM message text must reference the originating group chat_id.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner DM must describe the action_type that requires approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Owner must receive a DM when an approval originates from a group chat.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Process an approval decision.          IEC 62443 FR1 approving a high-risk acti]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Queue persistence across restart.]] - rationale - gateway/tests/test_approval_stress.py
- [[Request for human approval of a sensitive action      Submitted by an agent when]] - rationale - gateway/ingest_api/models.py
- [[Schedule a timeout task for a request.]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send Telegram notification for approval requests.          Sends a formatted mes]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Send a JSON message to all connected WebSocket clients.          SCRUM-154 boun]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Status updates persist.]] - rationale - gateway/tests/test_approval_stress.py
- [[Store marks expired items on load.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit 100 requests concurrently — all should succeed.]] - rationale - gateway/tests/test_approval_stress.py
- [[Submit a tool call request for approval.          Args             tool_name T]] - rationale - gateway/approval_queue/enhanced_queue.py
- [[Submit and decide requests concurrently.]] - rationale - gateway/tests/test_approval_stress.py
- [[Test timeout with auto-deny.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestApprovalStorePersistence]] - code - gateway/tests/test_approval_stress.py
- [[TestApprovalTimeout]] - code - gateway/tests/test_approval_stress.py
- [[TestAutoExpire]] - code - gateway/tests/test_approval_stress.py
- [[TestConcurrentApprovalRequests]] - code - gateway/tests/test_approval_stress.py
- [[TestGroupApprovalOwnerDM]] - code - gateway/tests/test_group_approval_routing.py
- [[The originating group chat must receive a thread-reply notification.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[Timeout handling for approval requests.]] - rationale - gateway/tests/test_approval_stress.py
- [[ToolRiskPolicy_1]] - code - gateway/approval_queue/enhanced_queue.py
- [[approval.py]] - code - gateway/ingest_api/routes/approval.py
- [[get_pending should expire stale items.]] - rationale - gateway/tests/test_approval_stress.py
- [[owner_chat_id receives a DM notification for every group-context approval.]] - rationale - gateway/tests/test_group_approval_routing.py
- [[queue()]] - code - gateway/tests/test_approval_stress.py
- [[store()_1]] - code - gateway/tests/test_approval_stress.py
- [[store.py]] - code - gateway/approval_queue/store.py
- [[test_approval_stress.py]] - code - gateway/tests/test_approval_stress.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_4
SORT file.name ASC
```

## Connections to other communities
- 66 edges to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 19 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 14 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 11 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 4 edges to [[_COMMUNITY_Mac App Discovery Skill (2)]]
- 4 edges to [[_COMMUNITY_create_auth_dependency (3)]]
- 3 edges to [[_COMMUNITY_Request (2)]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py (2)]]
- 2 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_Error Index]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_dashboard.py (2)]]
- 1 edge to [[_COMMUNITY_Restart Procedure (3)]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[ApprovalRequest_4]] - degree 79, connects to 8 communities
- [[approval.py]] - degree 15, connects to 6 communities
- [[ApprovalQueueItem_3]] - degree 30, connects to 5 communities
- [[store.py]] - degree 7, connects to 5 communities
- [[ApprovalQueueItem_2]] - degree 12, connects to 2 communities
