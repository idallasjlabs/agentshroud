---
source_file: "gateway/proxy/mcp_permissions.py"
type: "rationale"
community: "GitGuard"
location: "L500"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/GitGuard
---

# Block non-owner tool calls that reference admin-private data paths/content.

## Connections
- [[.check_tool_parameters()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/GitGuard