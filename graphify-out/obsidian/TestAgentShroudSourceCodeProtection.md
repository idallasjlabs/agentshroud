---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Privilege Separation & File Sandbox"
location: "L63"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Privilege_Separation__File_Sandbox
---

# TestAgentShroudSourceCodeProtection

## Connections
- [[.test_any_python_file_in_gateway_blocked()]] - `method` [EXTRACTED]
- [[.test_gateway_source_write_blocked()]] - `method` [EXTRACTED]
- [[.test_modules_source_write_blocked()]] - `method` [EXTRACTED]
- [[.test_security_module_write_blocked()]] - `method` [EXTRACTED]
- [[Agent cannot modify AgentShroud's own source code.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Privilege_Separation__File_Sandbox