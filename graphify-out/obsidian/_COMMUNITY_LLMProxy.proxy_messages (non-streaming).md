---
type: community
members: 51
---

# LLMProxy.proxy_messages (non-streaming)

**Members:** 51 nodes

## Members
- [[Alias for Hermes Anthropic SDK's apiv1 preflight path. Some Anthropic SDK…]] - rationale - gateway/ingest_api/main.py
- [[Alias for hermes v0.16.0+'s OpenAI client. Hermes upgraded to v0.16.0 on…]] - rationale - gateway/ingest_api/main.py
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
- [[Proxy Google Gemini API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Proxy bot Slack Web API calls through SecurityPipeline. Restricted to the…]] - rationale - gateway/ingest_api/main.py
- [[Proxy native Ollama API calls through security pipeline.]] - rationale - gateway/ingest_api/main.py
- [[Redirect bare hermes-dashboard to hermes-dashboard so assets resolve.]] - rationale - gateway/ingest_api/main.py
- [[Request_1]] - code
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Set a user's role (owner only).]] - rationale - gateway/ingest_api/main.py
- [[Store a report in the gateway-managed multi-bot report store. Body {bot…]] - rationale - gateway/ingest_api/main.py
- [[_LOCAL_BACKEND_HINTS]] - code - gateway/proxy/llm_proxy.py
- [[api_route]] - code
- [[create_report()]] - code - gateway/ingest_api/main.py
- [[google_api_proxy]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_root]] - code - gateway/ingest_api/main.py
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - code - gateway/ingest_api/main.py
- [[llm_api_v1_prefix_alias]] - code - gateway/ingest_api/main.py
- [[llm_openai_chat_alias]] - code - gateway/ingest_api/main.py
- [[ollama_api_proxy]] - code - gateway/ingest_api/main.py
- [[put]] - code
- [[set_user_role()]] - code - gateway/ingest_api/main.py
- [[slack_api_proxy()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LLMProxyproxy_messages_non-streaming
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)_1]]
- 5 edges to [[_COMMUNITY_Request]]
- 5 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 4 edges to [[_COMMUNITY_test_main_endpoints.py (2)]]
- 3 edges to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 3 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)]]
- 2 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy) (2)]]
- 2 edges to [[_COMMUNITY_SecureBrowser Skill (2) (2)]]
- 2 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 2 edges to [[_COMMUNITY_test_hermes_cron_seed.py]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py (3)]]
- 1 edge to [[_COMMUNITY_AgentTarget (5)]]
- 1 edge to [[_COMMUNITY__FakeStreamResponse]]
- 1 edge to [[_COMMUNITY_LLMProxy (2)]]

## Top bridge nodes
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - degree 13, connects to 6 communities
- [[Request_1]] - degree 22, connects to 5 communities
- [[LLMProxy.proxy_messages_streaming]] - degree 20, connects to 4 communities
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - degree 13, connects to 4 communities
- [[LLMProxy.proxy_messages (non-streaming)]] - degree 27, connects to 2 communities
