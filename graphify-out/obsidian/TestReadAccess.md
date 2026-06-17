---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L210"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestReadAccess

## Connections
- [[.test_gateway_source_read_flagged()]] - `method` [EXTRACTED]
- [[.test_sensitive_config_read_blocked()]] - `method` [EXTRACTED]
- [[.test_system_info_read_allowed()]] - `method` [EXTRACTED]
- [[.test_workspace_read_allowed()_1]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[Test read access controls.]] - `rationale_for` [EXTRACTED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection