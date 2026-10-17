---
type: community
members: 89
---

# test_llm_proxy_local_parity.py (2)

**Members:** 89 nodes

## Members
- [[dot-__init__()_6]] - code - gateway/proxy/llm_proxy.py
- [[dot-_flatten_fieldflare_schema()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_is_local_oom()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_merge_object_schemas()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_strip_fieldflare_unsupported_fields()]] - code - gateway/proxy/llm_proxy.py
- [[dot-get_stats()]] - code - gateway/proxy/llm_proxy.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[A Gemma model that is NOT Turbo Fieldflare's exact ID still falls through to…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[FIELDFLARE_API_BASE (TurboFieldfare 8238)]] - code - gateway/proxy/llm_proxy.py
- [[Fieldflare and other no-auth local backends are left untouched.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Fieldflare representable tool-schema subset (two-branch nullable unions only)]] - rationale - gateway/proxy/llm_proxy.py
- [[For Ollama backend the colon is kept (Ollama expects it).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[If the model already uses dashes (LM Studio native ID), normalizing again is a…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[LLM API Reverse Proxy — intercepts all OpenClaw ↔ (AnthropicOpenAIGoogle)…]] - rationale - gateway/proxy/llm_proxy.py
- [[LLMProxy]] - code - gateway/proxy/llm_proxy.py
- [[Non-coder Qwen3 models (e.g. the 14B base) keep the generic LM Studio route —…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Only the known stalemismatched alias is rewritten; anything else forwards as-…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - rationale - gateway/proxy/llm_proxy.py
- [[Qwen3-Coder-30B-A3B (registered opt-in coding model, served via oMLX) must win…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Remove OpenAI request fields TurboFieldfare rejects with HTTP 400, in place.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Return True if the response indicates a local-model OOM or backend_unavailable.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Returns a copy — never mutates the caller's headers dict in place.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Rewrite a tool-parameter JSON schema into the subset Fieldflare's Gemma…]] - rationale - gateway/proxy/llm_proxy.py
- [[Single-branch unions unwrap, null-only unions are left alone, and a union…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Turbo Fieldflare's exact model ID must win over the generic 'gemma' LM Studio…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Union several object schemas into one (see _flatten_fieldflare_schema).…]] - rationale - gateway/proxy/llm_proxy.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Workstream C — Full local-model parity for both bots. Tests that every cloud-…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom detects 'out of memory' in error message string.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom handles raw non-JSON bodies from some backends.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for cloud 429 quota errors (different failover…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns False for non-OOM raw 500 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_is_local_oom returns True for backend_unavailable 503 bodies.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_local_failover_base resolves correct backend for secondary model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_op()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[_skill_manage_like_request()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[gemma-4-12b-it-4bit is NOT renamed — oMLX accepts it case-insensitively…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[llm_proxy.py_2]] - code - gateway/proxy/llm_proxy.py
- [[mlx_lm backend colon is kept (no LM Studio dash convention).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX requires a bearer token, unlike LM Studiomlx_lmFieldflare.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's DeepSeek-R1-0528-Qwen3-8B must win over the generic 'deepseek-r1' -…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's gemma-4-12B-it-4bit must win over the generic 'gemma' LM Studio route,…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's own v1models only recognizes the exact-cased, exact-suffixed ID…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollamaqwen314b → qwen3-14b for LM Studio backend.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_collapses_type_list_to_one_concrete_type_plus_null()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_degenerate_unions()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_inlines_allof_and_recurses_into_nested_nodes()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_is_noop_without_the_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_first_branch_of_scalar_union()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_null_branch_when_merging()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_keeps_two_branch_nullable_union_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_representable_tool_schemas_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_merges_multi_branch_object_union_into_one_object()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_tolerates_malformed_tool_entries()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_backend_unavailable()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_detects_oom_in_error_message()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_handles_non_json_body()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_local_oom_raw_body_false_on_normal_500()]] - code - gateway/tests/test_llm_proxy_local_parity.py
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
- [[test_local_secondary_failover_base_routes_correctly()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_already_dashed_is_idempotent()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_lmstudio_replaces_colon_with_dash()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_mlxlm_keeps_colon()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_ollama_keeps_colon()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_gemma_passes_through_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_unknown_model_passes_through_unchanged()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxy_local_paritypy_2
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_LLMProxy]]
- 34 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)]]
- 26 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 6 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY__FakeStreamResponse]]
- 3 edges to [[_COMMUNITY_LLMProxy (3)]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py (2)]]
- 2 edges to [[_COMMUNITY_is_rate_limited_post_retry]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 1 edge to [[_COMMUNITY_LLMProxy (2)]]

## Top bridge nodes
- [[LLMProxy]] - degree 111, connects to 9 communities
- [[llm_proxy.py_2]] - degree 7, connects to 4 communities
- [[test_llm_proxy_local_parity.py]] - degree 79, connects to 2 communities
- [[dot-_is_local_oom()]] - degree 9, connects to 2 communities
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - degree 5, connects to 2 communities
