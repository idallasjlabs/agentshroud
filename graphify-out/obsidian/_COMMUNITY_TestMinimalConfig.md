---
type: community
cohesion: 0.17
members: 12
---

# TestMinimalConfig

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.config()_6]] - code - gateway/tests/test_config_validation.py
- [[.test_has_auth_token()]] - code - gateway/tests/test_config_validation.py
- [[.test_has_auth_token()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_gateway_bind()]] - code - gateway/tests/test_config_validation.py
- [[.test_has_gateway_bind()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_gateway_port()]] - code - gateway/tests/test_config_validation.py
- [[.test_has_gateway_port()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_log_level()]] - code - gateway/tests/test_config_validation.py
- [[.test_has_log_level()_1]] - code - gateway/tests/test_config_validation.py
- [[TestMinimalConfig]] - code - gateway/tests/test_config_validation.py
- [[TestMinimalConfig_1]] - code - gateway/tests/test_config_validation.py
- [[minimal.env should have reasonable defaults.]] - rationale - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMinimalConfig
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__parse_env_file()]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_config_validation.py]]

## Top bridge nodes
- [[TestMinimalConfig]] - degree 7, connects to 2 communities
- [[TestMinimalConfig_1]] - degree 7, connects to 1 community
- [[.config()_6]] - degree 2, connects to 1 community