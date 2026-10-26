---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "Community 129"
location: "L834-L1200"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_129
---

# LLMProxy.proxy_messages (non-streaming)

## Connections
- [[LLMProxy]] - `implements` [EXTRACTED]
- [[LLMProxy._build_timeout_fallback_response]] - `calls` [EXTRACTED]
- [[LLMProxy._emit_failover_notice]] - `calls` [EXTRACTED]
- [[LLMProxy._enforce_tool_acl]] - `calls` [EXTRACTED]
- [[LLMProxy._failover_request]] - `calls` [EXTRACTED]
- [[LLMProxy._filter_outbound]] - `calls` [EXTRACTED]
- [[LLMProxy._filter_outbound_streaming]] - `calls` [EXTRACTED]
- [[LLMProxy._forward_request]] - `calls` [EXTRACTED]
- [[LLMProxy._get_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._is_connect_error]] - `calls` [EXTRACTED]
- [[LLMProxy._is_local_oom]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_unavailable_response]] - `calls` [EXTRACTED]
- [[LLMProxy._local_secondary_failover_request]] - `calls` [EXTRACTED]
- [[LLMProxy._normalize_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._record_failover_event]] - `calls` [EXTRACTED]
- [[LLMProxy._scan_request_data]] - `calls` [EXTRACTED]
- [[LLMProxy._strip_fieldflare_unsupported_fields]] - `calls` [EXTRACTED]
- [[LLMProxy._suppress_qwen3_thinking]] - `calls` [EXTRACTED]
- [[LLMProxy._widen_optional_tool_param_types]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages_streaming]] - `semantically_similar_to` [EXTRACTED]
- [[LOCAL_MODEL_ROUTES]] - `references` [EXTRACTED]
- [[google_api_proxy]] - `calls` [EXTRACTED]
- [[ollama_api_proxy]] - `calls` [EXTRACTED]
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming]] - `calls` [EXTRACTED]
- [[test_non_fieldflare_local_route_keeps_fields]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_129