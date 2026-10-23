---
type: community
cohesion: 0.14
members: 14
---

# OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-test_dedup_is_per_agent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_is_retried()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_patched_versions_carried_into_result()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_second_check_does_not_resend()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unreadable_state_file_means_alert_again()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unwritable_state_file_is_logged_not_raised()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamAlertDedup]] - code - gateway/tests/test_daily_cve_report.py
- [[The 0605 check and the 0700 GHSA ingest share one diff; an advisory still…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[__enter__()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[__exit__()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_20]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_21]] - code - gateway/tests/test_daily_cve_report.py
- [[_flaky_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[read()_3]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_format_cve_report() (2)]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]

## Top bridge nodes
- [[dot-test_dedup_is_per_agent()]] - degree 4, connects to 2 communities
- [[dot-test_second_check_does_not_resend()]] - degree 4, connects to 2 communities
- [[TestUpstreamAlertDedup]] - degree 8, connects to 1 community
- [[dot-test_failed_send_is_retried()]] - degree 3, connects to 1 community
