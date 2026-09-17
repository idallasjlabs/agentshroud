---
type: community
cohesion: 0.12
members: 19
---

# .test_gives_up_and_marks_sent_after_max_retries(

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_skip_dirs_flag_when_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_retries_on_failed_send_before_giving_up()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skip_dirs_added_to_command()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCveReportSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivySkipDirs]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_run()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[_sleep()_9]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[now()_9]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_gives_up_and_marks_sent_after_max_retries
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_asyncio]]
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 3 edges to [[_COMMUNITY__sleep()]]

## Top bridge nodes
- [[.test_gives_up_and_marks_sent_after_max_retries()]] - degree 9, connects to 3 communities
- [[.test_retries_on_failed_send_before_giving_up()]] - degree 9, connects to 3 communities
- [[.test_successful_send_marks_sent_immediately_no_retry()]] - degree 8, connects to 3 communities
- [[_fake_run()_3]] - degree 6, connects to 1 community
- [[TestCveReportSchedulerRetry]] - degree 4, connects to 1 community