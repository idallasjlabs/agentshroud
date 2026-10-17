---
type: community
members: 34
---

# LLMProxy.proxy_messages (non-streaming)

**Members:** 34 nodes

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
- [[Proxy Anthropic API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Rapid-MLX host.docker.internal trusted-hosts fix (local-llms repo)]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - concept - INCIDENT-2026-10-16-conduit-and-stability.md
- [[_LOCAL_BACKEND_HINTS]] - code - gateway/proxy/llm_proxy.py
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - code - gateway/ingest_api/main.py
- [[oMLX's own v1models only recognizes the exact-cased, exact-suffixed ID…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxyproxy_messages_non-streaming
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 5 edges to [[_COMMUNITY_LLMProxy]]
- 4 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 4 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)]]
- 3 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 2 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_SecureBrowser Skill (2)]]
- 1 edge to [[_COMMUNITY__FakeStreamResponse]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]

## Top bridge nodes
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - degree 13, connects to 5 communities
- [[LLMProxy.proxy_messages (non-streaming)]] - degree 27, connects to 3 communities
- [[LLMProxy.proxy_messages_streaming]] - degree 20, connects to 3 communities
- [[test_normalize_local_model_omlx_deepseek_renamed_to_real_catalog_id]] - degree 5, connects to 2 communities
- [[Root cause Nemotron in-band reasoning + Qwen-only no_think suffix]] - degree 4, connects to 2 communities
