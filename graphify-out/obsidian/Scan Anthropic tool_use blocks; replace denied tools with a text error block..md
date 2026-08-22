---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "Llm Proxy (proxy)"
location: "L1490"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Llm_Proxy_proxy
---

# Scan Anthropic tool_use blocks; replace denied tools with a text error block.

## Connections
- [[._enforce_tool_acl()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Llm_Proxy_proxy