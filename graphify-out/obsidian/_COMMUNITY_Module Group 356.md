---
type: community
cohesion: 0.18
members: 11
---

# Module Group 356

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[.test_critical_image_finding_uses_red_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_error_does_not_abort_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_result_in_return_value()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_summary_appended_to_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scans_run_for_each_target()]] - code - gateway/tests/test_daily_cve_report.py
- [[A critical finding in an image scan uses the red icon.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failing image scan appends an error line but does not raise.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Message sent via Telegram includes a Container Image Scans section.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Return value includes image_scans list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportImageScans]] - code - gateway/tests/test_daily_cve_report.py
- [[run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each tar]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_356
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Module Group 169]]

## Top bridge nodes
- [[TestRunAndSendCveReportImageScans]] - degree 6, connects to 1 community