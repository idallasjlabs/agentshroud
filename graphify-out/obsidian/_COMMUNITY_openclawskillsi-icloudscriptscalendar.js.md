---
type: community
cohesion: 0.31
members: 10
---

# openclaw/skills/i-icloud/scripts/calendar.js

**Cohesion:** 0.31 - loosely connected
**Members:** 10 nodes

## Members
- [[Path_23]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[The alert must already be in alert_log before notification runs.      Before the]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[_alert()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[dispatcher()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_alert_dispatcher_retry.py]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_all_attempts_fail_logs_warning_not_error()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_backoff_called_between_attempts()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_dispatch_persists_alert_even_if_notification_fails()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_after_one_transient_failure()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_on_first_attempt()]] - code - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/openclaw/skills/i-icloud/scripts/calendarjs
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[test_alert_dispatcher_retry.py]] - degree 8, connects to 1 community
- [[dispatcher()]] - degree 3, connects to 1 community
- [[Path_23]] - degree 2, connects to 1 community