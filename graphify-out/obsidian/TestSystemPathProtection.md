---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Community 14"
location: "L160"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_14
---

# TestSystemPathProtection

## Connections
- [[.test_etc_write_blocked()]] - `method` [EXTRACTED]
- [[.test_usr_bin_write_blocked()]] - `method` [EXTRACTED]
- [[.test_var_log_write_blocked()]] - `method` [EXTRACTED]
- [[Agent cannot modify system paths.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_14