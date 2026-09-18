---
type: community
cohesion: 0.15
members: 13
---

# TestRunAndSendCveReportImageScans

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[._no_docker()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_critical_image_finding_uses_red_icon()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_error_does_not_abort_report()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_result_in_return_value()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_summary_appended_to_message()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scans_run_for_each_target()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[A critical finding in an image scan uses the red icon.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failing image scan appends an error line but does not raise.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Message sent via Telegram includes a Container Image Scans section.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Pin _running_image to the docker-unavailable fallback (same as         TestBuild]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Return value includes image_scans list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportImageScans_1]] - code - gateway/tests/test_daily_cve_report.py
- [[run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each tar]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRunAndSendCveReportImageScans
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestRunAndSendCveReportImageScans_1]] - degree 7, connects to 1 community
- [[Message sent via Telegram includes a Container Image Scans section.]] - degree 2, connects to 1 community
- [[Return value includes image_scans list.]] - degree 2, connects to 1 community
- [[A failing image scan appends an error line but does not raise.]] - degree 2, connects to 1 community
- [[A critical finding in an image scan uses the red icon.]] - degree 2, connects to 1 community