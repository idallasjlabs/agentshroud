---
type: community
members: 10
---

# §1 — Re-run of Prior Scenarios

**Members:** 10 nodes

## Members
- [[Path_67]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[The alert must already be in alert_log before notification runs.      Before the]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[_alert()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[dispatcher()_1]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_alert_dispatcher_retry.py]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_all_attempts_fail_logs_warning_not_error()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_backoff_called_between_attempts()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_dispatch_persists_alert_even_if_notification_fails()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_after_one_transient_failure()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_on_first_attempt()]] - code - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/1__Re-run_of_Prior_Scenarios
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[test_alert_dispatcher_retry.py]] - degree 8, connects to 1 community
- [[dispatcher()_1]] - degree 3, connects to 1 community
- [[Path_67]] - degree 2, connects to 1 community
