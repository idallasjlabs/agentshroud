---
type: community
cohesion: 0.06
members: 55
---

# Module Group 70

**Cohesion:** 0.06 - loosely connected
**Members:** 55 nodes

## Members
- [[.test_check_openclaw_updates_alias()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_create_purges_expired_tokens()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_create_returns_registered_prefixed_token()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_default_bot_dockerfile_used()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_echoes_status_until_disconnect()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_export_config_delegates_to_get()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_fallback_when_config_load_fails()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_fallback_when_default_bot_has_no_dockerfile()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_fallback_when_no_bots()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_first_bot_used_when_no_default_flag()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_get_config_reads_yaml()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_get_config_when_file_missing()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_get_engine_uses_runtime_config()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_import_config_delegates_to_update()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_invalid_token_closes_4003()_1]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_invalid_token_raises_401()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_master_token_rejected_4003()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_missing_token_closes_4001()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_missing_token_closes_4001()_1]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_rollback_openclaw_alias()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_status_runtime_failure_degrades_gracefully()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_status_with_running_and_stopped_containers()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_streams_logs_then_cleans_up_on_disconnect()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_rejects_unknown_keys()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_without_existing_file_skips_backup()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_update_config_writes_yaml_and_backs_up()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_upgrade_openclaw_alias()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_valid_token_authenticates()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_validate_is_single_use()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_validate_rejects_empty_and_unprefixed()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_validate_rejects_expired_token()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_validate_rejects_unknown_token()]] - code - gateway/tests/test_web_api_coverage.py
- [[HTTPAuthorizationCredentials]] - code - gateway/web/api.py
- [[KillSwitchAction]] - code - gateway/web/api.py
- [[Require valid Bearer token for all management endpoints.]] - rationale - gateway/web/api.py
- [[Restore AGENTSHROUD_MODE, revert task, and WS token registry per test.]] - rationale - gateway/tests/test_web_api_coverage.py
- [[SimpleNamespace_1]] - code - gateway/tests/test_web_api_coverage.py
- [[TestConfig_1]] - code - gateway/tests/test_web_api_coverage.py
- [[TestDefaultBotDockerfile]] - code - gateway/tests/test_web_api_coverage.py
- [[TestGetEngineHelper]] - code - gateway/tests/test_web_api_coverage.py
- [[TestMgmtWsTokens]] - code - gateway/tests/test_web_api_coverage.py
- [[TestOpenclawAliases]] - code - gateway/tests/test_web_api_coverage.py
- [[TestRebuild]] - code - gateway/tests/test_web_api_coverage.py
- [[TestRequireAuth]] - code - gateway/tests/test_web_api_coverage.py
- [[TestSecurityReport]] - code - gateway/tests/test_web_api_coverage.py
- [[TestStatus_1]] - code - gateway/tests/test_web_api_coverage.py
- [[TestWsLogs]] - code - gateway/tests/test_web_api_coverage.py
- [[TestWsUpdates]] - code - gateway/tests/test_web_api_coverage.py
- [[UpdateRequest]] - code - gateway/web/api.py
- [[_container()]] - code - gateway/tests/test_web_api_coverage.py
- [[_fake_ws()]] - code - gateway/tests/test_web_api_coverage.py
- [[_module_state_guard()]] - code - gateway/tests/test_web_api_coverage.py
- [[client()_16]] - code - gateway/tests/test_web_api_coverage.py
- [[require_auth()]] - code - gateway/web/api.py
- [[test_web_api_coverage.py]] - code - gateway/tests/test_web_api_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_70
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Module Group 146]]
- 17 edges to [[_COMMUNITY_Module Group 126]]
- 7 edges to [[_COMMUNITY_Web API & Dashboard UI]]
- 5 edges to [[_COMMUNITY_Module Group 310]]
- 2 edges to [[_COMMUNITY_Module Group 83]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 74]]
- 1 edge to [[_COMMUNITY_Module Group 61]]
- 1 edge to [[_COMMUNITY_Module Group 93]]
- 1 edge to [[_COMMUNITY_Module Group 156]]
- 1 edge to [[_COMMUNITY_Module Group 150]]

## Top bridge nodes
- [[require_auth()]] - degree 13, connects to 7 communities
- [[UpdateRequest]] - degree 25, connects to 5 communities
- [[KillSwitchAction]] - degree 23, connects to 5 communities
- [[test_web_api_coverage.py]] - degree 27, connects to 3 communities
- [[TestRebuild]] - degree 6, connects to 2 communities