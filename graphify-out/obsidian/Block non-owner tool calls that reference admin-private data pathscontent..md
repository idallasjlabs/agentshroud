---
source_file: "gateway/proxy/mcp_permissions.py"
type: "rationale"
community: "MCP Inspector & Audit"
location: "L500"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/MCP_Inspector__Audit
---

# Block non-owner tool calls that reference admin-private data paths/content.

## Connections
- [[.check_tool_parameters()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/MCP_Inspector__Audit