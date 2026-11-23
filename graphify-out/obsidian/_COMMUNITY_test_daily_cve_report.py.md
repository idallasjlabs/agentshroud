---
type: community
members: 35
---

# test_daily_cve_report.py

**Members:** 35 nodes

## Members
- [[dot-_no_docker()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_every_configured_bot_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_deduplication()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gateway_container_name_is_env_overridable()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_checked_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_file_missing()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_ingested_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_checked_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_ingested_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning. Prefers…]] - rationale - gateway/security/daily_cve_report.py
- [[Deployments that rename the gateway container (dev runs agentshroud-marvin-…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond gateway + the real…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Keep the alerted-advisory state file out of varlog in every test.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Pin _running_image to the docker-unavailable fallback path so these tests…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY source of bot…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Resolve the image tag a container is ACTUALLY running, via docker CLI. The…]] - rationale - gateway/security/daily_cve_report.py
- [[TestAlreadyCheckedUpstreamToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadyIngestedGhsaToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for gateway.security.daily_cve_report.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py
- [[_fake_running()]] - code - gateway/tests/test_daily_cve_report.py
- [[_isolated_alert_state()]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[fixture_89]] - code
- [[test_daily_cve_report.py]] - code - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_daily_cve_report.py]]
- 6 edges to [[_COMMUNITY_asyncio]]
- 5 edges to [[_COMMUNITY__make_report]]
- 3 edges to [[_COMMUNITY_check_upstream_cves]]
- 3 edges to [[_COMMUNITY__sleep]]
- 2 edges to [[_COMMUNITY_dot-test_gives_up_and_marks_sent_after_max_retries]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_TestRunningImageResolution]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_load_config]]
- 1 edge to [[_COMMUNITY_parse_trivy_output]]

## Top bridge nodes
- [[test_daily_cve_report.py]] - degree 35, connects to 10 communities
- [[_build_image_targets()]] - degree 12, connects to 2 communities
- [[_running_image()]] - degree 3, connects to 1 community
- [[fixture_89]] - degree 3, connects to 1 community
- [[dot-test_returns_false_when_file_missing()_2]] - degree 2, connects to 1 community
