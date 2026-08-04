---
type: community
cohesion: 0.03
members: 63
---

# Config Validation Tests

**Cohesion:** 0.03 - loosely connected
**Members:** 63 nodes

## Members
- [[.test_chat_console_script_uses_repo_relative_exec()]] - code - gateway/tests/test_config_validation.py
- [[.test_compose_sets_qwen_local_model_overrides()]] - code - gateway/tests/test_config_validation.py
- [[.test_empty_content_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_dashboard_insecure_optin_is_loopback_bounded()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_dockerfile_installs_xxd()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_openai_api_key_wired_via_secret()]] - code - gateway/tests/test_config_validation.py
- [[.test_hermes_startup_telegram_calls_use_system_header()]] - code - gateway/tests/test_config_validation.py
- [[.test_init_config_skips_anthropic_auth_seed_for_local_model()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_router_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_source_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_invalid_target_url_rejected()]] - code - gateway/tests/test_config_validation.py
- [[.test_lifespan_op_prewarm_guarded_against_pytest()]] - code - gateway/tests/test_config_validation.py
- [[.test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - code - gateway/tests/test_config_validation.py
- [[.test_main_compose_sets_openclaw_bind_lan_default()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_defaults_to_qwen_local_model()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_recovers_corrupt_json()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_removes_legacy_gateway_model_key()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_seeds_group_allowlist()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_patch_script_sets_control_ui_allowed_origins()]] - code - gateway/tests/test_config_validation.py
- [[.test_openclaw_version_pin_is_consistent_across_bot_images()]] - code - gateway/tests/test_config_validation.py
- [[.test_patch_slack_sdk_pong_patch_is_idempotent()]] - code - gateway/tests/test_config_validation.py
- [[.test_proxy_allowed_network_default_includes_current_subnets()]] - code - gateway/tests/test_config_validation.py
- [[.test_router_url_must_be_localhost_or_openclaw()]] - code - gateway/tests/test_config_validation.py
- [[.test_start_control_center_script_uses_repo_relative_exec()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_notifications_use_minimal_message_format()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_notifications_wait_for_runtime_readiness()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_online_notice_sent_only_after_readiness_gate()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_script_skips_anthropic_when_local_model_selected()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_telegram_calls_use_system_header()]] - code - gateway/tests/test_config_validation.py
- [[.test_startup_wrapper_defaults_openclaw_bind_to_loopback()]] - code - gateway/tests/test_config_validation.py
- [[.test_switch_model_script_exists_with_supported_targets()]] - code - gateway/tests/test_config_validation.py
- [[.test_switch_model_script_uses_current_target_syntax()]] - code - gateway/tests/test_config_validation.py
- [[.test_valid_forward_request()]] - code - gateway/tests/test_config_validation.py
- [[.test_valid_router_url_accepted()]] - code - gateway/tests/test_config_validation.py
- [[Bot startup should not load Anthropic secrets when Ollama local model is configu]] - rationale - gateway/tests/test_config_validation.py
- [[Both bot Dockerfiles must pin OpenClaw to the same value         (either both a]] - rationale - gateway/tests/test_config_validation.py
- [[Chat console launcher should be robust to current working directory.]] - rationale - gateway/tests/test_config_validation.py
- [[Control center launcher should be robust to current working directory.]] - rationale - gateway/tests/test_config_validation.py
- [[GatewayConfig validation behavior.]] - rationale - gateway/tests/test_config_validation.py
- [[HERMES_DASHBOARD_INSECURE may only be enabled with a loopback-only host publish.]] - rationale - gateway/tests/test_config_validation.py
- [[Hermes Dockerfile must install xxd — terminal_tool hex dumps fail without it.]] - rationale - gateway/tests/test_config_validation.py
- [[Hermes must receive OPENAI_API_KEY from the shared openai_api_key Docker secret.]] - rationale - gateway/tests/test_config_validation.py
- [[Hermes startup notifications must use X-AgentShroud-System 1 (bypasses content]] - rationale - gateway/tests/test_config_validation.py
- [[Init config should seed auth profiles for cloud providers and Ollama in local mo]] - rationale - gateway/tests/test_config_validation.py
- [[Lifespan filter should suppress repeated malformed HTTP warning noise.]] - rationale - gateway/tests/test_config_validation.py
- [[Main compose stack should expose a single model-mode switch with localcloud ref]] - rationale - gateway/tests/test_config_validation.py
- [[Model switch helper should support local and major cloud providers.]] - rationale - gateway/tests/test_config_validation.py
- [[Online notice must appear after readiness probes to avoid premature status signa]] - rationale - gateway/tests/test_config_validation.py
- [[OpenClaw patch script should default to local Ollama but keep API adapter config]] - rationale - gateway/tests/test_config_validation.py
- [[Operator guidance should use valid switch_model target syntax (no legacy cloud p]] - rationale - gateway/tests/test_config_validation.py
- [[Primary compose stack should bind OpenClaw gateway to lan by default for host Co]] - rationale - gateway/tests/test_config_validation.py
- [[Proxy CIDR fallback should include current 10.254 ranges plus legacy compatibili]] - rationale - gateway/tests/test_config_validation.py
- [[Startup notification Telegram calls should be marked as system-originated.]] - rationale - gateway/tests/test_config_validation.py
- [[Startup script should verify Telegrammodel readiness before sending online noti]] - rationale - gateway/tests/test_config_validation.py
- [[Startup wrapper should default OpenClaw bind to loopback unless explicitly overr]] - rationale - gateway/tests/test_config_validation.py
- [[Startupshutdown notifications should use minimal, non-identifying text.]] - rationale - gateway/tests/test_config_validation.py
- [[TestConfigValidation]] - code - gateway/tests/test_config_validation.py
- [[The 1Password prewarm thread must never spawn real op subprocesses under pytest.]] - rationale - gateway/tests/test_config_validation.py
- [[openclaw init patch script must quarantine malformed JSON instead of exiting.]] - rationale - gateway/tests/test_config_validation.py
- [[openclaw init patch script must remove unsupported gateway.model key.]] - rationale - gateway/tests/test_config_validation.py
- [[openclaw init patch script must seed Telegram group allowlist when policy is all]] - rationale - gateway/tests/test_config_validation.py
- [[openclaw init patch script must seed control UI origins for non-loopback bind.]] - rationale - gateway/tests/test_config_validation.py
- [[patch-slack-sdk.sh must stay quiet when the pong patch is already applied.]] - rationale - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Config_Validation_Tests
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 4 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 99]]

## Top bridge nodes
- [[TestConfigValidation]] - degree 38, connects to 3 communities
- [[.test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - degree 3, connects to 1 community
- [[.test_empty_content_rejected()]] - degree 2, connects to 1 community
- [[.test_invalid_router_url_rejected()]] - degree 2, connects to 1 community
- [[.test_invalid_source_rejected()]] - degree 2, connects to 1 community
