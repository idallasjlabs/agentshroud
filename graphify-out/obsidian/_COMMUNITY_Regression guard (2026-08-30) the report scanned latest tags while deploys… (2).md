---
type: community
cohesion: 0.25
members: 8
---

# Regression guard (2026-08-30): the report scanned :latest tags while deploys… (2)

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_prefers_running_image_over_configured_tag()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_parses_docker_inspect_stdout()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_returns_none_on_inspect_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_returns_none_when_docker_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[Regression guard (2026-08-30) the report scanned latest tags while deploys…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestRunningImageResolution]] - code - gateway/tests/test_daily_cve_report.py
- [[_raise()]] - code - gateway/tests/test_daily_cve_report.py
- [[_raise()_1]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Regression_guard_2026-08-30_the_report_scanned_latest_tags_while_deploys_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_asyncio]]

## Top bridge nodes
- [[TestRunningImageResolution]] - degree 5, connects to 1 community
- [[_raise()]] - degree 2, connects to 1 community
