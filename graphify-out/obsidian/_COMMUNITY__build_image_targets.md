---
type: community
members: 21
---

# _build_image_targets

**Members:** 21 nodes

## Members
- [[dot-_no_docker()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_every_configured_bot_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_deduplication()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_gateway_container_name_is_env_overridable()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning. Prefers…]] - rationale - gateway/security/daily_cve_report.py
- [[Deployments that rename the gateway container (dev runs agentshroud-marvin-…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond gateway + the real…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Keep the alerted-advisory state file out of varlog in every test.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Pin _running_image to the docker-unavailable fallback path so these tests…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY source of bot…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Resolve the image tag a container is ACTUALLY running, via docker CLI. The…]] - rationale - gateway/security/daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py
- [[_fake_running()]] - code - gateway/tests/test_daily_cve_report.py
- [[_isolated_alert_state()]] - code - gateway/tests/test_daily_cve_report.py
- [[_running_image()]] - code - gateway/security/daily_cve_report.py
- [[fixture_96]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_build_image_targets
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_asyncio_1]]
- 2 edges to [[_COMMUNITY_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]

## Top bridge nodes
- [[_build_image_targets()]] - degree 12, connects to 4 communities
- [[TestBuildImageTargets]] - degree 9, connects to 1 community
- [[_running_image()]] - degree 3, connects to 1 community
- [[_isolated_alert_state()]] - degree 3, connects to 1 community
- [[fixture_96]] - degree 3, connects to 1 community
