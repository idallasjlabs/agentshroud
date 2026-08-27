---
type: community
members: 56
---

# Community 43

**Members:** 56 nodes

## Members
- [[.send_json()]] - code - gateway/tests/test_approval_queue.py
- [[A WebSocket stand-in whose send_json never returns — models a dead     client (c]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue configuration for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue store file should persist items and status transitions.]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 cleanup_decided() must persist the removal, not just mutate     the i]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 writes go through a temp file + os.replace so a crash     mid-write c]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm]] - rationale - gateway/tests/test_approval_queue.py
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
- [[_HangingWebSocket]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[broadcast() bounds each client's send with a timeout — defense in     depth so a]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() must not remove pending items regardless of age.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should not remove decided items newer than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[cleanup_decided() should remove approvedrejected items older than threshold.]] - rationale - gateway/tests/test_approval_queue.py
- [[queue_config()]] - code - gateway/tests/test_approval_queue.py
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
TABLE source_file, type FROM #community/Community_43
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Community 24]]
- 7 edges to [[_COMMUNITY_Community 1]]
- 2 edges to [[_COMMUNITY_Community 109]]
- 1 edge to [[_COMMUNITY_Community 38]]

## Top bridge nodes
- [[test_approval_queue.py]] - degree 30, connects to 2 communities
- [[_HangingWebSocket]] - degree 8, connects to 2 communities
- [[test_broadcast_with_failed_client()]] - degree 4, connects to 2 communities
- [[test_store_persists_submit_and_decision()]] - degree 4, connects to 2 communities
- [[test_cleanup_decided_persists_removal_to_disk()]] - degree 4, connects to 2 communities