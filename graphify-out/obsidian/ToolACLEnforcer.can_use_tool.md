---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "record_decision"
location: "233"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/record_decision
---

# ToolACLEnforcer.can_use_tool

## Connections
- [[TokenValidator.validate]] - `semantically_similar_to` [INFERRED]
- [[ToolACLEnforcer._can_use_tool_impl]] - `calls` [EXTRACTED]
- [[ToolACLEnforcer.can_use_tool_from_origin]] - `calls` [EXTRACTED]
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - `calls` [EXTRACTED]
- [[record_decision]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/record_decision