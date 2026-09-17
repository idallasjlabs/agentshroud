---
source_file: "gateway/tests/test_session_manager.py"
type: "rationale"
community: "TestAtomicRegistryWrites"
location: "L399"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestAtomicRegistryWrites
---

# Concurrent add_conversation_message calls (each of which saves) must         not

## Connections
- [[.test_concurrent_saves_do_not_lose_entries()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestAtomicRegistryWrites