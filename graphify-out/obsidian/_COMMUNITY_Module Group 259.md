---
type: community
cohesion: 0.11
members: 18
---

# Module Group 259

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.test_conversation_histories_are_bot_scoped()]] - code - gateway/tests/test_session_manager.py
- [[.test_default_bot_id_is_openclaw()]] - code - gateway/tests/test_session_manager.py
- [[.test_different_bots_get_different_memory_files()]] - code - gateway/tests/test_session_manager.py
- [[.test_different_bots_get_different_workspace_dirs()]] - code - gateway/tests/test_session_manager.py
- [[.test_invalid_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_lazy_migration_copies_legacy_memory()]] - code - gateway/tests/test_session_manager.py
- [[.test_legacy_session_promoted_on_load()]] - code - gateway/tests/test_session_manager.py
- [[.test_long_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_same_bot_same_user_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_bot_id_stored_correctly()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_context_includes_bot_id()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_registry_uses_compound_key()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_paths_under_bot_namespace()]] - code - gateway/tests/test_session_manager.py
- [[Existing plain user_id keys (no separator) are promoted to useropenclaw.]] - rationale - gateway/tests/test_session_manager.py
- [[If legacy users{uid}MEMORY.md exists, first openclaw session copies it.]] - rationale - gateway/tests/test_session_manager.py
- [[TestMultiBotIsolation]] - code - gateway/tests/test_session_manager.py
- [[Verify that different bots get independent workspaces per user.]] - rationale - gateway/tests/test_session_manager.py
- [[openclaw and hermes sessions for the same user must not share a directory.]] - rationale - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_259
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 2 edges to [[_COMMUNITY_Module Group 111]]
- 1 edge to [[_COMMUNITY_Webhook Receiver]]

## Top bridge nodes
- [[TestMultiBotIsolation]] - degree 18, connects to 3 communities
- [[.test_lazy_migration_copies_legacy_memory()]] - degree 3, connects to 1 community
- [[.test_legacy_session_promoted_on_load()]] - degree 3, connects to 1 community
