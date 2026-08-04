---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L185"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestWorkspaceAccessPreserved

## Connections
- [[.test_tmp_write_allowed()_1]] - `method` [EXTRACTED]
- [[.test_workspace_subdirectory_write_allowed()]] - `method` [EXTRACTED]
- [[.test_workspace_write_allowed()_1]] - `method` [EXTRACTED]
- [[Agent can still write to its own workspace.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection
