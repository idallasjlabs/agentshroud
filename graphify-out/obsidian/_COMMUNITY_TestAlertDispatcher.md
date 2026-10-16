---
type: community
cohesion: 0.29
members: 13
---

# TestAlertDispatcher

**Cohesion:** 0.29 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-_make_dispatcher()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_cleanup_seen()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_critical_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_dedup()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_digest()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_get_stats()_2]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_high_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_log_to_jsonl()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_low_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_medium_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_notify_failure()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_rate_limiting()]] - code - gateway/tests/test_security_toolchain.py
- [[TestAlertDispatcher]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]

## Top bridge nodes
- [[TestAlertDispatcher]] - degree 14, connects to 2 communities
- [[dot-_make_dispatcher()]] - degree 13, connects to 1 community
