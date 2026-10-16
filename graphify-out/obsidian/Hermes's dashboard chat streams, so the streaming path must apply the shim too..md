---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "rationale"
community: "LLMProxy.proxy_messages (non-streaming)"
location: "L1157"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/LLMProxyproxy_messages_non-streaming
---

# Hermes's dashboard chat streams, so the streaming path must apply the shim too.

## Connections
- [[test_fieldflare_route_strips_unsupported_fields_streaming]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/LLMProxyproxy_messages_non-streaming
