---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Environment Guard & Leak Detection"
location: "L197"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Environment_Guard__Leak_Detection
---

# Agent can write to /tmp for temporary files.

## Connections
- [[.test_tmp_write_allowed()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Environment_Guard__Leak_Detection
