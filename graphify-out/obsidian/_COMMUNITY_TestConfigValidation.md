---
type: community
members: 11
---

# TestConfigValidation

**Members:** 11 nodes

## Members
- [[dot-test_empty_content_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_invalid_router_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_invalid_source_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_invalid_target_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_router_url_must_be_localhost_or_openclaw()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_startup_telegram_calls_use_system_header()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_valid_forward_request()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_valid_router_url_accepted()]] - code - gateway/tests/test_config_validation.py
- [[GatewayConfig validation behavior.]] - rationale - gateway/tests/test_config_validation.py
- [[Startup notification Telegram calls should be marked as system-originated.]] - rationale - gateway/tests/test_config_validation.py
- [[TestConfigValidation]] - code - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestConfigValidation
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_GatewayConfig]]
- 4 edges to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_recovers_corrupt_json]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_removes_legacy_gateway_model_key]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_version_pin_is_consistent_across_bot_images]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_sets_control_ui_allowed_origins]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_seeds_group_allowlist]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_uses_multi_group_allowlist_var]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_script_emits_per_chat_group_agents]]
- 1 edge to [[_COMMUNITY_dot-test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_allowed_network_default_includes_current_subnets]]
- 1 edge to [[_COMMUNITY_dot-test_lifespan_op_prewarm_guarded_against_pytest]]
- 1 edge to [[_COMMUNITY_dot-test_startup_wrapper_defaults_openclaw_bind_to_loopback]]
- 1 edge to [[_COMMUNITY_dot-test_main_compose_sets_openclaw_bind_lan_default]]
- 1 edge to [[_COMMUNITY_dot-test_startup_notifications_use_minimal_message_format]]
- 1 edge to [[_COMMUNITY_dot-test_startup_notifications_wait_for_runtime_readiness]]
- 1 edge to [[_COMMUNITY_dot-test_startup_online_notice_sent_only_after_readiness_gate]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_startup_telegram_calls_use_system_header]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_dockerfile_installs_xxd]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_openai_api_key_wired_via_secret]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_dashboard_insecure_optin_is_loopback_bounded]]
- 1 edge to [[_COMMUNITY_dot-test_patch_slack_sdk_pong_patch_is_idempotent]]
- 1 edge to [[_COMMUNITY_dot-test_start_control_center_script_uses_repo_relative_exec]]
- 1 edge to [[_COMMUNITY_dot-test_chat_console_script_uses_repo_relative_exec]]
- 1 edge to [[_COMMUNITY_dot-test_switch_model_script_exists_with_supported_targets]]
- 1 edge to [[_COMMUNITY_dot-test_switch_model_script_uses_current_target_syntax]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_patch_defaults_to_qwen_local_model]]
- 1 edge to [[_COMMUNITY_dot-test_compose_sets_nemotron_local_model_overrides]]
- 1 edge to [[_COMMUNITY_dot-test_startup_script_skips_anthropic_when_local_model_selected]]
- 1 edge to [[_COMMUNITY_dot-test_init_config_skips_anthropic_auth_seed_for_local_model]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_soul_documents_ssh_hosts]]
- 1 edge to [[_COMMUNITY_dot-test_hermes_soul_has_no_refuse_directive]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_soul_has_no_refuse_directive]]
- 1 edge to [[_COMMUNITY_dot-test_gateway_yaml_ssh_hosts_cover_all_lab_hosts]]
- 1 edge to [[_COMMUNITY_dot-test_openclaw_ssh_config_allows_all_lab_hosts]]

## Top bridge nodes
- [[TestConfigValidation]] - degree 45, connects to 36 communities
- [[dot-test_empty_content_rejected()]] - degree 2, connects to 1 community
- [[dot-test_invalid_router_url_rejected()]] - degree 2, connects to 1 community
- [[dot-test_invalid_source_rejected()]] - degree 2, connects to 1 community
- [[dot-test_invalid_target_url_rejected()]] - degree 2, connects to 1 community
