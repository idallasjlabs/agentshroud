---
type: community
members: 13
---

# test_daily_cve_report.py (3)

**Members:** 13 nodes

## Members
- [[dot-test_already_ingested_helper_swallows_read_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_when_already_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[A disk-write failure on the sentinel is swallowed; in-memory guard set.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A raised per-agent check error is ISOLATED — the ingest still completes.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[After sleeping, if the day is now marked done, the loop skips ingest.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[First iteration ingests + records; second sees dedup and skips.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If already ingested today, the loop bumps to tomorrow and never ingests.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestScheduler]] - code - gateway/tests/test_daily_cve_report.py
- [[_already_ingested_ghsa_today returns False on a malformed sentinel.]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy_3
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py (2)]]

## Top bridge nodes
- [[dot-test_runs_ingest_records_then_skips_next_iteration()]] - degree 4, connects to 2 communities
- [[TestGhsaIngestScheduler]] - degree 7, connects to 1 community
- [[dot-test_ingest_records_even_when_disk_write_fails()]] - degree 3, connects to 1 community
- [[dot-test_per_agent_check_error_is_isolated_not_fatal()]] - degree 3, connects to 1 community
- [[dot-test_skips_ingest_when_marked_done_after_wake()]] - degree 3, connects to 1 community
