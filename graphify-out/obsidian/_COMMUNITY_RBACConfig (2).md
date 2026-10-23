---
type: community
cohesion: 0.03
members: 73
---

# RBACConfig (2)

**Cohesion:** 0.03 - loosely connected
**Members:** 73 nodes

## Members
- [[dot-test_add_message()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_atomic_save_never_leaves_partial_registry_on_crash()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_concurrent_saves_do_not_lose_entries()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_conversation_histories_are_bot_scoped()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_conversation_history_limit()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_default_bot_id_is_openclaw()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_default_trust_level_is_untrusted()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_different_bots_get_different_memory_files()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_different_bots_get_different_workspace_dirs()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_empty_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_get_or_create_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_get_session_context_contains_user_id()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_invalid_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_lazy_migration_copies_legacy_memory()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_legacy_session_promoted_on_load()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_load_tolerates_corrupt_registry()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_load_tolerates_empty_registry()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_long_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_long_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_memory_file_created()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_no_temp_files_left_behind()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_non_owner_cannot_view_other_sessions()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_non_owner_empty_when_no_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_owner_can_access_any_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_owner_can_view_all_sessions()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_path_traversal_rejected()_1]] - code - gateway/tests/test_session_manager.py
- [[dot-test_prompt_addition_mentions_isolation()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_contains_security_notice()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_prepends_preamble()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_reanchor_preserves_original_content()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_same_bot_same_user_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_save_uses_atomic_replace()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_session_bot_id_stored_correctly()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_session_context_includes_bot_id()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_session_registry_uses_compound_key()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_session_to_dict_and_back()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_sessions_are_isolated()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_special_chars_rejected()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_update_trust_level()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_user_can_access_own_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_user_cannot_access_other_session()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_workspace_directory_created()]] - code - gateway/tests/test_session_manager.py
- [[dot-test_workspace_paths_under_bot_namespace()]] - code - gateway/tests/test_session_manager.py
- [[A corruptpartial registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[A successful save leaves only the final registry file, no .tmp.]] - rationale - gateway/tests/test_session_manager.py
- [[An empty registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[Concurrent add_conversation_message calls (each of which saves) must         not]] - rationale - gateway/tests/test_session_manager.py
- [[Create a UserSessionManager with a temp base workspace and an owner.]] - rationale - gateway/tests/test_session_manager.py
- [[Existing plain user_id keys (no separator) are promoted to useropenclaw.]] - rationale - gateway/tests/test_session_manager.py
- [[History should be capped at 1000 messages.]] - rationale - gateway/tests/test_session_manager.py
- [[If legacy users{uid}MEMORY.md exists, first openclaw session copies it.]] - rationale - gateway/tests/test_session_manager.py
- [[If the write to the temp file fails mid-flight, the existing         registry on]] - rationale - gateway/tests/test_session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[Registry writes must be atomic (os.replace) and serialized (lock).      The sess]] - rationale - gateway/tests/test_session_manager.py
- [[Represents an isolated session for a user within a specific bot workspace.]] - rationale - gateway/security/session_manager.py
- [[TestAccessControl_1]] - code - gateway/tests/test_session_manager.py
- [[TestAtomicRegistryWrites]] - code - gateway/tests/test_session_manager.py
- [[TestConversationHistory]] - code - gateway/tests/test_session_manager.py
- [[TestInputValidation]] - code - gateway/tests/test_session_manager.py
- [[TestMultiBotIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSerialization_1]] - code - gateway/tests/test_session_manager.py
- [[TestSessionContext]] - code - gateway/tests/test_session_manager.py
- [[TestSessionIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py
- [[TestTrustLevel]] - code - gateway/tests/test_session_manager.py
- [[UserSession]] - code - gateway/security/session_manager.py
- [[Verify that different bots get independent workspaces per user.]] - rationale - gateway/tests/test_session_manager.py
- [[_save_sessions must go through os.replace(tmp, final), never a         partial i]] - rationale - gateway/tests/test_session_manager.py
- [[mgr()_1]] - code - gateway/tests/test_session_manager.py
- [[openclaw and hermes sessions for the same user must not share a directory.]] - rationale - gateway/tests/test_session_manager.py
- [[test_session_manager.py]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig_2
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager]]

## Top bridge nodes
- [[test_session_manager.py]] - degree 14, connects to 2 communities
- [[UserSession]] - degree 17, connects to 1 community
- [[TestMultiBotIsolation]] - degree 17, connects to 1 community
- [[TestAtomicRegistryWrites]] - degree 10, connects to 1 community
- [[TestAccessControl_1]] - degree 9, connects to 1 community
