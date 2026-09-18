---
type: community
cohesion: 0.05
members: 43
---

# TestConfigValidation

**Cohesion:** 0.05 - loosely connected
**Members:** 43 nodes

## Members
- [[.test_compose_sets_nemotron_local_model_overrides()]] - code - gateway/tests/test_config_validation.py
- [[.test_empty_content_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_gateway_yaml_ssh_hosts_cover_all_lab_hosts()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_dashboard_insecure_optin_is_loopback_bounded()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_openai_api_key_wired_via_secret()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_soul_has_no_refuse_directive()]] - code - gateway/tests/test_config_validation.py
- [[.test_init_config_skips_anthropic_auth_seed_for_local_model()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_router_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_source_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_target_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_main_compose_sets_openclaw_bind_lan_default()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_defaults_to_qwen_local_model()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_emits_per_chat_group_agents()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_seeds_group_allowlist()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_soul_has_no_refuse_directive()]] - code - gateway/tests/test_config_validation.py
- [[.test_patch_slack_sdk_pong_patch_is_idempotent()]] - code - gateway/tests/test_config_validation.py
- [[.test_proxy_allowed_network_default_includes_current_subnets()]] - code - gateway/tests/test_config_validation.py
- [[.test_router_url_must_be_localhost_or_openclaw()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_notifications_wait_for_runtime_readiness()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_online_notice_sent_only_after_readiness_gate()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_script_skips_anthropic_when_local_model_selected()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_wrapper_defaults_openclaw_bind_to_loopback()]] - code - gateway/tests/test_config_validation.py
- [[.test_valid_forward_request()]] - code - gateway/tests/test_config_validation.py
- [[.test_valid_router_url_accepted()]] - code - gateway/tests/test_config_validation.py
- [[Bot startup should not load Anthropic secrets when Ollama local model is…]] - rationale - gateway/tests/test_config_validation.py
- [[GatewayConfig validation behavior.]] - rationale - gateway/tests/test_config_validation.py
- [[HERMES_DASHBOARD_INSECURE may only be enabled with a loopback-only host…]] - rationale - gateway/tests/test_config_validation.py
- [[Hermes SOUL.md must instruct the agent never to issue a blanket 'cannot…]] - rationale - gateway/tests/test_config_validation.py
- [[Hermes must receive OPENAI_API_KEY from the shared openai_api_key Docker…]] - rationale - gateway/tests/test_config_validation.py
- [[Init config should seed auth profiles for cloud providers and Ollama in local…]] - rationale - gateway/tests/test_config_validation.py
- [[Main compose stack should expose a single model-mode switch with localcloud…]] - rationale - gateway/tests/test_config_validation.py
- [[Online notice must appear after readiness probes to avoid premature status…]] - rationale - gateway/tests/test_config_validation.py
- [[OpenClaw SOUL.md must carry the same 'never blanket-refuse cannot connect'…]] - rationale - gateway/tests/test_config_validation.py
- [[OpenClaw patch script should default to local Ollama but keep API adapter…]] - rationale - gateway/tests/test_config_validation.py
- [[Primary compose stack should bind OpenClaw gateway to lan by default for host…]] - rationale - gateway/tests/test_config_validation.py
- [[Proxy CIDR fallback should include current 10.254 ranges plus legacy…]] - rationale - gateway/tests/test_config_validation.py
- [[Startup script should verify Telegrammodel readiness before sending online…]] - rationale - gateway/tests/test_config_validation.py
- [[Startup wrapper should default OpenClaw bind to loopback unless explicitly…]] - rationale - gateway/tests/test_config_validation.py
- [[TestConfigValidation]] - code - gateway/tests/test_config_validation.py
- [[agentshroud.yaml must define all three lab hosts in ssh.hosts as agentshroud-…]] - rationale - gateway/tests/test_config_validation.py
- [[apply-patches.js must create per-chat group-{chatId} agents for the approval…]] - rationale - gateway/tests/test_config_validation.py
- [[openclaw init patch script must seed Telegram group allowlist when policy is…]] - rationale - gateway/tests/test_config_validation.py
- [[patch-slack-sdk.sh must stay quiet when the pong patch is already applied. The…]] - rationale - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestConfigValidation
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_.test_chat_console_script_uses_repo_relative_exe]]
- 1 edge to [[_COMMUNITY_.test_hermes_dockerfile_installs_xxd()]]
- 1 edge to [[_COMMUNITY_.test_hermes_soul_documents_ssh_hosts()]]
- 1 edge to [[_COMMUNITY_.test_hermes_startup_telegram_calls_use_system_h]]
- 1 edge to [[_COMMUNITY_.test_lifespan_op_prewarm_guarded_against_pytest]]
- 1 edge to [[_COMMUNITY_.test_lifespan_uvicorn_warning_filter_drops_inva]]
- 1 edge to [[_COMMUNITY_.test_openclaw_patch_script_recovers_corrupt_jso]]
- 1 edge to [[_COMMUNITY_.test_openclaw_patch_script_removes_legacy_gatew]]
- 1 edge to [[_COMMUNITY_.test_openclaw_patch_script_sets_control_ui_allo]]
- 1 edge to [[_COMMUNITY_.test_openclaw_patch_script_uses_multi_group_all]]
- 1 edge to [[_COMMUNITY_.test_openclaw_ssh_config_allows_all_lab_hosts()]]
- 1 edge to [[_COMMUNITY_.test_openclaw_version_pin_is_consistent_across_]]
- 1 edge to [[_COMMUNITY_.test_start_control_center_script_uses_repo_rela]]
- 1 edge to [[_COMMUNITY_.test_startup_notifications_use_minimal_message_]]
- 1 edge to [[_COMMUNITY_.test_startup_telegram_calls_use_system_header()]]
- 1 edge to [[_COMMUNITY_.test_switch_model_script_exists_with_supported_]]
- 1 edge to [[_COMMUNITY_.test_switch_model_script_uses_current_target_sy]]
- 1 edge to [[_COMMUNITY_TestConfigValidation]]

## Top bridge nodes
- [[TestConfigValidation]] - degree 43, connects to 18 communities
- [[GatewayConfig validation behavior.]] - degree 2, connects to 1 community