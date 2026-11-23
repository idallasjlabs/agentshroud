---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy"
location: "L1477"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxy
---

# _stream()

## Connections
- [[dot-_emit_failover_notice()]] - `calls` [EXTRACTED]
- [[dot-_get_local_model()]] - `calls` [EXTRACTED]
- [[dot-_is_connect_error()]] - `calls` [EXTRACTED]
- [[dot-_local_backend_headers()]] - `calls` [EXTRACTED]
- [[dot-_local_failover_base()]] - `calls` [EXTRACTED]
- [[dot-_normalize_local_model()]] - `calls` [EXTRACTED]
- [[dot-_record_failover_event()]] - `calls` [EXTRACTED]
- [[dot-base_url()]] - `indirect_call` [INFERRED]
- [[dot-proxy_messages_streaming()]] - `contains` [EXTRACTED]
- [[StreamHead]] - `calls` [EXTRACTED]
- [[_bytes_only()]] - `calls` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `calls` [EXTRACTED]
- [[is_overloaded()]] - `calls` [EXTRACTED]
- [[is_quota_exhausted()]] - `calls` [EXTRACTED]
- [[translate_openai_sse_to_anthropic()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxy
