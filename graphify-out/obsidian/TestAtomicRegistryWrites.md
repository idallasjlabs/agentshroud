---
source_file: "gateway/tests/test_session_manager.py"
type: "code"
community: "Community 174"
location: "L312"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_174
---

# TestAtomicRegistryWrites

## Connections
- [[.test_atomic_save_never_leaves_partial_registry_on_crash()]] - `method` [EXTRACTED]
- [[.test_concurrent_saves_do_not_lose_entries()]] - `method` [EXTRACTED]
- [[.test_load_tolerates_corrupt_registry()]] - `method` [EXTRACTED]
- [[.test_load_tolerates_empty_registry()]] - `method` [EXTRACTED]
- [[.test_no_temp_files_left_behind()]] - `method` [EXTRACTED]
- [[.test_save_uses_atomic_replace()]] - `method` [EXTRACTED]
- [[Registry writes must be atomic (os.replace) and serialized (lock).      The sess]] - `rationale_for` [EXTRACTED]
- [[UserSession]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_session_manager.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_174