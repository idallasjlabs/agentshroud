---
type: community
cohesion: 0.03
members: 112
---

# ModeRequest

**Cohesion:** 0.03 - loosely connected
**Members:** 112 nodes

## Members
- [[NOTE This branch ships hot-reload of the config FILE only. The web config]] - rationale - gateway/ingest_api/config.py
- [[.base_url()]] - code - gateway/ingest_api/bot_config.py
- [[.model_post_init()]] - code - gateway/ingest_api/config.py
- [[.resolved_container_name()]] - code - gateway/ingest_api/bot_config.py
- [[.test_bot_config_has_telegram_token_secret_field()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_bot_config_image_field_present()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_bot_config_telegram_token_secret_set()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_config_with_tool_result_pii()]] - code - gateway/tests/test_tool_result_pii.py
- [[.test_mcp_proxy_data_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_mcp_proxy_data_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_openclaw_bot_config_backward_compat()]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[.test_proxy_allowed_domains_defaults_to_empty_when_absent()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[.test_proxy_allowed_domains_parsed_from_yaml()]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[A missing file (mtime -1.0) must not trigger a reload (no reject storm).]] - rationale - gateway/tests/test_config_hot_reload.py
- [[A structurally-valid YAML that violates the pydantic schema is rejected.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[AuditExportConfig]] - code - gateway/ingest_api/config.py
- [[Background mtime-poll watcher reload the config when the file changes.      Pol]] - rationale - gateway/ingest_api/config.py
- [[BotConfig]] - code - gateway/ingest_api/bot_config.py
- [[BotConfig.base_url computes http{hostname}{port}.]] - rationale - gateway/tests/test_config.py
- [[Channel ownership configuration (P3 Telegram + email oversight, P5 iMessage)]] - rationale - gateway/ingest_api/config.py
- [[ChannelsConfig]] - code - gateway/ingest_api/config.py
- [[Complete gateway configuration]] - rationale - gateway/ingest_api/config.py
- [[Compute the bot's internal base URL from hostname and port.]] - rationale - gateway/ingest_api/bot_config.py
- [[Configuration for compliance audit export functionality.]] - rationale - gateway/ingest_api/config.py
- [[Copy only the reloadable-field subset from ``new`` onto ``current`` in place.]] - rationale - gateway/ingest_api/config.py
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - rationale - gateway/ingest_api/bot_config.py
- [[Dependency Graph_1]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Dependency Graph]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Every GatewayConfig field is classified exactly once, disjointly.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[Explicit container_name wins over the 'agentshroud-{id}' convention —     regres]] - rationale - gateway/tests/test_config.py
- [[File mtime changes but no reloadable field differs — reload still succeeds.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[Gateway Module Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Gateway Startup Initialization Order]] - concept - docs/vault/09 - Diagrams/Dependency Graph.md
- [[GatewayConfig_3]] - code - gateway/tests/test_config_hot_reload.py
- [[GatewayConfig_1]] - code - gateway/ingest_api/config.py
- [[Key Initialization Order (main.py lifespan)]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Load and validate configuration from agentshroud.yaml      Search order     1.]] - rationale - gateway/ingest_api/config.py
- [[Load the real agentshroud.yaml when present (deployment host), else the     comm]] - rationale - gateway/tests/test_config.py
- [[Map agentshroud.yaml entity names to Presidiointernal entity names]] - rationale - gateway/ingest_api/config.py
- [[No explicit container_name — derives 'agentshroud-{id}' (openclaw's case).]] - rationale - gateway/tests/test_config.py
- [[OpenClaw BotConfig must still work without the new fields.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[Path_1]] - code - gateway/ingest_api/config.py
- [[Path_25]] - code - gateway/tests/test_config_hot_reload.py
- [[Python Package Dependencies]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[README_128]] - document - gateway/README.md
- [[Re-parse and validate ``config_path``; atomically swap in reloadable fields.]] - rationale - gateway/ingest_api/config.py
- [[Related Notes_70]] - document - docs/vault/09 - Diagrams/Dependency Graph.md
- [[Resolve the config file path using the same search order as load_config().]] - rationale - gateway/ingest_api/config.py
- [[Return the file mtime, or -1.0 if the file is missing (treated as no-op).]] - rationale - gateway/ingest_api/config.py
- [[RouterConfig must accept the Hermes Docker service hostname.]] - rationale - gateway/tests/test_config.py
- [[RouterConfig should accept single-label Docker service hostnames.]] - rationale - gateway/tests/test_config.py
- [[Test PII entity type mapping]] - rationale - gateway/tests/test_config.py
- [[Test loading configuration from agentshroud.yaml (or the committed example).]] - rationale - gateway/tests/test_config.py
- [[Test that configuration has sensible defaults]] - rationale - gateway/tests/test_config.py
- [[Test that configuration includes tool result PII settings]] - rationale - gateway/tests/test_tool_result_pii.py
- [[Test that load_config() populates bots — from YAML or backward-compat default.]] - rationale - gateway/tests/test_config.py
- [[TestMCPProxyConfigLoading]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[TestTelegramBotConfigTokenSecretField]] - code - gateway/tests/test_telegram_proxy_multibot.py
- [[The real docker container name for this bot — see container_name field.]] - rationale - gateway/ingest_api/bot_config.py
- [[Verify BotConfig.telegram_token_secret field is present and defaults correctly.]] - rationale - gateway/tests/test_telegram_proxy_multibot.py
- [[When agentshroud.yaml declares hermes, load_config() populates it in bots.]] - rationale - gateway/tests/test_config.py
- [[_bot_service_names() must use each bot's real container name, not a     hardcode]] - rationale - gateway/tests/test_config.py
- [[_default_mtime returns the file mtime, and -1.0 when the file is absent.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[_default_mtime()]] - code - gateway/ingest_api/config.py
- [[_entity_type_mapping()]] - code - gateway/ingest_api/config.py
- [[_load()]] - code - gateway/tests/test_config_hot_reload.py
- [[_load_config()]] - code - gateway/tests/test_config.py
- [[_write()]] - code - gateway/tests/test_config_hot_reload.py
- [[apply_reloadable_config()]] - code - gateway/ingest_api/config.py
- [[auth_headers()_2]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[bot_config.py]] - code - gateway/ingest_api/bot_config.py
- [[config.py]] - code - gateway/ingest_api/config.py
- [[config_watcher()]] - code - gateway/ingest_api/config.py
- [[load_config computes CORS origins from the configured port.]] - rationale - gateway/tests/test_router.py
- [[load_config()]] - code - gateway/ingest_api/config.py
- [[mcp_proxy_data is an empty dict when section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[mcp_proxy_data is populated from the mcp_proxy YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is empty list when proxy section is absent from YAML.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[proxy_allowed_domains is populated from the proxy.allowed_domains YAML section.]] - rationale - gateway/tests/test_mcp_result_endpoint.py
- [[reload_config()]] - code - gateway/ingest_api/config.py
- [[resolve_config_path honors the explicit arg and AGENTSHROUD_CONFIG env.]] - rationale - gateway/tests/test_config_hot_reload.py
- [[resolve_config_path()]] - code - gateway/ingest_api/config.py
- [[sanitizer.py]] - code - gateway/ingest_api/sanitizer.py
- [[test_apply_swaps_only_reloadable_fields()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_bot_config_base_url()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_defaults_to_agentshroud_id()]] - code - gateway/tests/test_config.py
- [[test_bot_config_resolved_container_name_uses_explicit_override()]] - code - gateway/tests/test_config.py
- [[test_bot_service_names_uses_resolved_container_name()]] - code - gateway/tests/test_config.py
- [[test_config.py]] - code - gateway/tests/test_config.py
- [[test_config_defaults()]] - code - gateway/tests/test_config.py
- [[test_config_hot_reload.py]] - code - gateway/tests/test_config_hot_reload.py
- [[test_cors_origins_include_configured_port()]] - code - gateway/tests/test_router.py
- [[test_default_mtime_reads_real_file_and_handles_missing()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_entity_type_mapping()]] - code - gateway/tests/test_config.py
- [[test_field_partition_is_disjoint_and_covers_model()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_load_config()]] - code - gateway/tests/test_config.py
- [[test_load_config_has_bots()]] - code - gateway/tests/test_config.py
- [[test_load_config_registers_hermes()]] - code - gateway/tests/test_config.py
- [[test_mcp_result_endpoint.py]] - code - gateway/tests/test_mcp_result_endpoint.py
- [[test_reload_applies_valid_change()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_missing_file_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_no_reloadable_field_changed()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_rejects_invalid_and_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_reload_rejects_schema_violation_and_keeps_last_good()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_resolve_config_path_explicit_and_env()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_router_config_accepts_docker_service_hostname()]] - code - gateway/tests/test_config.py
- [[test_router_config_accepts_hermes_hostname()]] - code - gateway/tests/test_config.py
- [[test_watcher_ignores_missing_file()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_watcher_reloads_on_mtime_change()]] - code - gateway/tests/test_config_hot_reload.py
- [[test_watcher_stops_on_event()]] - code - gateway/tests/test_config_hot_reload.py
- [[verify.sh]] - code - gateway/verify.sh
- [[verify.sh script]] - code - gateway/verify.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ModeRequest
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_EgressPolicy]]
- 21 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 13 edges to [[_COMMUNITY_ResourceGuard]]
- 13 edges to [[_COMMUNITY_ApprovalRequest]]
- 11 edges to [[_COMMUNITY_version_routes.py]]
- 10 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 10 edges to [[_COMMUNITY_api.py]]
- 9 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 8 edges to [[_COMMUNITY_TrustManager]]
- 8 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_A2APolicyEngine]]
- 6 edges to [[_COMMUNITY_gateway service (prod, sole egress point, 75-mod]]
- 5 edges to [[_COMMUNITY_SSHProxy]]
- 4 edges to [[_COMMUNITY_main.rs]]
- 2 edges to [[_COMMUNITY_TestAuth]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_STPA-Sec Analysis of AgentShroud]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_Hermes Cron Jobs Reference & Recreation Guide]]
- 2 edges to [[_COMMUNITY_Safe Refactor Specialist]]
- 1 edge to [[_COMMUNITY_test_a2a_proxy.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Policy - Final Decision]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_test_jira_weekly_review.py]]
- 1 edge to [[_COMMUNITY__make_stream_app_state()]]
- 1 edge to [[_COMMUNITY_TestBenchmarkRegression]]
- 1 edge to [[_COMMUNITY_Test-Driven Development README]]
- 1 edge to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 1 edge to [[_COMMUNITY_Examples]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_Function Details]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_AgentShroud v1.0.0 Fortress Release Announcement]]
- 1 edge to [[_COMMUNITY_.get_or_create_session()]]
- 1 edge to [[_COMMUNITY_egress_monitor.py]]

## Top bridge nodes
- [[config.py]] - degree 43, connects to 16 communities
- [[load_config()]] - degree 51, connects to 15 communities
- [[GatewayConfig_1]] - degree 65, connects to 11 communities
- [[test_mcp_result_endpoint.py]] - degree 16, connects to 9 communities
- [[BotConfig]] - degree 34, connects to 8 communities