---
type: community
cohesion: 0.04
members: 97
---

# LLMProxy

**Cohesion:** 0.04 - loosely connected
**Members:** 97 nodes

## Members
- [[dot-__init__()_4]] - code - gateway/proxy/llm_proxy.py
- [[dot-_apply_filters()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_build_timeout_fallback_response()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_emit_failover_notice()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_enforce_tool_acl()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_streaming_event()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_forward_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_get_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_get_local_secondary_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_is_connect_error()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_backend_headers()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_backend_unavailable_response()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_failover_base()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_local_secondary_failover_request()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_normalize_local_model()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_record_failover_event()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_scan_inbound()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_scan_request_data()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_strip_fieldflare_unsupported_fields()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_widen_optional_tool_param_types()]] - code - gateway/proxy/llm_proxy.py
- [[dot-get_stats()]] - code - gateway/proxy/llm_proxy.py
- [[dot-proxy_messages()]] - code - gateway/proxy/llm_proxy.py
- [[dot-proxy_messages_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[A Gemma model that is NOT Turbo Fieldflare's exact ID still falls through to…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Add 'null' as an accepted type for every non-required tool parameter, in place.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Any_57]] - code
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats. Also enforces…]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a cloud→local failover dispatch. Returns (status, headers, body) from…]] - rationale - gateway/proxy/llm_proxy.py
- [[Attempt a local→local-secondary failover when the primary local model hits OOM.…]] - rationale - gateway/proxy/llm_proxy.py
- [[BaseException_1]] - code
- [[Build a structured 503 for an unreachable local backend. Logs one WARNING per…]] - rationale - gateway/proxy/llm_proxy.py
- [[Build provider-compatible timeout fallback message to avoid silent Telegram…]] - rationale - gateway/proxy/llm_proxy.py
- [[Fieldflare and other no-auth local backends are left untouched.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and…]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py
- [[For Ollama backend the colon is kept (Ollama expects it).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Forward request to the real LLM API provider. Retries up to 3 times on…]] - rationale - gateway/proxy/llm_proxy.py
- [[If the model already uses dashes (LM Studio native ID), normalizing again is a…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Inject per-backend auth for local backends that require it. Unlike LM Studio …]] - rationale - gateway/proxy/llm_proxy.py
- [[LLMProxy]] - code - gateway/proxy/llm_proxy.py
- [[Non-coder Qwen3 models (e.g. the 14B base) keep the generic LM Studio route —…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Only the known stalemismatched alias is rewritten; anything else forwards as-…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Persist a failover event to the audit chain if wired.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline.]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy a streaming LLM API request, yielding SSE chunks as they arrive. Used…]] - rationale - gateway/proxy/llm_proxy.py
- [[Proxy an LLM API request. Returns (status_code, response_headers,…]] - rationale - gateway/proxy/llm_proxy.py
- [[Qwen3-Coder-30B-A3B (registered opt-in coding model, served via oMLX) must win…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Remove OpenAI request fields TurboFieldfare rejects with HTTP 400, in place.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Return the bare secondary local model name, or None if not configured. Reads…]] - rationale - gateway/proxy/llm_proxy.py
- [[Returns a copy — never mutates the caller's headers dict in place.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Scan Anthropic tool_use blocks; replace denied tools with a text error block.…]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan inbound user message text for PII and injection.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan request data for PII and injection across different provider formats.]] - rationale - gateway/proxy/llm_proxy.py
- [[Send a single Telegram notice per cooldown window when failover activates.]] - rationale - gateway/proxy/llm_proxy.py
- [[True for connection-level failures (refused  unreachable  reset). Unwraps…]] - rationale - gateway/proxy/llm_proxy.py
- [[Turbo Fieldflare's exact model ID must win over the generic 'gemma' LM Studio…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_bytes_only()]] - code - gateway/proxy/llm_proxy.py
- [[_is_connect_error matches connection-level failures only.]] - rationale - gateway/tests/test_llm_proxy.py
- [[_local_failover_base resolves correct backend for secondary model.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[_read_error_body()]] - code - gateway/proxy/llm_proxy.py
- [[_stream()]] - code - gateway/proxy/llm_proxy.py
- [[_urlopen_and_read()]] - code - gateway/proxy/llm_proxy.py
- [[gemma-4-12b-it-4bit is NOT renamed — oMLX accepts it case-insensitively…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[mlx_lm backend colon is kept (no LM Studio dash convention).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX requires a bearer token, unlike LM Studiomlx_lmFieldflare.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's DeepSeek-R1-0528-Qwen3-8B must win over the generic 'deepseek-r1' -…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's gemma-4-12B-it-4bit must win over the generic 'gemma' LM Studio route,…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[oMLX's own v1models only recognizes the exact-cased, exact-suffixed ID…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[ollamaqwen314b → qwen3-14b for LM Studio backend.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_is_noop_without_the_fields()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_is_connect_error_classification()]] - code - gateway/tests/test_llm_proxy.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxy
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 25 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 13 edges to [[_COMMUNITY_gatewayteststest_llm_proxy_thinking_suppression.py (8 cases)]]
- 7 edges to [[_COMMUNITY_dot-_is_local_oom()]]
- 6 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_test_claude_via_openai_path.py_1]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py_1]]
- 2 edges to [[_COMMUNITY_is_rate_limited_post_retry]]
- 1 edge to [[_COMMUNITY__t]]

## Top bridge nodes
- [[LLMProxy]] - degree 109, connects to 10 communities
- [[dot-proxy_messages()]] - degree 21, connects to 2 communities
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - degree 5, connects to 2 communities
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - degree 4, connects to 2 communities
- [[test_fieldflare_shim_leaves_accepted_tool_choice_strings_alone()]] - degree 4, connects to 2 communities
