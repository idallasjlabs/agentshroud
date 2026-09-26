---
type: community
cohesion: 0.20
members: 10
---

# TestCredentialInjection

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_export_config_delegates_to_get()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_get_config_reads_yaml()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_get_config_when_file_missing()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_import_config_delegates_to_update()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_rejects_unknown_keys()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_round_trips_bots_key()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_without_existing_file_skips_backup()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_writes_yaml_and_backs_up()]] - code - gateway/tests/test_web_api_coverage.py
- [[SCRUM-107 the `bots` top-level key must be allowed through PUT         apicon]] - rationale - gateway/tests/test_web_api_coverage.py
- [[TestConfig_1]] - code - gateway/tests/test_web_api_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestCredentialInjection
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_system-requirements]]

## Top bridge nodes
- [[TestConfig_1]] - degree 12, connects to 2 communities