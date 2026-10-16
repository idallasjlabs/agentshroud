---
type: community
cohesion: 0.05
members: 66
---

# load_config

**Cohesion:** 0.05 - loosely connected
**Members:** 66 nodes

## Members
- [[NOTE This branch ships hot-reload of the config FILE only. The web config]] - rationale - gateway/ingest_api/config.py
- [[dot-model_post_init()_1]] - code - gateway/ingest_api/config.py
- [[dot-test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_mcp_proxy_data_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_mcp_proxy_data_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[dot-test_proxy_allowed_domains_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[A missing file (mtime -1.0) must not trigger a reload (no reject storm).]] - rationale - gateway/tests/test_config_hot_reload.py
- [[A structurally-valid YAML that violates the pydantic schema is rejected.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[AuditExportConfig]] - code - gateway/ingest_api/config.py
- [[Background mtime-poll watcher reload the config when the file changes.      Pol]] - rationale - gateway/ingest_api/config.py
- [[CI has no real agentshroud.yaml (gitignored, per-deployment secret     config) —]] - rationale - gateway/tests/conftest.py
- [[Channel ownership configuration (P3 Telegram + email oversight, P5 iMessage)]] - rationale - gateway/ingest_api/config.py
- [[ChannelsConfig]] - code - gateway/ingest_api/config.py
- [[Configuration for compliance audit export functionality.]] - rationale - gateway/ingest_api/config.py
- [[Copy only the reloadable-field subset from ``new`` onto ``current`` in place.]] - rationale - gateway/ingest_api/config.py
- [[Every GatewayConfig field is classified exactly once, disjointly.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[File mtime changes but no reloadable field differs — reload still succeeds.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[GatewayConfig]] - code - gateway/tests/test_config_hot_reload.py
- [[Load and validate configuration from agentshroud.yaml      Search order     1.]] - rationale - gateway/ingest_api/config.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[Map agentshroud.yaml entity names to Presidiointernal entity names]] - rationale - gateway/ingest_api/config.py
- [[Path_31]] - code - gateway/ingest_api/config.py
- [[Path_32]] - code - gateway/tests/test_config_hot_reload.py
- [[Re-parse and validate ``config_path``; atomically swap in reloadable fields.]] - rationale - gateway/ingest_api/config.py
- [[Resolve the Dockerfile for the default bot from gateway config.]] - rationale - gateway/web/api.py
- [[Resolve the config file path using the same search order as load_config().]] - rationale - gateway/ingest_api/config.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
- [[Return the file mtime, or -1.0 if the file is missing (treated as no-op).]] - rationale - gateway/ingest_api/config.py
- [[_default_mtime returns the file mtime, and -1.0 when the file is absent.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[_default_mtime()]] - code - gateway/ingest_api/config.py
- [[_ensure_agentshroud_config_resolvable()]] - code - gateway/tests/conftest.py
- [[_entity_type_mapping()]] - code - gateway/ingest_api/config.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_load()]] - code - gateway/tests/test_config_hot_reload.py
- [[_write()]] - code - gateway/tests/test_config_hot_reload.py
- [[apply_reloadable_config()]] - code - gateway/ingest_api/config.py
- [[check_monitor_mode_warnings()]] - code - gateway/ingest_api/config.py
- [[config_watcher()]] - code - gateway/ingest_api/config.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py
- [[ingest_apiconfig.py]] - code - gateway/ingest_api/config.py
- [[load_config()]] - code - gateway/ingest_api/config.py
- [[mcp_proxy_data is an empty dict when section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[mcp_proxy_data is populated from the mcp_proxy YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is empty list when proxy section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is populated from the proxy.allowed_domains YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[reload_config()]] - code - gateway/ingest_api/config.py
- [[resolve_config_path honors the explicit arg and AGENTSHROUD_CONFIG env.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[resolve_config_path()]] - code - gateway/ingest_api/config.py
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
TABLE source_file, type FROM #community/load_config
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_DataLedger]]
- 11 edges to [[_COMMUNITY_lifespan.py]]
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 9 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 6 edges to [[_COMMUNITY_BotConfig]]
- 6 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_test_config.py]]
- 4 edges to [[_COMMUNITY__get_engine]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_SSHHostConfig]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_group_config.py]]
- 1 edge to [[_COMMUNITY_Collaborator Setup Checklist]]
- 1 edge to [[_COMMUNITY_TestObservatoryMode]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]
- 1 edge to [[_COMMUNITY__build_image_targets]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[ingest_apiconfig.py]] - degree 43, connects to 17 communities
- [[load_config()]] - degree 51, connects to 16 communities
- [[get_module_mode()]] - degree 14, connects to 5 communities
- [[AuditExportConfig]] - degree 7, connects to 3 communities
- [[ChannelsConfig]] - degree 6, connects to 3 communities
