---
source_file: "gateway/tests/test_llm_proxy.py"
type: "rationale"
community: "Llm Proxy"
location: "L683"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Llm_Proxy
---

# No streaming call site may hardcode its own connect timeout literal.      Guards

## Connections
- [[test_all_streaming_clients_use_the_shared_connect_timeout_constant()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Llm_Proxy