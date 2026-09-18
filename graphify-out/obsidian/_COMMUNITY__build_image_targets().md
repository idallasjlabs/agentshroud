---
type: community
cohesion: 0.18
members: 15
---

# _build_image_targets()

**Cohesion:** 0.18 - loosely connected
**Members:** 15 nodes

## Members
- [[._no_docker()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_every_configured_bot_image()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_always_includes_gateway_image()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_deduplication()_2]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_adds_extra_targets()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_empty_string_ignored()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_gateway_container_name_is_env_overridable()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_whitespace_stripped_from_env_var()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[Deployments that rename the gateway container (dev runs         agentshroud-marv]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond         gateway + th]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Path_14]] - code
- [[Pin _running_image to the docker-unavailable fallback path so these         test]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Regression guard AGENTSHROUD_TRIVY_IMAGES used to be the ONLY         source of]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestBuildImageTargets_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_build_image_targets
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY__build_image_targets]]

## Top bridge nodes
- [[_build_image_targets()]] - degree 12, connects to 2 communities
- [[Path_14]] - degree 3, connects to 2 communities
- [[TestBuildImageTargets_1]] - degree 9, connects to 1 community