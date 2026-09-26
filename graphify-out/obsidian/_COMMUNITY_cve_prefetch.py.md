---
type: community
cohesion: 0.40
members: 5
---

# cve_prefetch.py

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_clean_when_installed_not_running()_2]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_run_when_not_installed()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_report_mtime_timestamp()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_running_without_report()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestClamavSummary]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/cve_prefetchpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_wazuh_client.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]

## Top bridge nodes
- [[TestClamavSummary]] - degree 5, connects to 1 community
- [[.test_running_report_mtime_timestamp()]] - degree 2, connects to 1 community