---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L139"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# Agent cannot write to gateway config directory.

## Connections
- [[.test_gateway_config_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection