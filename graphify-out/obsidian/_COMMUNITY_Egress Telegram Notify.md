---
type: community
cohesion: 0.67
members: 3
---

# Egress Telegram Notify

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.test_handle_callback_approve_1h()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[.test_handle_callback_approve_4h()]] - code - gateway/tests/test_egress_telegram_notify.py
- [[Test handling 1-hour time-limited approval callback.]] - rationale - gateway/tests/test_egress_telegram_notify.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Telegram_Notify
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Egress Telegram Notify]]

## Top bridge nodes
- [[.test_handle_callback_approve_1h()]] - degree 2, connects to 1 community
- [[.test_handle_callback_approve_4h()]] - degree 2, connects to 1 community