---
source_file: "gateway/ingest_api/bot_config.py"
type: "code"
community: "scripts/sync-cve-registry.py"
location: "L19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/scripts/sync-cve-registrypy
---

# BotConfig

## Connections
- [[.base_url()]] - `method` [EXTRACTED]
- [[.resolved_container_name()]] - `method` [EXTRACTED]
- [[.test_bot_config_has_telegram_token_secret_field()]] - `calls` [EXTRACTED]
- [[.test_bot_config_image_field_present()]] - `calls` [EXTRACTED]
- [[.test_bot_config_telegram_token_secret_set()]] - `calls` [EXTRACTED]
- [[.test_openclaw_bot_config_backward_compat()]] - `calls` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `uses` [INFERRED]
- [[AuditExportConfig]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[ChannelsConfig]] - `uses` [INFERRED]
- [[Declaration for a single bot encapsulated by AgentShroud.      Required bot HTTP]] - `rationale_for` [EXTRACTED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `shares_data_with` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[Path_1]] - `uses` [INFERRED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[SecurityConfig_2]] - `uses` [INFERRED]
- [[SecurityModuleConfig]] - `uses` [INFERRED]
- [[TestMultiBotContextvarRouting]] - `uses` [INFERRED]
- [[TestTelegramBotConfigTokenSecretField]] - `uses` [INFERRED]
- [[TestTelegramProxyRouteMultiBot]] - `uses` [INFERRED]
- [[TestTelegramTokenRegistry]] - `uses` [INFERRED]
- [[TestTelegramTokenRegistryRebuildOnMiss]] - `uses` [INFERRED]
- [[ToolRiskConfig_1]] - `uses` [INFERRED]
- [[ToolRiskPolicy_1]] - `uses` [INFERRED]
- [[bot_config.py]] - `contains` [EXTRACTED]
- [[config.py]] - `imports` [EXTRACTED]
- [[load_config()]] - `calls` [EXTRACTED]
- [[test_bot_config_base_url()]] - `calls` [EXTRACTED]
- [[test_bot_config_resolved_container_name_defaults_to_agentshroud_id()]] - `calls` [EXTRACTED]
- [[test_bot_config_resolved_container_name_uses_explicit_override()]] - `calls` [EXTRACTED]
- [[test_config.py]] - `imports` [EXTRACTED]
- [[test_telegram_proxy_multibot.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/scripts/sync-cve-registrypy