---
type: community
members: 10
---

# TestConfig

**Members:** 10 nodes

## Members
- [[dot-test_export_config_delegates_to_get()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_get_config_reads_yaml()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_get_config_when_file_missing()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_import_config_delegates_to_update()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_update_config_rejects_unknown_keys()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_update_config_round_trips_bots_key()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_update_config_without_existing_file_skips_backup()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_update_config_writes_yaml_and_backs_up()]] - code - gateway/tests/test_web_api_coverage.py
- [[SCRUM-107 the `bots` top-level key must be allowed through PUT apiconfig,…]] - rationale - gateway/tests/test_web_api_coverage.py
- [[TestConfig]] - code - gateway/tests/test_web_api_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestConfig
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__engine]]

## Top bridge nodes
- [[TestConfig]] - degree 9, connects to 1 community
