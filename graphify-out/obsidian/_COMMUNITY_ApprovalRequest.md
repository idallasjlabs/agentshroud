---
type: community
cohesion: 0.08
members: 27
---

# ApprovalRequest

**Cohesion:** 0.08 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-send_json()]] - code - gateway/tests/test_approval_queue.py
- [[A WebSocket stand-in whose send_json never returns — models a dead     client (c]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue configuration for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Create approval queue instance for testing]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue should restore persisted items from store file on startup.]] - rationale - gateway/tests/test_approval_queue.py
- [[Queue store file should persist items and status transitions.]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 cleanup_decided() must persist the removal, not just mutate     the i]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-110 writes go through a temp file + os.replace so a crash     mid-write c]] - rationale - gateway/tests/test_approval_queue.py
- [[SCRUM-154 a dead WebSocket client must never wedge the approval lock.      subm]] - rationale - gateway/tests/test_approval_queue.py
- [[Test WebSocket client connection]] - rationale - gateway/tests/test_approval_queue.py
- [[Test deciding on nonexistent request raises KeyError]] - rationale - gateway/tests/test_approval_queue.py
- [[Test getting nonexistent item returns None]] - rationale - gateway/tests/test_approval_queue.py
- [[_HangingWebSocket]] - code - gateway/tests/test_approval_queue.py
- [[approval_queue()]] - code - gateway/tests/test_approval_queue.py
- [[broadcast() bounds each client's send with a timeout — defense in     depth so a]] - rationale - gateway/tests/test_approval_queue.py
- [[queue_config()]] - code - gateway/tests/test_approval_queue.py
- [[test_approval_queue.py]] - code - gateway/tests/test_approval_queue.py
- [[test_broadcast_does_not_hang_forever_on_dead_client()]] - code - gateway/tests/test_approval_queue.py
- [[test_cleanup_decided_persists_removal_to_disk()]] - code - gateway/tests/test_approval_queue.py
- [[test_decide_nonexistent_request()]] - code - gateway/tests/test_approval_queue.py
- [[test_get_item_nonexistent()]] - code - gateway/tests/test_approval_queue.py
- [[test_persist_pending_store_writes_atomically()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_persists_submit_and_decision()]] - code - gateway/tests/test_approval_queue.py
- [[test_store_restores_items_on_init()]] - code - gateway/tests/test_approval_queue.py
- [[test_submit_does_not_deadlock_on_hung_websocket_client()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_connect()]] - code - gateway/tests/test_approval_queue.py
- [[test_websocket_disconnect()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalRequest
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 10 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[test_approval_queue.py]] - degree 30, connects to 3 communities
- [[_HangingWebSocket]] - degree 8, connects to 2 communities
- [[test_cleanup_decided_persists_removal_to_disk()]] - degree 4, connects to 2 communities
- [[test_persist_pending_store_writes_atomically()]] - degree 4, connects to 2 communities
- [[test_store_persists_submit_and_decision()]] - degree 4, connects to 2 communities
