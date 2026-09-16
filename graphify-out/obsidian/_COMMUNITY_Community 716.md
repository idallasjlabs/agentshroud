---
type: community
cohesion: 0.14
members: 14
---

# Community 716

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-test_atomic_save_never_leaves_partial_registry_on_crash()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_concurrent_saves_do_not_lose_entries()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_load_tolerates_corrupt_registry()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_load_tolerates_empty_registry()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_no_temp_files_left_behind()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_save_uses_atomic_replace()]] - code - gateway/tests/test_session_manager.py
- [[A corruptpartial registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[A successful save leaves only the final registry file, no .tmp.]] - rationale - gateway/tests/test_session_manager.py
- [[An empty registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[Concurrent add_conversation_message calls (each of which saves) must         not]] - rationale - gateway/tests/test_session_manager.py
- [[If the write to the temp file fails mid-flight, the existing         registry on]] - rationale - gateway/tests/test_session_manager.py
- [[Registry writes must be atomic (os.replace) and serialized (lock).      The sess]] - rationale - gateway/tests/test_session_manager.py
- [[TestAtomicRegistryWrites]] - code - gateway/tests/test_session_manager.py
- [[_save_sessions must go through os.replace(tmp, final), never a         partial i]] - rationale - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_716
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Ingest Middleware & File Sandbox]]
- 2 edges to [[_COMMUNITY_Community 390]]

## Top bridge nodes
- [[TestAtomicRegistryWrites]] - degree 10, connects to 2 communities
- [[dot-test_load_tolerates_corrupt_registry()]] - degree 3, connects to 1 community
- [[dot-test_load_tolerates_empty_registry()]] - degree 3, connects to 1 community