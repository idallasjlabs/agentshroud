---
type: community
members: 31
---

# AlertDispatcher

**Members:** 31 nodes

## Members
- [[dot-__init__()_174]] - code - gateway/security/alert_dispatcher.py
- [[dot-_format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[dot-cleanup_seen()]] - code - gateway/security/alert_dispatcher.py
- [[dot-dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_stats()_12]] - code - gateway/security/alert_dispatcher.py
- [[dot-test_alert_dedup()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_alert_dispatcher_write()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_canary_system_importable()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_health_report_importable()]] - code - gateway/tests/test_security_audit.py
- [[AlertDispatcher]] - code - gateway/security/alert_dispatcher.py
- [[Any_65]] - code
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatch an alert based on severity. Args alert Alert dict with at least…]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatches security alerts with dedup and rate limiting.]] - rationale - gateway/security/alert_dispatcher.py
- [[Duplicate alerts should be deduplicated.]] - rationale - gateway/tests/test_security_audit.py
- [[Format alert as human-readable message.]] - rationale - gateway/security/alert_dispatcher.py
- [[Get buffered alerts for daily digest. Args clear Clear buffer after…]] - rationale - gateway/security/alert_dispatcher.py
- [[Get dispatcher statistics.]] - rationale - gateway/security/alert_dispatcher.py
- [[POST alert to apialerts with bounded retry + backoff. Returns True on first…]] - rationale - gateway/security/alert_dispatcher.py
- [[Path_57]] - code
- [[Remove expired entries from seen IDs cache. Returns Number of entries removed.]] - rationale - gateway/security/alert_dispatcher.py
- [[Test audit chain integrity and tamper detection.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuditTrail_2]] - code - gateway/tests/test_security_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_DriftDetector]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_test_alert_dispatcher_retry.py]]
- 2 edges to [[_COMMUNITY_TestAlertDispatcher]]
- 2 edges to [[_COMMUNITY_TestConcurrency]]
- 1 edge to [[_COMMUNITY_ContainerSnapshot]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[AlertDispatcher]] - degree 29, connects to 9 communities
- [[TestAuditTrail_2]] - degree 13, connects to 3 communities
