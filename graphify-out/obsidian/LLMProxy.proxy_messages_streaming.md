---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy.proxy_messages"
location: "1136"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages
---

# LLMProxy.proxy_messages_streaming

## Connections
- [[CredentialInjector.inject_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._emit_failover_notice]] - `calls` [EXTRACTED]
- [[LLMProxy._get_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._local_failover_base]] - `calls` [EXTRACTED]
- [[LLMProxy._normalize_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._record_failover_event]] - `calls` [EXTRACTED]
- [[LLMProxy._scan_request_data]] - `calls` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `calls` [EXTRACTED]
- [[is_overloaded()]] - `calls` [EXTRACTED]
- [[is_quota_exhausted()]] - `calls` [EXTRACTED]
- [[translate_openai_sse_to_anthropic()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxyproxy_messages