---
type: community
members: 10
---

# Regression guard (2026-08-30): the report scanned :latest tags while deploys… (2)

**Members:** 10 nodes

## Members
- [[dot-test_agent_label_falls_back_when_source_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_prefers_running_image_over_configured_tag()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_parses_docker_inspect_stdout()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_returns_none_on_inspect_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_running_image_returns_none_when_docker_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[If the per-agent source config is missing, the label falls back gracefully.]] - rationale - gateway/tests/test_daily_cve_report.py
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
- 1 edge to [[_COMMUNITY_OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]

## Top bridge nodes
- [[dot-test_agent_label_falls_back_when_source_missing()]] - degree 4, connects to 2 communities
- [[TestRunningImageResolution]] - degree 5, connects to 1 community
