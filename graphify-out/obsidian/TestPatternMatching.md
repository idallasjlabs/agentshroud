---
source_file: "gateway/tests/test_privilege_separation.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L237"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# TestPatternMatching

## Connections
- [[.test_symlink_resolution()]] - `method` [EXTRACTED]
- [[.test_wildcard_pattern_matching()]] - `method` [EXTRACTED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[Test file path pattern matching logic.]] - `rationale_for` [EXTRACTED]
- [[test_privilege_separation.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection