---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Security Module Middleware"
location: "L643"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Module_Middleware
---

# No yaml.load() without Loader (arbitrary code execution).

## Connections
- [[.test_no_yaml_unsafe_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Module_Middleware