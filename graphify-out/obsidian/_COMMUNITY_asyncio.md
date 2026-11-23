---
type: community
members: 61
---

# asyncio

**Members:** 61 nodes

## Members
- [[dot-test_agent_label_falls_back_when_source_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_omitting_bot_tokens_preserves_default_behavior()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_runs_each_independently_and_isolates_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_uses_per_agent_token_when_provided()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_check_scoped_to_agent_registry_and_repo()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_dedup_is_per_agent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_is_retried()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_hermes_zero_stays_silent_via_all_agents()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_hermes_zero_still_reports_when_always_report_zero()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_openclaw_zero_stays_silent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_patched_versions_carried_into_result()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_summary_without_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_second_check_does_not_resend()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_sends_telegram_on_success()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_trivy_error_still_sends_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unreadable_state_file_means_alert_again()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unwritable_state_file_is_logged_not_raised()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_report_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 fix Hermes zero-CVE heartbeats confused the owner because they're…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 each wrapped agent's alert must go out via ITS OWN bot token (so it…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the new-CVE alert path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the zero-report path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Backward compatibility no bot_tokens arg means every agent still gets the…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If the per-agent source config is missing, the label falls back gracefully.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[OpenClaw and Hermes are processed on fully separate paths; one failing never…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Owner wants to SEE a Hermes report even with 0 new advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestPerAgentUpstreamChecks]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReport]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamAlertDedup]] - code - gateway/tests/test_daily_cve_report.py
- [[The 0605 check and the 0700 GHSA ingest share one diff; an advisory still…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[__enter__()]] - code - gateway/tests/test_daily_cve_report.py
- [[__exit__()]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_check()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_3]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_4]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_5]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_6]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_7]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_8]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_9]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_10]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_11]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_12]] - code - gateway/tests/test_daily_cve_report.py
- [[_flaky_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_error_report()]] - code - gateway/tests/test_daily_cve_report.py
- [[asyncio_20]] - code
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[read()_2]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY__make_report]]
- 8 edges to [[_COMMUNITY__sleep]]
- 6 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 4 edges to [[_COMMUNITY_dot-test_gives_up_and_marks_sent_after_max_retries]]
- 4 edges to [[_COMMUNITY_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]

## Top bridge nodes
- [[asyncio_20]] - degree 40, connects to 4 communities
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - degree 6, connects to 2 communities
- [[dot-test_sends_telegram_on_success()]] - degree 5, connects to 2 communities
- [[dot-test_returns_summary_without_token()]] - degree 4, connects to 2 communities
- [[_make_error_report()]] - degree 3, connects to 2 communities
