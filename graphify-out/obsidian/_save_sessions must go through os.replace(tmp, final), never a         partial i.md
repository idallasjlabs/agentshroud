---
source_file: "gateway/tests/test_session_manager.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L321"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# _save_sessions must go through os.replace(tmp, final), never a         partial i

## Connections
- [[.test_save_uses_atomic_replace()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite