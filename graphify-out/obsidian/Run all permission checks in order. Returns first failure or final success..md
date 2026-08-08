---
source_file: "gateway/proxy/mcp_permissions.py"
type: "rationale"
community: "MCP Proxy Config"
location: "L626"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MCP_Proxy_Config
---

# Run all permission checks in order. Returns first failure or final success.

## Connections
- [[.check_all()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MCP_Proxy_Config