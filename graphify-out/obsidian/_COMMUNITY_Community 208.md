---
type: community
members: 129
---

# Community 208

**Members:** 129 nodes

## Members
- [[.__aenter__()_5]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.__aexit__()_5]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.__init__()_174]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.aiter_bytes()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.aread()_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.block_credentials()_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.filter_xml_blocks()_2]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[.sanitize()_4]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[A Gemma model that is NOT Turbo Fieldflare's exact ID still falls     through to]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Anthropic-format tool_use response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Cloud mode Anthropic tool_use responses are unmodified (baseline parity).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Exception during secondary dispatch increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Fieldflare and other no-auth local backends are left untouched.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[For Ollama backend the colon is kept (Ollama expects it).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Full round-trip each model ref is normalized and dispatched to the correct back]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Hermes's dashboard chat streams, so the streaming path must apply the shim too.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If no secondary is configured and primary hits OOM, 503 is returned.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If the model already uses dashes (LM Studio native ID), normalizing again is a n]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[In cloud mode, Hermes Claude model routes to Anthropic endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Non-coder Qwen3 models (e.g. the 14B base) keep the generic LM Studio     route]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OOM (503 backend_unavailable from primary local) triggers secondary local failov]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Only the known stalemismatched alias is rewritten; anything else forwards as-is]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[OpenAI-format tool_calls response returns the same shape in local mode.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Qwen3-Coder-30B-A3B (registered opt-in coding model, served via oMLX)     must w]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Returns a copy — never mutates the caller's headers dict in place.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary failover for Anthropic-format (v1messages) path translates and retur]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Secondary model returning non-200 increments failed stat and returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Single-branch unions unwrap, null-only unions are left alone, and a     union ne]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[The shim must not leak onto backends that accept these fields (LM Studio).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Turbo Fieldflare's exact model ID must win over the generic 'gemma' LM     Studi]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Unknown path (not v1messages, not is_openai) returns None.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of ResourceWarnin]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_FakeSanitizer_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_FakeStreamResponse_1]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_anthropic_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_model strips the provider prefix for a Fieldflare ref, same     as it]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_get_local_secondary_model returns None if env var is unset.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom detects 'out of memory' in error message string.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom handles raw non-JSON bodies from some backends.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for cloud 429 quota errors (different failover path)]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for successful responses.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_local_failover_base resolves correct backend for secondary model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_make_proxy()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_op()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_openai_tool_use_ok()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_skill_manage_like_request()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[deepseek-r1 is routed to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[failover_local_secondary_succeeded stat increments on successful secondary dispa]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[gemma-4-12b-it-4bit is NOT renamed — oMLX accepts it case-insensitively     (con]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx-communitydeepseek-r1 full ID routes to mlx_lm endpoint.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx_lm backend colon is kept (no LM Studio dash convention).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX requires a bearer token, unlike LM Studiomlx_lmFieldflare.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's DeepSeek-R1-0528-Qwen3-8B must win over the generic     'deepseek-r1' -]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's gemma-4-12B-it-4bit must win over the generic 'gemma' LM Studio     route]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's own v1models only recognizes the exact-cased, exact-suffixed ID     'De]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollama prefix is stripped during proxy_messages dispatch and normalization foll]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollamaqwen314b → qwen3-14b for LM Studio backend.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[proxy_messages applies the shim only on the Fieldflare route, before forwarding.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_cloud_mode_anthropic_tool_use_shape_passes_through()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_deepseek_r1_routes_to_mlxlm()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_route_strips_unsupported_fields_streaming()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_collapses_type_list_to_one_concrete_type_plus_null()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_degenerate_unions()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_inlines_allof_and_recurses_into_nested_nodes()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_is_noop_without_the_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_first_branch_of_scalar_union()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_null_branch_when_merging()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_two_branch_nullable_union_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_representable_tool_schemas_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_merges_multi_branch_object_union_into_one_object()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_tolerates_malformed_tool_entries()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_model_reads_fieldflare_ref()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_reads_env()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_get_local_secondary_model_returns_none_when_unset()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_cloud_mode_uses_anthropic_endpoint()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_hermes_openai_path_local_model_routed_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_backend_unavailable()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_oom_in_error_message()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_handles_non_json_body()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_200()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_returns_false_for_quota_429()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_llm_proxy_local_parity.py]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_backend_headers_does_not_mutate_input()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_backend_headers_injects_bearer_token_for_omlx()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_backend_headers_no_auth_for_fieldflare()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_other_gemma_models_still_route_to_lmstudio()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_other_qwen3_models_still_route_to_lmstudio()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_fieldflare_gemma_before_generic_gemma()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_omlx_deepseek_r1_qwen3_8b()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_omlx_gemma_before_generic_gemma()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_failover_base_routes_omlx_qwen3_coder_before_generic_qwen3()]] - code - gateway/tests/test_llm_proxy_local_parity.py
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
- [[test_non_fieldflare_local_route_keeps_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
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
TABLE source_file, type FROM #community/Community_208
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 5]]
- 4 edges to [[_COMMUNITY_Community 1278]]
- 1 edge to [[_COMMUNITY_Community 360]]

## Top bridge nodes
- [[test_llm_proxy_local_parity.py]] - degree 81, connects to 3 communities
- [[_make_proxy()]] - degree 28, connects to 2 communities
- [[_FakeStreamResponse_1]] - degree 11, connects to 2 communities
- [[_FakeSanitizer_1]] - degree 9, connects to 2 communities
- [[test_vram_headroom_error_is_not_resource_warning()]] - degree 3, connects to 1 community