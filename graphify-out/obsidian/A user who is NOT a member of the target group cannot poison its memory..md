---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L95"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# A user who is NOT a member of the target group cannot poison its memory.

## Connections
- [[.test_non_member_write_is_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite