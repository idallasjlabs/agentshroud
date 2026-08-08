---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "Gateway Proxy Layer"
location: "L1267"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Proxy_Layer
---

# Scan Anthropic tool_use blocks; replace denied tools with a text error block.

## Connections
- [[._enforce_tool_acl()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Proxy_Layer