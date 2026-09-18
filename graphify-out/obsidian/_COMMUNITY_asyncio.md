---
type: community
cohesion: 0.05
members: 82
---

# asyncio

**Cohesion:** 0.05 - loosely connected
**Members:** 82 nodes

## Members
- [[._no_docker()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_affected_packages_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_agent_label_falls_back_when_source_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_omitting_bot_tokens_preserves_default_behavior()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_runs_each_independently_and_isolates_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_uses_per_agent_token_when_provided()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_check_scoped_to_agent_registry_and_repo()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_cve_ids()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_package_names()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_contains_severity_counts()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_critical_image_finding_uses_red_icon()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_daily_fs_scan_skips_security_log_tree()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_error_report_shows_error_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_fixed_version_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_hermes_zero_stays_silent_via_all_agents()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_hermes_zero_still_reports_when_always_report_zero()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_error_does_not_abort_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_result_in_return_value()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scan_summary_appended_to_message()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_image_scans_run_for_each_target()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_openclaw_zero_stays_silent()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_clean_when_no_critical_high()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_status_critical_when_critical_present()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_total_vulnerability_count_shown()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_count_severity_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_report_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 fix Hermes zero-CVE heartbeats confused the owner because they're…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 each wrapped agent's alert must go out via ITS OWN bot token (so it…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Backward compatibility no bot_tokens arg means every agent still gets the…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[OpenClaw and Hermes are processed on fully separate paths; one failing never…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Pin _running_image to the docker-unavailable fallback (same as…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Run a Trivy scan, format the report, and send via Telegram. Args bot_token…]] - rationale - gateway/security/daily_cve_report.py
- [[TestFormatCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestPerAgentUpstreamChecks]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportImageScans]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for gateway.security.daily_cve_report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_boom_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_check()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_6]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_9]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_10]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_11]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_12]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_13]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_14]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_15]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_16]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_trivy_scan()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[asyncio_4]] - code
- [[format_cve_report]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report]] - code - gateway/security/daily_cve_report.py
- [[run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 11 edges to [[_COMMUNITY__sleep()]]
- 7 edges to [[_COMMUNITY_.test_gives_up_and_marks_sent_after_max_retries(]]
- 5 edges to [[_COMMUNITY_TestPerAgentUpstreamChecks]]
- 4 edges to [[_COMMUNITY__build_image_targets]]
- 4 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 4 edges to [[_COMMUNITY_TestRunAndSendCveReportImageScans]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY_.test_short_text_passes_through_unchanged()]]
- 2 edges to [[_COMMUNITY_TestRunningImageResolution]]
- 2 edges to [[_COMMUNITY_format_cve_report()]]
- 2 edges to [[_COMMUNITY_gateway.security.agent_cve_registry]]
- 1 edge to [[_COMMUNITY_TestAlreadyCheckedUpstreamToday]]
- 1 edge to [[_COMMUNITY_TestAlreadyIngestedGhsaToday]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY__t()]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestTrivySkipDirs]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 34, connects to 12 communities
- [[run_and_send_cve_report]] - degree 17, connects to 6 communities
- [[asyncio_4]] - degree 37, connects to 3 communities
- [[format_cve_report]] - degree 17, connects to 3 communities
- [[.test_daily_fs_scan_skips_security_log_tree()]] - degree 6, connects to 2 communities