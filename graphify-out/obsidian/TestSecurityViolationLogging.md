---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L277"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestSecurityViolationLogging

## Connections
- [[.test_multiple_violations_tracked()]] - `method` [EXTRACTED]
- [[.test_normal_operations_not_violations()]] - `method` [EXTRACTED]
- [[.test_violation_recorded_in_audit()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[Test that security violations are properly logged and tracked.]] - `rationale_for` [EXTRACTED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection