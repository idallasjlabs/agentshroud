---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "File Sandbox & Privilege Separation Tests"
location: "L160"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/File_Sandbox__Privilege_Separation_Tests
---

# TestSystemPathProtection

## Connections
- [[dot-test_etc_write_blocked()]] - `method` [EXTRACTED]
- [[dot-test_usr_bin_write_blocked()]] - `method` [EXTRACTED]
- [[dot-test_var_log_write_blocked()]] - `method` [EXTRACTED]
- [[Agent cannot modify system paths.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/File_Sandbox__Privilege_Separation_Tests