---
type: community
members: 55
---

# Community 1325

**Members:** 55 nodes

## Members
- [[NOTE This branch ships hot-reload of the config FILE only. The web config]] - rationale - gateway/ingest_api/config.py
- [[.model_post_init()]] - code - gateway/ingest_api/config.py
- [[A missing file (mtime -1.0) must not trigger a reload (no reject storm).]] - rationale - gateway/tests/test_config_hot_reload.py
- [[A structurally-valid YAML that violates the pydantic schema is rejected.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[AuditExportConfig]] - code - gateway/ingest_api/config.py
- [[Background mtime-poll watcher reload the config when the file changes.      Pol]] - rationale - gateway/ingest_api/config.py
- [[CI has no real agentshroud.yaml (gitignored, per-deployment secret     config) —]] - rationale - gateway/tests/conftest.py
- [[Channel ownership configuration (P3 Telegram + email oversight, P5 iMessage)]] - rationale - gateway/ingest_api/config.py
- [[ChannelsConfig]] - code - gateway/ingest_api/config.py
- [[Configuration for compliance audit export functionality.]] - rationale - gateway/ingest_api/config.py
- [[Copy only the reloadable-field subset from ``new`` onto ``current`` in place.]] - rationale - gateway/ingest_api/config.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Every GatewayConfig field is classified exactly once, disjointly.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[File mtime changes but no reloadable field differs — reload still succeeds.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[GatewayConfig_3]] - code - gateway/tests/test_config_hot_reload.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Path_1]] - code - gateway/ingest_api/config.py
- [[Path_25]] - code - gateway/tests/test_config_hot_reload.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[README_128]] - document - gateway/README.md
- [[Re-parse and validate ``config_path``; atomically swap in reloadable fields.]] - rationale - gateway/ingest_api/config.py
- [[Related Notes_70]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Resolve the config file path using the same search order as load_config().]] - rationale - gateway/ingest_api/config.py
- [[Return the file mtime, or -1.0 if the file is missing (treated as no-op).]] - rationale - gateway/ingest_api/config.py
- [[_default_mtime returns the file mtime, and -1.0 when the file is absent.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[_default_mtime()]] - code - gateway/ingest_api/config.py
- [[_ensure_agentshroud_config_resolvable()]] - code - gateway/tests/conftest.py
- [[_load()]] - code - gateway/tests/test_config_hot_reload.py
- [[_write()]] - code - gateway/tests/test_config_hot_reload.py
- [[apply_reloadable_config()]] - code - gateway/ingest_api/config.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
- [[config.py]] - code - gateway/ingest_api/config.py
- [[config_watcher()]] - code - gateway/ingest_api/config.py
- [[reload_config()]] - code - gateway/ingest_api/config.py
- [[resolve_config_path honors the explicit arg and AGENTSHROUD_CONFIG env.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[resolve_config_path()]] - code - gateway/ingest_api/config.py
- [[sanitizer.py]] - code - gateway/ingest_api/sanitizer.py
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
- [[verify.sh]] - code - gateway/verify.sh
- [[verify.sh script]] - code - gateway/verify.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1325
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 1]]
- 10 edges to [[_COMMUNITY_Community 6]]
- 9 edges to [[_COMMUNITY_Community 34]]
- 7 edges to [[_COMMUNITY_Community 9]]
- 6 edges to [[_COMMUNITY_Community 273]]
- 5 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 24]]
- 3 edges to [[_COMMUNITY_Community 38]]
- 2 edges to [[_COMMUNITY_Community 18]]
- 2 edges to [[_COMMUNITY_Community 69]]
- 2 edges to [[_COMMUNITY_Community 99]]
- 2 edges to [[_COMMUNITY_Community 659]]
- 2 edges to [[_COMMUNITY_Community 513]]
- 1 edge to [[_COMMUNITY_Community 134]]
- 1 edge to [[_COMMUNITY_Community 81]]
- 1 edge to [[_COMMUNITY_Community 45]]
- 1 edge to [[_COMMUNITY_Community 799]]
- 1 edge to [[_COMMUNITY_Community 870]]
- 1 edge to [[_COMMUNITY_Community 849]]
- 1 edge to [[_COMMUNITY_Community 548]]
- 1 edge to [[_COMMUNITY_Community 603]]
- 1 edge to [[_COMMUNITY_Community 217]]

## Top bridge nodes
- [[config.py]] - degree 43, connects to 14 communities
- [[sanitizer.py]] - degree 13, connects to 8 communities
- [[README_128]] - degree 11, connects to 6 communities
- [[AuditExportConfig]] - degree 7, connects to 4 communities
- [[ChannelsConfig]] - degree 6, connects to 4 communities