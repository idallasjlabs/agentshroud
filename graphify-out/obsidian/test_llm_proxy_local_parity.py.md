---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_llm_proxy_local_parity.py

## Connections
- [[LLMProxy]] - `imports` [EXTRACTED]
- [[ResourceGuard]] - `imports` [EXTRACTED]
- [[ResourceLimits]] - `imports` [EXTRACTED]
- [[VRAMHeadroomError]] - `imports` [EXTRACTED]
- [[_FakeSanitizer_1]] - `contains` [EXTRACTED]
- [[_anthropic_ok()]] - `contains` [EXTRACTED]
- [[_anthropic_tool_use_ok()]] - `contains` [EXTRACTED]
- [[_make_proxy()]] - `contains` [EXTRACTED]
- [[_openai_ok()]] - `contains` [EXTRACTED]
- [[_openai_tool_use_ok()]] - `contains` [EXTRACTED]
- [[llm_proxy.py]] - `references` [EXTRACTED]
- [[resource_guard.py]] - `references` [EXTRACTED]
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - `contains` [EXTRACTED]
- [[test_deepseek_r1_routes_to_mlxlm()]] - `contains` [EXTRACTED]
- [[test_get_local_model_reads_fieldflare_ref()]] - `contains` [EXTRACTED]
- [[test_get_local_secondary_model_reads_env()]] - `contains` [EXTRACTED]
- [[test_get_local_secondary_model_returns_none_when_unset()]] - `contains` [EXTRACTED]
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - `contains` [EXTRACTED]
- [[test_hermes_openai_path_local_model_routed_correctly()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_detects_backend_unavailable()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_detects_oom_in_error_message()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_handles_non_json_body()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_returns_false_for_200()]] - `contains` [EXTRACTED]
- [[test_is_local_oom_returns_false_for_quota_429()]] - `contains` [EXTRACTED]
- [[test_local_backend_headers_does_not_mutate_input()]] - `contains` [EXTRACTED]
- [[test_local_backend_headers_injects_bearer_token_for_omlx()]] - `contains` [EXTRACTED]
- [[test_local_backend_headers_no_auth_for_fieldflare()]] - `contains` [EXTRACTED]
- [[test_local_failover_base_other_gemma_models_still_route_to_lmstudio()]] - `contains` [EXTRACTED]
- [[test_local_failover_base_routes_fieldflare_gemma_before_generic_gemma()]] - `contains` [EXTRACTED]
- [[test_local_failover_base_routes_omlx_deepseek_r1_qwen3_8b()]] - `contains` [EXTRACTED]
- [[test_local_failover_base_routes_omlx_gemma_before_generic_gemma()]] - `contains` [EXTRACTED]
- [[test_local_mode_anthropic_tool_use_shape_passes_through()]] - `contains` [EXTRACTED]
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - `contains` [EXTRACTED]
- [[test_local_oom_failover_disabled_does_not_retry()]] - `contains` [EXTRACTED]
- [[test_local_oom_no_secondary_falls_through_to_503()]] - `contains` [EXTRACTED]
- [[test_local_oom_triggers_secondary_failover()]] - `contains` [EXTRACTED]
- [[test_local_p99_timeout_triggers_secondary_failover()]] - `contains` [EXTRACTED]
- [[test_local_secondary_failover_anthropic_path()]] - `contains` [EXTRACTED]
- [[test_local_secondary_failover_base_routes_correctly()]] - `contains` [EXTRACTED]
- [[test_local_secondary_failover_exception_returns_none()]] - `contains` [EXTRACTED]
- [[test_local_secondary_failover_secondary_non_200_returns_none()]] - `contains` [EXTRACTED]
- [[test_local_secondary_failover_unknown_path_returns_none()]] - `contains` [EXTRACTED]
- [[test_mlx_community_deepseek_routes_to_mlxlm()]] - `contains` [EXTRACTED]
- [[test_model_ref_round_trip()]] - `contains` [EXTRACTED]
- [[test_normalize_local_model_already_dashed_is_idempotent()]] - `contains` [EXTRACTED]
- [[test_normalize_local_model_lmstudio_replaces_colon_with_dash()]] - `contains` [EXTRACTED]
- [[test_normalize_local_model_mlxlm_keeps_colon()]] - `contains` [EXTRACTED]
- [[test_normalize_local_model_ollama_keeps_colon()]] - `contains` [EXTRACTED]
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - `contains` [EXTRACTED]
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - `contains` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - `contains` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - `contains` [EXTRACTED]
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - `contains` [EXTRACTED]
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - `contains` [EXTRACTED]
- [[test_vram_headroom_error_is_not_resource_warning()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite