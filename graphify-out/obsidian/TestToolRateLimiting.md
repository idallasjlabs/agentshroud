---
source_file: "gateway/tests/test_tool_acl.py"
type: "code"
community: "Tool ACL & Group RBAC"
location: "L266"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_ACL__Group_RBAC
---

# TestToolRateLimiting

## Connections
- [[.enforcer()]] - `method` [EXTRACTED]
- [[.test_per_minute_limit_exceeded_blocks()]] - `method` [EXTRACTED]
- [[.test_per_user_isolation()]] - `method` [EXTRACTED]
- [[.test_under_threshold_passes()]] - `method` [EXTRACTED]
- [[.test_unlisted_tool_always_passes()]] - `method` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[test_tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_ACL__Group_RBAC