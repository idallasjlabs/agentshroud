---
source_file: "gateway/proxy/mcp_permissions.py"
type: "rationale"
community: "SOC Dashboard"
location: "L500"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_Dashboard
---

# Block non-owner tool calls that reference admin-private data paths/content.

## Connections
- [[.check_tool_parameters()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_Dashboard