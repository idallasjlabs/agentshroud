---
type: community
members: 37
---

# test_config_hot_reload.py

**Members:** 37 nodes

## Members
- [[A missing file (mtime -1.0) must not trigger a reload (no reject storm).]] - rationale - gateway/tests/test_config_hot_reload.py
- [[A structurally-valid YAML that violates the pydantic schema is rejected.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[Background mtime-poll watcher reload the config when the file changes. Polls…]] - rationale - gateway/ingest_api/config.py
- [[Copy only the reloadable-field subset from ``new`` onto ``current`` in place.…]] - rationale - gateway/ingest_api/config.py
- [[Every GatewayConfig field is classified exactly once, disjointly.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[File mtime changes but no reloadable field differs — reload still succeeds.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[Path_15]] - code
- [[Path_16]] - code
- [[Re-parse and validate ``config_path``; atomically swap in reloadable fields.…]] - rationale - gateway/ingest_api/config.py
- [[Return the file mtime, or -1.0 if the file is missing (treated as no-op).]] - rationale - gateway/ingest_api/config.py
- [[Tests for SCRUM-89 config hot-reload (config.py). Covers the validated, fail-…]] - rationale - gateway/tests/test_config_hot_reload.py
- [[_default_mtime returns the file mtime, and -1.0 when the file is absent.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[_default_mtime()]] - code - gateway/ingest_api/config.py
- [[_drive()]] - code - gateway/tests/test_config_hot_reload.py
- [[_drive()_1]] - code - gateway/tests/test_config_hot_reload.py
- [[_drive()_2]] - code - gateway/tests/test_config_hot_reload.py
- [[_fake_mtime()]] - code - gateway/tests/test_config_hot_reload.py
- [[_load()_1]] - code - gateway/tests/test_config_hot_reload.py
- [[_on_reload()]] - code - gateway/tests/test_config_hot_reload.py
- [[_write()]] - code - gateway/tests/test_config_hot_reload.py
- [[apply_reloadable_config()]] - code - gateway/ingest_api/config.py
- [[config_watcher()]] - code - gateway/ingest_api/config.py
- [[reload_config()]] - code - gateway/ingest_api/config.py
- [[resolve_config_path honors the explicit arg and AGENTSHROUD_CONFIG env.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[test_apply_swaps_only_reloadable_fields()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_config_hot_reload.py]] - code - gateway/tests/test_config_hot_reload.py
- [[test_default_mtime_reads_real_file_and_handles_missing()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_field_partition_is_disjoint_and_covers_model()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_applies_valid_change()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_missing_file_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_no_reloadable_field_changed()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_rejects_invalid_and_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_rejects_schema_violation_and_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_resolve_config_path_explicit_and_env()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_watcher_ignores_missing_file()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_watcher_reloads_on_mtime_change()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_watcher_stops_on_event()]] - code - gateway/tests/test_config_hot_reload.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_config_hot_reloadpy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[config_watcher()]] - degree 14, connects to 3 communities
- [[test_config_hot_reload.py]] - degree 23, connects to 1 community
- [[reload_config()]] - degree 13, connects to 1 community
- [[_load()_1]] - degree 13, connects to 1 community
- [[apply_reloadable_config()]] - degree 6, connects to 1 community
