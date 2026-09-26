---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Enum"
location: "L164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enum
---

# Agent cannot write to /etc/ system configuration.

## Connections
- [[.test_etc_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enum