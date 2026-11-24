---
type: community
members: 10
---

# TestBotIdIsolationInSharedMemory

**Members:** 10 nodes

## Members
- [[dot-test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H1 SharedMemoryManager.get_user_memory must accept a bot_id parameter. The…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H3 The filesystem paths for openclaw and hermes sessions differ.…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 (reverse) Writing to Hermes workspace does not bleed into OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 Writing to the openclaw workspace must not leak into the hermes…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestBotIdIsolationInSharedMemory]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestBotIdIsolationInSharedMemory
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]

## Top bridge nodes
- [[TestBotIdIsolationInSharedMemory]] - degree 6, connects to 1 community
