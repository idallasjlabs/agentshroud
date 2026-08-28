---
type: community
cohesion: 0.07
members: 49
---

# Community 122

**Cohesion:** 0.07 - loosely connected
**Members:** 49 nodes

## Members
- [[.test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_every_configured_bot_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_deduplication()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal parsed Trivy report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning.      Combine]] - rationale - gateway/security/daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond         gateway + th]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Format a Trivy scan result into a Telegram-ready Markdown message.      Args]] - rationale - gateway/security/daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY         source of]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[daily_cve_report module]] - code - gateway/security/daily_cve_report.py
- [[format_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_122
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 100]]
- 4 edges to [[_COMMUNITY_Community 215]]
- 3 edges to [[_COMMUNITY_Community 685]]
- 2 edges to [[_COMMUNITY_Community 380]]
- 2 edges to [[_COMMUNITY_Community 631]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 640]]
- 1 edge to [[_COMMUNITY_SOC Collaborators]]
- 1 edge to [[_COMMUNITY_Community 455]]
- 1 edge to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 1270]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 30, connects to 7 communities
- [[run_and_send_cve_report()]] - degree 16, connects to 4 communities
- [[_build_image_targets()]] - degree 12, connects to 3 communities
- [[format_cve_report()]] - degree 17, connects to 2 communities