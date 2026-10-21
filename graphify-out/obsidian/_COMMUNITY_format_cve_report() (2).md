---
type: community
members: 43
---

# format_cve_report() (2)

**Members:** 43 nodes

## Members
- [[dot-_no_docker()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_critical_image_finding_uses_red_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_daily_fs_scan_skips_security_log_tree()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_image_scan_error_does_not_abort_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_image_scan_result_in_return_value()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_image_scan_summary_appended_to_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_image_scans_run_for_each_target()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[A critical finding in an image scan uses the red icon.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A failing image scan appends an error line but does not raise.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message. Args…]] - rationale - gateway/security/daily_cve_report.py
- [[Message sent via Telegram includes a Container Image Scans section.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Pin _running_image to the docker-unavailable fallback (same as…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Return value includes image_scans list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportImageScans]] - code - gateway/tests/test_daily_cve_report.py
- [[The daily fs scan of  must exclude varlogsecurity (trivy's own cache +…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_fake_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each…]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/format_cve_report_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 6 edges to [[_COMMUNITY_OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)]]
- 1 edge to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips.]]
- 1 edge to [[_COMMUNITY_Skill Project Management (PM) (3)]]

## Top bridge nodes
- [[dot-test_daily_fs_scan_skips_security_log_tree()]] - degree 6, connects to 3 communities
- [[format_cve_report()]] - degree 17, connects to 2 communities
- [[dot-test_critical_image_finding_uses_red_icon()]] - degree 7, connects to 2 communities
- [[dot-test_image_scan_error_does_not_abort_report()]] - degree 7, connects to 2 communities
- [[dot-test_image_scan_result_in_return_value()]] - degree 7, connects to 2 communities
