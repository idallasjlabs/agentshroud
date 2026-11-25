---
type: community
members: 10
---

# TestUpstreamAlertDedup

**Members:** 10 nodes

## Members
- [[dot-test_failed_send_is_retried()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_patched_versions_carried_into_result()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unreadable_state_file_means_alert_again()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unwritable_state_file_is_logged_not_raised()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamAlertDedup]] - code - gateway/tests/test_daily_cve_report.py
- [[The 0605 check and the 0700 GHSA ingest share one diff; an advisory still…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[__enter__()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[__exit__()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_flaky_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[read()_4]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestUpstreamAlertDedup
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_asyncio_1]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestUpstreamAlertDedup]] - degree 8, connects to 2 communities
- [[dot-test_failed_send_is_retried()]] - degree 3, connects to 1 community
