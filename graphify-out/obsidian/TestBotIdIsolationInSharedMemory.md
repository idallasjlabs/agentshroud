---
source_file: "gateway/tests/test_security_regressions_v1_2.py"
type: "code"
community: "Security Regressions V1 2"
location: "L65"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Regressions_V1_2
---

# TestBotIdIsolationInSharedMemory

## Connections
- [[.test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - `method` [EXTRACTED]
- [[.test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - `method` [EXTRACTED]
- [[.test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - `method` [EXTRACTED]
- [[.test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - `method` [EXTRACTED]
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_security_regressions_v1_2.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Regressions_V1_2