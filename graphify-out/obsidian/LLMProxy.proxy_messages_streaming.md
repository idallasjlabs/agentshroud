---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy.proxy_messages (non-streaming)"
location: "L1202-L1590"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages_non-streaming
---

# LLMProxy.proxy_messages_streaming

## Connections
- [[LLMProxy]] - `implements` [EXTRACTED]
- [[LLMProxy._emit_failover_notice]] - `calls` [EXTRACTED]
- [[LLMProxy._get_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._is_connect_error]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._local_failover_base]] - `calls` [EXTRACTED]
- [[LLMProxy._normalize_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._record_failover_event]] - `calls` [EXTRACTED]
- [[LLMProxy._scan_request_data]] - `calls` [EXTRACTED]
- [[LLMProxy._strip_fieldflare_unsupported_fields]] - `calls` [EXTRACTED]
- [[LLMProxy._suppress_qwen3_thinking]] - `calls` [EXTRACTED]
- [[LLMProxy._widen_optional_tool_param_types]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages (non-streaming)]] - `semantically_similar_to` [EXTRACTED]
- [[LOCAL_MODEL_ROUTES]] - `references` [EXTRACTED]
- [[StreamHead]] - `shares_data_with` [EXTRACTED]
- [[_LOCAL_BACKEND_HINTS]] - `references` [EXTRACTED]
- [[_run_stream (StreamHead test harness)]] - `calls` [EXTRACTED]
- [[llm_api_proxy()]] - `calls` [EXTRACTED]
- [[test_fieldflare_route_strips_unsupported_fields_streaming]] - `calls` [EXTRACTED]
- [[test_streaming_connect_failure_keeps_in_stream_error_frame]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxyproxy_messages_non-streaming
