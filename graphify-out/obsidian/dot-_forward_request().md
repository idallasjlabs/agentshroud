---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: ".proxy_messages"
location: "L1905"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/proxy_messages
---

# ._forward_request()

## Connections
- [[dot-_failover_request()]] - `calls` [EXTRACTED]
- [[dot-_local_secondary_failover_request()]] - `calls` [EXTRACTED]
- [[dot-proxy_messages()]] - `calls` [EXTRACTED]
- [[Forward request to the real LLM API provider. Retries up to 3 times on…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy]] - `method` [EXTRACTED]
- [[_read_error_body()]] - `indirect_call` [INFERRED]
- [[_urlopen_and_read()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/proxy_messages
