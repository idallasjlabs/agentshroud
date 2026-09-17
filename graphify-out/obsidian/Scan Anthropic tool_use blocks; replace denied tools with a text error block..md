---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: ".proxy_messages()"
location: "L1598"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/proxy_messages
---

# Scan Anthropic tool_use blocks; replace denied tools with a text error block.

## Connections
- [[._enforce_tool_acl()]] - `rationale_for` [EXTRACTED]
- [[._enforce_tool_acl()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/proxy_messages