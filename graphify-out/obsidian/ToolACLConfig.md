---
source_file: "gateway/security/tool_acl.py"
type: "code"
community: "test_tool_acl.py"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_tool_aclpy
---

# ToolACLConfig

## Connections
- [[dot-__init__()_185]] - `calls` [EXTRACTED]
- [[dot-effective_admin()]] - `method` [EXTRACTED]
- [[dot-effective_collaborator_allowed()]] - `method` [EXTRACTED]
- [[dot-effective_private()]] - `method` [EXTRACTED]
- [[dot-test_collaborator_can_use_unknown_tool_when_not_denied()]] - `calls` [EXTRACTED]
- [[dot-test_group_allowlist_grants_extra_tool()]] - `calls` [EXTRACTED]
- [[dot-test_no_rbac_allows_read()]] - `calls` [EXTRACTED]
- [[dot-test_private_tool_still_blocked_even_when_deny_unknown_false()]] - `calls` [EXTRACTED]
- [[dot-test_project_allowed_tools_grant_access()]] - `calls` [EXTRACTED]
- [[Policy configuration for tool ACL enforcement. Loaded from agentshroud.yaml…]] - `rationale_for` [EXTRACTED]
- [[TestDenyUnknownFalse]] - `uses` [INFERRED]
- [[TestGroupToolAllowlist]] - `uses` [INFERRED]
- [[TestNoRBACConfig]] - `uses` [INFERRED]
- [[acl_config()]] - `uses` [INFERRED]
- [[enforcer()_3]] - `uses` [INFERRED]
- [[test_group_rbac.py]] - `imports` [EXTRACTED]
- [[test_tool_acl.py]] - `imports` [EXTRACTED]
- [[tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_tool_aclpy
