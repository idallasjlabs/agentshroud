---
type: community
members: 41
---

# OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)

**Members:** 41 nodes

## Members
- [[dot-test_alert_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_omitting_bot_tokens_preserves_default_behavior()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_runs_each_independently_and_isolates_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_uses_per_agent_token_when_provided()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_check_scoped_to_agent_registry_and_repo()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_dedup_is_per_agent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_failed_send_is_retried()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_hermes_zero_stays_silent_via_all_agents()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_hermes_zero_still_reports_when_always_report_zero()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_openclaw_zero_stays_silent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_patched_versions_carried_into_result()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_second_check_does_not_resend()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unreadable_state_file_means_alert_again()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_unwritable_state_file_is_logged_not_raised()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_zero_report_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 fix Hermes zero-CVE heartbeats confused the owner because they're…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 each wrapped agent's alert must go out via ITS OWN bot token (so it…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the new-CVE alert path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the zero-report path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Backward compatibility no bot_tokens arg means every agent still gets the…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[OpenClaw and Hermes are processed on fully separate paths; one failing never…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Owner wants to SEE a Hermes report even with 0 new advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestPerAgentUpstreamChecks]] - code - gateway/tests/test_daily_cve_report.py
- [[TestUpstreamAlertDedup]] - code - gateway/tests/test_daily_cve_report.py
- [[The 0605 check and the 0700 GHSA ingest share one diff; an advisory still…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[__enter__()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[__exit__()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_check()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_9]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_10]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_11]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_12]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_13]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_14]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_15]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_16]] - code - gateway/tests/test_daily_cve_report.py
- [[_flaky_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[read()_1]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 6 edges to [[_COMMUNITY_format_cve_report() (2)]]
- 5 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_Regression guard (2026-08-30) the report scanned latest tags while deploys… (2)]]
- 1 edge to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips.]]

## Top bridge nodes
- [[_fake_send()_14]] - degree 19, connects to 3 communities
- [[TestPerAgentUpstreamChecks]] - degree 11, connects to 2 communities
- [[dot-test_all_agents_runs_each_independently_and_isolates_failure()]] - degree 4, connects to 2 communities
- [[TestUpstreamAlertDedup]] - degree 8, connects to 1 community
- [[dot-test_alert_send_failure_is_swallowed()]] - degree 5, connects to 1 community
