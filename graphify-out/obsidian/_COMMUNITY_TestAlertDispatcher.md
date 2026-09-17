---
type: community
cohesion: 0.14
members: 21
---

# TestAlertDispatcher

**Cohesion:** 0.14 - loosely connected
**Members:** 21 nodes

## Members
- [[._make_dispatcher()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_cleanup_seen()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_critical_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_dedup()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_digest()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_get_stats()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_high_alert_notified()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_log_to_jsonl()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_low_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_medium_alert_buffered()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_notify_failure()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_rate_limiting()]] - code - gateway/tests/test_security_toolchain.py
- [[TestAlertDispatcher]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]

## Top bridge nodes
- [[TestAlertDispatcher]] - degree 13, connects to 1 community
- [[TestClamAVParser]] - degree 8, connects to 1 community