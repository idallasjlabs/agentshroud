---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L649"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# No yaml.load() without Loader (arbitrary code execution).

## Connections
- [[.test_no_yaml_unsafe_load()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection
