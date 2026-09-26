---
type: community
cohesion: 0.17
members: 16
---

# Examples

**Cohesion:** 0.17 - loosely connected
**Members:** 16 nodes

## Members
- [[._no_docker()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_every_configured_bot_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_deduplication()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_gateway_container_name_is_env_overridable()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning.      Prefers]] - rationale - gateway/security/daily_cve_report.py
- [[Deployments that rename the gateway container (dev runs         agentshroud-marv]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond         gateway + th]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Path_19]] - code - gateway/security/trivy_report.py
- [[Pin _running_image to the docker-unavailable fallback path so these         test]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY         source of]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Examples
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 1 edge to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[_build_image_targets()]] - degree 13, connects to 2 communities
- [[TestBuildImageTargets]] - degree 9, connects to 1 community
- [[Path_19]] - degree 2, connects to 1 community