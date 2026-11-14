---
type: community
members: 53
---

# Community 557

**Members:** 53 nodes

## Members
- [[.__init__()_68]] - code - gateway/security/alert_dispatcher.py
- [[._format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[._is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[._is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[._log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[._make_dispatcher()]] - code - gateway/tests/test_security_toolchain.py
- [[._send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[.cleanup_seen()]] - code - gateway/security/alert_dispatcher.py
- [[.dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[.get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[.get_stats()_12]] - code - gateway/security/alert_dispatcher.py
- [[.test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_concurrent_dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[.test_cleanup_seen()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_critical_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_dedup()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_digest()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_stats()_2]] - code - gateway/tests/test_security_toolchain.py
- [[.test_high_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_log_to_jsonl()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_low_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_medium_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_notify_failure()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_rate_limiting()]] - code - gateway/tests/test_security_toolchain.py
- [[AlertDispatcher]] - code - gateway/security/alert_dispatcher.py
- [[Any_41]] - code - gateway/security/alert_dispatcher.py
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Concurrent alert dispatch shouldn't lose or corrupt alerts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dispatch an alert based on severity.          Args             alert Alert dic]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatches security alerts with dedup and rate limiting.]] - rationale - gateway/security/alert_dispatcher.py
- [[Duplicate alerts should be deduplicated.]] - rationale - gateway/tests/test_security_audit.py
- [[Format alert as human-readable message.]] - rationale - gateway/security/alert_dispatcher.py
- [[Get buffered alerts for daily digest.          Args             clear Clear bu]] - rationale - gateway/security/alert_dispatcher.py
- [[Get dispatcher statistics.]] - rationale - gateway/security/alert_dispatcher.py
- [[Kaizen Fix AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14week) at ERROR level]] - rationale - gateway/tests/test_alert_dispatcher_retry.py
- [[POST alert to apialerts with bounded retry + backoff.          Returns True on]] - rationale - gateway/security/alert_dispatcher.py
- [[Path_7]] - code - gateway/security/alert_dispatcher.py
- [[Path_25]] - code - gateway/tests/test_alert_dispatcher_retry.py
- [[Remove expired entries from seen IDs cache.          Returns             Number]] - rationale - gateway/security/alert_dispatcher.py
- [[TestAlertDispatcher]] - code - gateway/tests/test_security_toolchain.py
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
TABLE source_file, type FROM #community/Community_557
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 185]]
- 11 edges to [[_COMMUNITY_Community 0]]
- 10 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 162]]
- 4 edges to [[_COMMUNITY_Community 148]]
- 4 edges to [[_COMMUNITY_Community 131]]
- 3 edges to [[_COMMUNITY_Community 41]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 365]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 113]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 235]]
- 1 edge to [[_COMMUNITY_Community 128]]
- 1 edge to [[_COMMUNITY_Community 479]]
- 1 edge to [[_COMMUNITY_Community 5]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 9]]

## Top bridge nodes
- [[AlertDispatcher]] - degree 77, connects to 19 communities
- [[TestAlertDispatcher]] - degree 14, connects to 1 community
- [[.__init__()_68]] - degree 3, connects to 1 community
- [[.test_alert_dedup()]] - degree 3, connects to 1 community
- [[.test_alert_dispatcher_concurrent_dispatch()]] - degree 3, connects to 1 community