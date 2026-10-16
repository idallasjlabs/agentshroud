---
source_file: "gateway/tests/test_shared_memory_write_acl.py"
type: "rationale"
community: "Audit Ledger (SHA-256 hash only)"
location: "L95"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Audit_Ledger_SHA-256_hash_only
---

# A user who is NOT a member of the target group cannot poison its memory.

## Connections
- [[dot-test_non_member_write_is_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Audit_Ledger_SHA-256_hash_only
