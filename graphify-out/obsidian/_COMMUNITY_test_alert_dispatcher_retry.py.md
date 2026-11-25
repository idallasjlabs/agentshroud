---
type: community
members: 14
---

# test_alert_dispatcher_retry.py

**Members:** 14 nodes

## Members
- [[Path_2]] - code
- [[Retry behavior of AlertDispatcher._send_notification (kaizen fix). Before this…]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[The alert must already be in alert_log before notification runs. Before the…]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[_alert()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[dispatcher()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[fixture_11]] - code
- [[flaky()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_alert_dispatcher_retry.py]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_all_attempts_fail_logs_warning_not_error()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_backoff_called_between_attempts()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_dispatch_persists_alert_even_if_notification_fails()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_after_one_transient_failure()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_on_first_attempt()]] - code - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_alert_dispatcher_retrypy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[alert_dispatcher.py]] - degree 4, connects to 3 communities
- [[test_alert_dispatcher_retry.py]] - degree 10, connects to 1 community
- [[dispatcher()]] - degree 4, connects to 1 community
