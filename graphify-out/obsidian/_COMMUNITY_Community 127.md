---
type: community
members: 44
---

# Community 127

**Members:** 44 nodes

## Members
- [[._patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_daily_fs_scan_skips_security_log_tree()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_skip_dirs_flag_when_omitted()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_short_text_passes_through_unchanged()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skip_dirs_added_to_command()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_truncates_over_length_text()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id.      ``ghsa_i]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't trac]] - rationale - gateway/security/daily_cve_report.py
- [[Keep the alerted-advisory state file out of varlog in every test.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[TestGhsaIngestSchedulerRetry]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[TestSendTelegramTruncation]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivySkipDirs]] - code - gateway/tests/test_daily_cve_report.py
- [[The daily fs scan of  must exclude varlogsecurity (trivy's own         cache]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_isolated_alert_state()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_127
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 736]]
- 6 edges to [[_COMMUNITY_Community 762]]
- 2 edges to [[_COMMUNITY_Community 74]]
- 2 edges to [[_COMMUNITY_Community 1200]]
- 2 edges to [[_COMMUNITY_Community 1202]]
- 1 edge to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 131]]
- 1 edge to [[_COMMUNITY_Community 1001]]
- 1 edge to [[_COMMUNITY_Community 1554]]
- 1 edge to [[_COMMUNITY_Community 2048]]
- 1 edge to [[_COMMUNITY_Community 2003]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 34, connects to 11 communities
- [[check_upstream_cves()]] - degree 13, connects to 2 communities
- [[.test_returns_false_when_file_missing()]] - degree 2, connects to 1 community
- [[.test_undelivered_new_advisory_retries_not_marked_ingested()]] - degree 2, connects to 1 community