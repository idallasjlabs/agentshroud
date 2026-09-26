---
source_file: "gateway/proxy/llm_proxy.py"
type: "rationale"
community: "test_trust_manager.py"
location: "L1598"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_trust_managerpy
---

# Scan Anthropic tool_use blocks; replace denied tools with a text error block.

## Connections
- [[._enforce_tool_acl()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_trust_managerpy