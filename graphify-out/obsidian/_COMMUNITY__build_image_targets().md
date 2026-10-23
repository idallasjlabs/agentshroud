---
type: community
cohesion: 0.13
members: 19
---

# _build_image_targets()

**Cohesion:** 0.13 - loosely connected
**Members:** 19 nodes

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
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py
- [[_fake_running()]] - code - gateway/tests/test_daily_cve_report.py
- [[_isolated_alert_state()]] - code - gateway/tests/test_daily_cve_report.py
- [[fixture_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_build_image_targets
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_format_cve_report() (2)]]

## Top bridge nodes
- [[_build_image_targets()]] - degree 11, connects to 1 community
- [[TestBuildImageTargets]] - degree 9, connects to 1 community
- [[_isolated_alert_state()]] - degree 3, connects to 1 community
- [[fixture_1]] - degree 3, connects to 1 community
