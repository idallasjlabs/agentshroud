---
source_file: "gateway/tests/test_ledger.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L217"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c

## Connections
- [[test_initialize_is_idempotent()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline