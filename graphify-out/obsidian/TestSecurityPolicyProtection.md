---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L99"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestSecurityPolicyProtection

## Connections
- [[.test_config_yaml_write_blocked()]] - `method` [EXTRACTED]
- [[.test_soul_md_in_workspace_blocked()]] - `method` [EXTRACTED]
- [[.test_soul_md_write_blocked()]] - `method` [EXTRACTED]
- [[.test_system_prompt_write_blocked()]] - `method` [EXTRACTED]
- [[Agent cannot modify security policies and behavioral instructions.]] - `rationale_for` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection
