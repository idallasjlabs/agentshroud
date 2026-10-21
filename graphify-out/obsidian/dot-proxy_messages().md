---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: ".proxy_messages()"
location: "L970"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/proxy_messages
---

# .proxy_messages()

## Connections
- [[dot-_build_timeout_fallback_response()]] - `calls` [EXTRACTED]
- [[dot-_emit_failover_notice()]] - `calls` [EXTRACTED]
- [[dot-_enforce_tool_acl()]] - `calls` [EXTRACTED]
- [[dot-_failover_request()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound()]] - `calls` [EXTRACTED]
- [[dot-_filter_outbound_streaming()]] - `calls` [EXTRACTED]
- [[dot-_forward_request()]] - `calls` [EXTRACTED]
- [[dot-_get_local_model()]] - `calls` [EXTRACTED]
- [[dot-_is_connect_error()]] - `calls` [EXTRACTED]
- [[dot-_is_local_oom()]] - `calls` [EXTRACTED]
- [[dot-_local_backend_headers()]] - `calls` [EXTRACTED]
- [[dot-_local_backend_unavailable_response()]] - `calls` [EXTRACTED]
- [[dot-_local_secondary_failover_request()]] - `calls` [EXTRACTED]
- [[dot-_normalize_local_model()]] - `calls` [EXTRACTED]
- [[dot-_record_failover_event()]] - `calls` [EXTRACTED]
- [[dot-_scan_request_data()]] - `calls` [EXTRACTED]
- [[dot-_strip_fieldflare_unsupported_fields()]] - `calls` [EXTRACTED]
- [[dot-_suppress_qwen3_thinking()]] - `calls` [EXTRACTED]
- [[dot-_widen_optional_tool_param_types()]] - `calls` [EXTRACTED]
- [[LLMProxy]] - `method` [EXTRACTED]
- [[Proxy an LLM API request. Returns (status_code, response_headers,…]] - `rationale_for` [EXTRACTED]
- [[test_fieldflare_route_strips_unsupported_fields_non_streaming]] - `calls` [INFERRED]
- [[test_non_fieldflare_local_route_keeps_fields]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/proxy_messages
