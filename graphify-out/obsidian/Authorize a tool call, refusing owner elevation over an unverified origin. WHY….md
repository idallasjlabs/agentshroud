---
source_file: "gateway/security/tool_acl.py"
type: "rationale"
community: "ToolACLEnforcer"
location: "L469"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ToolACLEnforcer
---

# Authorize a tool call, refusing owner elevation over an unverified origin. WHY…

## Connections
- [[.can_use_tool_from_origin()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ToolACLEnforcer