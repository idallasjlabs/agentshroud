---
type: community
cohesion: 1.00
members: 2
---

# Tool Acl (security)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[PRIVATE_TOOLS (owner-only tool set)]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tool_Acl_security
SORT file.name ASC
```
