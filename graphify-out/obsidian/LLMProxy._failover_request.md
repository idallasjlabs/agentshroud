---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "LLMProxy.proxy_messages"
location: "line:607"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages
---

# LLMProxy._failover_request

## Connections
- [[LLMProxy._forward_request]] - `calls` [EXTRACTED]
- [[LLMProxy._get_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy._local_backend_headers]] - `calls` [EXTRACTED]
- [[LLMProxy._local_failover_base]] - `calls` [EXTRACTED]
- [[LLMProxy._normalize_local_model]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages]] - `calls` [EXTRACTED]
- [[anthropic_to_openai_request()]] - `calls` [EXTRACTED]
- [[gemini_failover_unsupported_reason()]] - `calls` [EXTRACTED]
- [[gemini_to_openai_request()]] - `calls` [EXTRACTED]
- [[openai_to_anthropic_response()]] - `calls` [EXTRACTED]
- [[openai_to_gemini_response()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLMProxyproxy_messages