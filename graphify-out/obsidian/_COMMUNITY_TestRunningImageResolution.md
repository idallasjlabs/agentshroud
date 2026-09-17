---
type: community
cohesion: 0.33
members: 6
---

# TestRunningImageResolution

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_prefers_running_image_over_configured_tag()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_running_image_parses_docker_inspect_stdout()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_running_image_returns_none_on_inspect_failure()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_running_image_returns_none_when_docker_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[Regression guard (2026-08-30) the report scanned latest tags         while dep]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestRunningImageResolution_1]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRunningImageResolution
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestRunningImageResolution_1]] - degree 5, connects to 1 community