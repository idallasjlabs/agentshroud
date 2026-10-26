---
type: community
members: 42
---

# Community 129

**Members:** 42 nodes

## Members
- [[LLMProxy._apply_filters]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._build_timeout_fallback_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._emit_failover_notice]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._enforce_tool_acl]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound_streaming]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_streaming_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._forward_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_secondary_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_connect_error]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_local_oom]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_headers]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_unavailable_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_failover_base]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_secondary_failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._normalize_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._record_failover_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_inbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_request_data]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._strip_fieldflare_unsupported_fields]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._suppress_qwen3_thinking]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._widen_optional_tool_param_types]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages (non-streaming)]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages_streaming]] - code - gateway/proxy/llm_proxy.py
- [[LOCAL_MODEL_ROUTES]] - code - gateway/proxy/llm_proxy.py
- [[Rapid-MLX host.docker.internal trusted-hosts fix (local-llms repo)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[_LOCAL_BACKEND_HINTS]] - code - gateway/proxy/llm_proxy.py
- [[_telegram_send]] - code - docker/bots/hermes/start.sh
- [[google_api_proxy]] - code - gateway/ingest_api/main.py
- [[ollama_api_proxy]] - code - gateway/ingest_api/main.py
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_route_strips_unsupported_fields_streaming]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_drops_parallel_tool_calls_true_and_false]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_named_tool_choice_object_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_fieldflare_shim_rewrites_required_tool_choice_to_auto]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_local_oom_triggers_secondary_failover]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_non_fieldflare_local_route_keeps_fields]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_streaming_connect_failure_keeps_in_stream_error_frame]] - code - gateway/tests/test_llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_129
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 1278]]
- 3 edges to [[_COMMUNITY_Community 53]]
- 2 edges to [[_COMMUNITY_Community 190]]
- 2 edges to [[_COMMUNITY_Community 290]]
- 1 edge to [[_COMMUNITY_Community 1105]]

## Top bridge nodes
- [[LLMProxy.proxy_messages_streaming]] - degree 19, connects to 2 communities
- [[_telegram_send]] - degree 4, connects to 2 communities
- [[test_streaming_connect_failure_keeps_in_stream_error_frame]] - degree 3, connects to 2 communities
- [[LLMProxy.proxy_messages (non-streaming)]] - degree 26, connects to 1 community
- [[LLMProxy._normalize_local_model]] - degree 6, connects to 1 community