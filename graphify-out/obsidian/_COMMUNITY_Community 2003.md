---
type: community
members: 8
---

# Community 2003

**Members:** 8 nodes

## Members
- [[.test_dedup_is_per_agent()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_failed_send_is_retried()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_patched_versions_carried_into_result()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_second_check_does_not_resend()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_unreadable_state_file_means_alert_again()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_unwritable_state_file_is_logged_not_raised()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamAlertDedup]] - code - gateway/tests/test_daily_cve_report.py
- [[The 0605 check and the 0700 GHSA ingest share one diff; an advisory     still]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2003
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 127]]
- 1 edge to [[_COMMUNITY_Community 480]]

## Top bridge nodes
- [[TestUpstreamAlertDedup]] - degree 8, connects to 1 community
- [[.test_patched_versions_carried_into_result()]] - degree 2, connects to 1 community