---
source_file: "gateway/tests/test_tool_acl.py"
type: "code"
community: "File Sandbox"
location: "L302"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/File_Sandbox
---

# TestCVE2026_9367TerminalToolDenied

## Connections
- [[.test_admin_denied_terminal_tool()]] - `method` [EXTRACTED]
- [[.test_collaborator_denied_terminal_tool()]] - `method` [EXTRACTED]
- [[.test_owner_allowed_terminal_tool()]] - `method` [EXTRACTED]
- [[.test_terminal_in_private_tools()]] - `method` [EXTRACTED]
- [[.test_terminal_tool_in_private_tools()]] - `method` [EXTRACTED]
- [[.test_terminal_tool_not_in_collab_allowed()]] - `method` [EXTRACTED]
- [[.test_viewer_denied_terminal_tool()]] - `method` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[TeamsConfig]] - `uses` [INFERRED]
- [[ToolACLConfig]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `uses` [INFERRED]
- [[terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals.]] - `rationale_for` [EXTRACTED]
- [[test_tool_acl.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/File_Sandbox