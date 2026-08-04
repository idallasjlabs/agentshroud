---
type: community
cohesion: 0.39
members: 8
---

# Module Group 435

**Cohesion:** 0.39 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_always_includes_gateway_image()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_deduplication()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_adds_extra_targets()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_env_var_empty_string_ignored()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_whitespace_stripped_from_env_var()]] - code - gateway/tests/test_daily_cve_report.py
- [[Build the list of container image targets for Trivy image scanning.      Combine]] - rationale - gateway/security/daily_cve_report.py
- [[TestBuildImageTargets]] - code - gateway/tests/test_daily_cve_report.py
- [[_build_image_targets()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_435
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 169]]
- 1 edge to [[_COMMUNITY_Module Group 176]]

## Top bridge nodes
- [[_build_image_targets()]] - degree 9, connects to 2 communities
- [[TestBuildImageTargets]] - degree 6, connects to 1 community
