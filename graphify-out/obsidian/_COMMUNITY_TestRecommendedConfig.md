---
type: community
cohesion: 0.33
members: 6
---

# TestRecommendedConfig

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_approval_queue_enabled()_3]] - code - gateway/tests/test_config_validation.py
- [[.test_kill_switch_enabled()_3]] - code - gateway/tests/test_config_validation.py
- [[.test_pii_enabled()_3]] - code - gateway/tests/test_config_validation.py
- [[.test_ssh_requires_approval()_3]] - code - gateway/tests/test_config_validation.py
- [[.test_tailscale_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[TestRecommendedConfig_1]] - code - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRecommendedConfig
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_config_validation.py]]
- 1 edge to [[_COMMUNITY_TestRecommendedConfig]]
- 1 edge to [[_COMMUNITY__parse_env_file()]]

## Top bridge nodes
- [[TestRecommendedConfig_1]] - degree 8, connects to 3 communities