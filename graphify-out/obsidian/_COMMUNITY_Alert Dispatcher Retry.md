---
type: community
cohesion: 0.43
members: 8
---

# Alert Dispatcher Retry

**Cohesion:** 0.43 - moderately connected
**Members:** 8 nodes

## Members
- [[The alert must already be in alert_log before notification runs.      Before the]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[_alert()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_alert_dispatcher_retry.py]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_all_attempts_fail_logs_warning_not_error()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_backoff_called_between_attempts()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_dispatch_persists_alert_even_if_notification_fails()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_after_one_transient_failure()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_on_first_attempt()]] - code - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Alert_Dispatcher_Retry
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[test_alert_dispatcher_retry.py]] - degree 8, connects to 1 community