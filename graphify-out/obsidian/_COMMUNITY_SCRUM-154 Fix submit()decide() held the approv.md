---
type: community
cohesion: 1.00
members: 1
---

# SCRUM-154 Fix: submit()/decide() held the approv

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[SCRUM-154 Fix submit()decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout]] - rationale - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SCRUM-154_Fix_submit/decide_held_the_approv
SORT file.name ASC
```
