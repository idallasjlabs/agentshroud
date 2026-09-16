---
source_file: "gateway/tests/test_ledger.py"
type: "rationale"
community: "Gateway Config & PII Sanitizer"
location: "L217"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Config__PII_Sanitizer
---

# Re-initializing must not orphan the first aiosqlite connection.      aiosqlite c

## Connections
- [[test_initialize_is_idempotent()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Config__PII_Sanitizer