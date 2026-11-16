---
type: community
members: 52
---

# Community 557

**Members:** 52 nodes

## Members
- [[.__init__()_68]] - code - gateway/security/alert_dispatcher.py
- [[._format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[._is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[._is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[._log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[._send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[.cleanup_seen()]] - code - gateway/security/alert_dispatcher.py
- [[.dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[.get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[.get_stats()_12]] - code - gateway/security/alert_dispatcher.py
- [[.test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_concurrent_dispatch()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[.test_canary_system_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_context_guard_session_isolation_under_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_health_report_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_prompt_guard_concurrent_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_trust_manager_rapid_updates()]] - code - gateway/tests/test_security_audit_advanced.py
- [[AlertDispatcher]] - code - gateway/security/alert_dispatcher.py
- [[Any_41]] - code - gateway/security/alert_dispatcher.py
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Concurrent alert dispatch shouldn't lose or corrupt alerts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Concurrent prompt scans shouldn't interfere with each other.]] - rationale - gateway/tests/test_security_audit_advanced.py
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
- [[Rapid trust score updates shouldn't corrupt state.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Remove expired entries from seen IDs cache.          Returns             Number]] - rationale - gateway/security/alert_dispatcher.py
- [[Sessions shouldn't leak data under concurrent access.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test audit chain integrity and tamper detection.]] - rationale - gateway/tests/test_security_audit.py
- [[Test thread safety and race conditions in security modules.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestAuditTrail_1]] - code - gateway/tests/test_security_audit.py
- [[TestConcurrency_1]] - code - gateway/tests/test_security_audit_advanced.py
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
- 21 edges to [[_COMMUNITY_Community 72]]
- 21 edges to [[_COMMUNITY_Community 0]]
- 11 edges to [[_COMMUNITY_Community 52]]
- 9 edges to [[_COMMUNITY_Community 809]]
- 7 edges to [[_COMMUNITY_Community 121]]
- 6 edges to [[_COMMUNITY_Community 84]]
- 5 edges to [[_COMMUNITY_Community 102]]
- 4 edges to [[_COMMUNITY_Community 185]]
- 4 edges to [[_COMMUNITY_Community 131]]
- 3 edges to [[_COMMUNITY_Community 220]]
- 2 edges to [[_COMMUNITY_Community 151]]
- 2 edges to [[_COMMUNITY_Community 793]]
- 2 edges to [[_COMMUNITY_Community 152]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Community 31]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 113]]
- 1 edge to [[_COMMUNITY_Community 394]]
- 1 edge to [[_COMMUNITY_Community 140]]
- 1 edge to [[_COMMUNITY_Community 625]]
- 1 edge to [[_COMMUNITY_Community 943]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 684]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 532]]
- 1 edge to [[_COMMUNITY_Community 5]]

## Top bridge nodes
- [[AlertDispatcher]] - degree 77, connects to 17 communities
- [[TestAuditTrail_1]] - degree 43, connects to 16 communities
- [[TestConcurrency_1]] - degree 29, connects to 10 communities
- [[.__init__()_68]] - degree 3, connects to 1 community
- [[.test_context_guard_session_isolation_under_load()]] - degree 3, connects to 1 community