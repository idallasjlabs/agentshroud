---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "rationale"
community: "MCP Proxy Config"
location: "L938"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MCP_Proxy_Config
---

# No trust_manager configured — the hook must no-op, not crash the         request

## Connections
- [[.test_missing_trust_manager_does_not_raise()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MCP_Proxy_Config