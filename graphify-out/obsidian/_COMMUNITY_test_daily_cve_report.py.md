---
type: community
members: 26
---

# test_daily_cve_report.py

**Members:** 26 nodes

## Members
- [[dot-_patch_urllib()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_raises_on_network_error()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_empty_when_all_known()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_new_advisory_not_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_whose_cve_is_already_tracked()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_advisory_without_ghsa_id()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_skips_ghsa_already_in_registry()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_uses_github_token_in_header()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build a minimal GitHub Security Advisory payload keyed on GHSA id. ``ghsa_id``…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Fetch one agent's GitHub Security Advisories and return advisories we don't…]] - rationale - gateway/security/daily_cve_report.py
- [[Stub urllib.request.urlopen to return a list of advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestCheckUpstreamCves]] - code - gateway/tests/test_daily_cve_report.py
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for gateway.security.daily_cve_report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_capture_req()]] - code - gateway/tests/test_daily_cve_report.py
- [[_make_github_advisory()]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves()]] - code - gateway/security/daily_cve_report.py
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_asyncio]]
- 6 edges to [[_COMMUNITY_daily_cve_report.py]]
- 4 edges to [[_COMMUNITY__make_report]]
- 3 edges to [[_COMMUNITY__sleep]]
- 3 edges to [[_COMMUNITY__build_image_targets]]
- 2 edges to [[_COMMUNITY_format_upstream_cve_alert]]
- 2 edges to [[_COMMUNITY_dot-test_gives_up_and_marks_sent_after_max_retries]]
- 2 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_TestUpstreamAlertDedup]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_list_cve_agents]]
- 1 edge to [[_COMMUNITY_parse_trivy_output]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 35, connects to 13 communities
- [[check_upstream_cves()]] - degree 13, connects to 2 communities
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - degree 2, connects to 1 community
