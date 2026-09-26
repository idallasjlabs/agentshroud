---
source_file: "gateway/tests/test_privilege_separation.py"
type: "rationale"
community: "Enum"
location: "L170"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enum
---

# Agent cannot write to /usr/bin/ system binaries.

## Connections
- [[.test_usr_bin_write_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enum