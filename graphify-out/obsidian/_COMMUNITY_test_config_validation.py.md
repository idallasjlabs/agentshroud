---
type: community
cohesion: 0.29
members: 7
---

# test_config_validation.py

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_file_exists()]] - code - gateway/tests/test_config_validation.py
- [[.test_file_exists()_1]] - code - gateway/tests/test_config_validation.py
- [[TestAllExampleConfigsExist]] - code - gateway/tests/test_config_validation.py
- [[TestAllExampleConfigsExist_1]] - code - gateway/tests/test_config_validation.py
- [[Verify all referenced example configs exist.]] - rationale - gateway/tests/test_config_validation.py
- [[parametrize_1]] - code
- [[test_config_validation.py_1]] - code - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_config_validationpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_cron_jobs_prompts.py]]
- 1 edge to [[_COMMUNITY__parse_env_file()]]
- 1 edge to [[_COMMUNITY_TestConfigValidation]]
- 1 edge to [[_COMMUNITY_TestMinimalConfig]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_TestRecommendedConfig]]

## Top bridge nodes
- [[test_config_validation.py_1]] - degree 10, connects to 9 communities
- [[TestAllExampleConfigsExist]] - degree 3, connects to 1 community