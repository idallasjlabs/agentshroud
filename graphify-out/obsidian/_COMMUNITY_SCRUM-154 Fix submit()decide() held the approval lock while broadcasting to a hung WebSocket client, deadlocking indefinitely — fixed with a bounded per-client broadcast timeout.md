---
type: community
cohesion: 1.00
members: 1
---

# SCRUM-154 Fix: submit()/decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[SCRUM-154 Fix submit()decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout]] - rationale - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SCRUM-154_Fix_submit/decide_held_the_approval_lock_while_broadcasting_to_a_hung_WebSocket_client_deadlocking_indefinitely__fixed_with_a_bounded_per-client_broadcast_timeout
SORT file.name ASC
```
