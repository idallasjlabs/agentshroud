---
type: community
cohesion: 0.03
members: 81
---

# Community 54

**Cohesion:** 0.03 - loosely connected
**Members:** 81 nodes

## Members
- [[A Gemma model that is NOT Turbo Fieldflare's exact ID still falls     through to]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Anthropic-format tool_use response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Cloud mode Anthropic tool_use responses are unmodified (baseline parity).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Exception during secondary dispatch increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Fieldflare and other no-auth local backends are left untouched.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[For Ollama backend the colon is kept (Ollama expects it).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Full round-trip each model ref is normalized and dispatched to the correct back]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If no secondary is configured and primary hits OOM, 503 is returned.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If the model already uses dashes (LM Studio native ID), normalizing again is a n]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[In cloud mode, Hermes Claude model routes to Anthropic endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[LLMProxy_3]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[Non-coder Qwen3 models (e.g. the 14B base) keep the generic LM Studio     route]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OOM (503 backend_unavailable from primary local) triggers secondary local failov]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Only the known stalemismatched alias is rewritten; anything else forwards as-is]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OpenAI-format tool_calls response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary failover for Anthropic-format (v1messages) path translates and retur]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary model returning non-200 increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Unknown path (not v1messages, not is_openai) returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of ResourceWarnin]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_model strips the provider prefix for a Fieldflare ref, same     as it]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model returns None if env var is unset.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom detects 'out of memory' in error message string.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom handles raw non-JSON bodies from some backends.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for cloud 429 quota errors (different failover path)]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for successful responses.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_local_failover_base resolves correct backend for secondary model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_make_proxy()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[failover_local_secondary_succeeded stat increments on successful secondary dispa]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[gemma-4-12b-it-4bit is NOT renamed — oMLX accepts it case-insensitively     (con]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx-communitydeepseek-r1 full ID routes to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx_lm backend colon is kept (no LM Studio dash convention).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's own v1models only recognizes the exact-cased, exact-suffixed ID     'De]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollama prefix is stripped during proxy_messages dispatch and normalization foll]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollamaqwen314b → qwen3-14b for LM Studio backend.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_deepseek_r1_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_model_reads_fieldflare_ref()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_reads_env()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_returns_none_when_unset()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_openai_path_local_model_routed_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_oom_in_error_message()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_handles_non_json_body()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_200()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_quota_429()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_llm_proxy_local_parity.py]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_backend_headers_no_auth_for_fieldflare()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_other_gemma_models_still_route_to_lmstudio()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_other_qwen3_models_still_route_to_lmstudio()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_mode_openai_tool_call_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_failover_disabled_does_not_retry()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_no_secondary_falls_through_to_503()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_p99_timeout_triggers_secondary_failover()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_anthropic_path()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_base_routes_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_exception_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_secondary_non_200_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_secondary_failover_unknown_path_returns_none()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_mlx_community_deepseek_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_model_ref_round_trip()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_already_dashed_is_idempotent()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_lmstudio_replaces_colon_with_dash()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_mlxlm_keeps_colon()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_ollama_keeps_colon()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_gemma_passes_through_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_unknown_model_passes_through_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_provider_prefix_stripped_before_normalize()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_stats_local_secondary_failover_succeeded_incremented()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_54
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 225]]
- 5 edges to [[_COMMUNITY_Community 88]]
- 4 edges to [[_COMMUNITY_Community 990]]
- 3 edges to [[_COMMUNITY_Community 83]]
- 2 edges to [[_COMMUNITY_Community 1348]]
- 2 edges to [[_COMMUNITY_Community 1347]]
- 1 edge to [[_COMMUNITY_Community 126]]
- 1 edge to [[_COMMUNITY_Community 807]]

## Top bridge nodes
- [[test_llm_proxy_local_parity.py]] - degree 61, connects to 8 communities
- [[_make_proxy()]] - degree 26, connects to 2 communities
- [[test_vram_headroom_error_is_not_resource_warning()]] - degree 3, connects to 1 community
- [[LLMProxy_3]] - degree 2, connects to 1 community