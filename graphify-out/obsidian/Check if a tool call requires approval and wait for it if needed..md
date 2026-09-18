---
source_file: "gateway/proxy/mcp_proxy.py"
type: "rationale"
community: ".process_tool_call()"
location: "L860"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/process_tool_call
---

# Check if a tool call requires approval and wait for it if needed.

## Connections
- [[.check_approval_required()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/process_tool_call