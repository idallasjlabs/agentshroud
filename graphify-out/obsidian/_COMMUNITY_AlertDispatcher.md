---
type: community
members: 44
---

# AlertDispatcher

**Members:** 44 nodes

## Members
- [[dot-__init__()_169]] - code - gateway/security/alert_dispatcher.py
- [[dot-_format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[dot-cleanup_seen()]] - code - gateway/security/alert_dispatcher.py
- [[dot-dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_stats()_11]] - code - gateway/security/alert_dispatcher.py
- [[dot-test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_concurrent_dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[AlertDispatcher]] - code - gateway/security/alert_dispatcher.py
- [[Any_65]] - code
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Concurrent alert dispatch shouldn't lose or corrupt alerts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dispatch an alert based on severity. Args alert Alert dict with at least…]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatches security alerts with dedup and rate limiting.]] - rationale - gateway/security/alert_dispatcher.py
- [[Duplicate alerts should be deduplicated.]] - rationale - gateway/tests/test_security_audit.py
- [[Format alert as human-readable message.]] - rationale - gateway/security/alert_dispatcher.py
- [[Get buffered alerts for daily digest. Args clear Clear buffer after…]] - rationale - gateway/security/alert_dispatcher.py
- [[Get dispatcher statistics.]] - rationale - gateway/security/alert_dispatcher.py
- [[POST alert to apialerts with bounded retry + backoff. Returns True on first…]] - rationale - gateway/security/alert_dispatcher.py
- [[Path_57]] - code
- [[Path_58]] - code
- [[Remove expired entries from seen IDs cache. Returns Number of entries removed.]] - rationale - gateway/security/alert_dispatcher.py
- [[Retry behavior of AlertDispatcher._send_notification (kaizen fix). Before this…]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[The alert must already be in alert_log before notification runs. Before the…]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[_alert()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dispatcher()_1]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[fixture_113]] - code
- [[flaky()_1]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_alert_dispatcher_retry.py]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_all_attempts_fail_logs_warning_not_error()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_backoff_called_between_attempts()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_dispatch_persists_alert_even_if_notification_fails()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_after_one_transient_failure()]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[test_succeeds_on_first_attempt()]] - code - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ContainerSnapshot]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestAlertDispatcher]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[AlertDispatcher]] - degree 29, connects to 8 communities
- [[alert_dispatcher.py]] - degree 4, connects to 2 communities
- [[dot-test_alert_dispatcher_concurrent_dispatch()]] - degree 4, connects to 1 community
- [[dot-test_alert_dedup()]] - degree 3, connects to 1 community
- [[dot-test_alert_dispatcher_init()]] - degree 2, connects to 1 community
