---
type: community
members: 77
---

# Community 60

**Members:** 77 nodes

## Members
- [[.__init__()_130]] - code - gateway/security/session_manager.py
- [[._load_sessions()]] - code - gateway/security/session_manager.py
- [[.add_conversation_message()]] - code - gateway/security/session_manager.py
- [[.from_dict()_11]] - code - gateway/security/session_manager.py
- [[.get_session_context()]] - code - gateway/security/session_manager.py
- [[.reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[.test_add_message()]] - code - gateway/tests/test_session_manager.py
- [[.test_atomic_save_never_leaves_partial_registry_on_crash()]] - code - gateway/tests/test_session_manager.py
- [[.test_concurrent_saves_do_not_lose_entries()]] - code - gateway/tests/test_session_manager.py
- [[.test_conversation_history_limit()]] - code - gateway/tests/test_session_manager.py
- [[.test_default_trust_level_is_untrusted()]] - code - gateway/tests/test_session_manager.py
- [[.test_empty_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_or_create_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_session_context_contains_user_id()]] - code - gateway/tests/test_session_manager.py
- [[.test_load_tolerates_corrupt_registry()]] - code - gateway/tests/test_session_manager.py
- [[.test_load_tolerates_empty_registry()]] - code - gateway/tests/test_session_manager.py
- [[.test_long_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_memory_file_created()]] - code - gateway/tests/test_session_manager.py
- [[.test_no_temp_files_left_behind()]] - code - gateway/tests/test_session_manager.py
- [[.test_non_owner_cannot_view_other_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_non_owner_empty_when_no_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_access_any_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_view_all_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_path_traversal_rejected()_1]] - code - gateway/tests/test_session_manager.py
- [[.test_prompt_addition_mentions_isolation()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_contains_security_notice()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_prepends_preamble()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_preserves_original_content()]] - code - gateway/tests/test_session_manager.py
- [[.test_save_uses_atomic_replace()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_to_dict_and_back()]] - code - gateway/tests/test_session_manager.py
- [[.test_sessions_are_isolated()]] - code - gateway/tests/test_session_manager.py
- [[.test_special_chars_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_update_trust_level()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_can_access_own_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_cannot_access_other_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_directory_created()]] - code - gateway/tests/test_session_manager.py
- [[.to_dict()_12]] - code - gateway/security/session_manager.py
- [[A corruptpartial registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[A successful save leaves only the final registry file, no .tmp.]] - rationale - gateway/tests/test_session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[An empty registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[Any_69]] - code - gateway/security/session_manager.py
- [[Concurrent add_conversation_message calls (each of which saves) must         not]] - rationale - gateway/tests/test_session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a UserSessionManager with a temp base workspace and an owner.]] - rationale - gateway/tests/test_session_manager.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[History should be capped at 1000 messages.]] - rationale - gateway/tests/test_session_manager.py
- [[If the write to the temp file fails mid-flight, the existing         registry on]] - rationale - gateway/tests/test_session_manager.py
- [[Initialize session manager.          Args             base_workspace Base dire]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file.          Handles both the new ``{use]] - rationale - gateway/security/session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Path_20]] - code - gateway/security/session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[Registry writes must be atomic (os.replace) and serialized (lock).      The sess]] - rationale - gateway/tests/test_session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Represents an isolated session for a user within a specific bot workspace.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[TestAccessControl_2]] - code - gateway/tests/test_session_manager.py
- [[TestAtomicRegistryWrites]] - code - gateway/tests/test_session_manager.py
- [[TestConversationHistory]] - code - gateway/tests/test_session_manager.py
- [[TestInputValidation]] - code - gateway/tests/test_session_manager.py
- [[TestSerialization_1]] - code - gateway/tests/test_session_manager.py
- [[TestSessionContext]] - code - gateway/tests/test_session_manager.py
- [[TestSessionIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py
- [[TestTrustLevel]] - code - gateway/tests/test_session_manager.py
- [[UserSession]] - code - gateway/security/session_manager.py
- [[_save_sessions must go through os.replace(tmp, final), never a         partial i]] - rationale - gateway/tests/test_session_manager.py
- [[mgr()_2]] - code - gateway/tests/test_session_manager.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[session_manager.py (UserSessionManager)]] - code - gateway/security/session_manager.py
- [[test_session_manager.py]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_60
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_Community 1305]]
- 2 edges to [[_COMMUNITY_Community 1015]]
- 1 edge to [[_COMMUNITY_Community 489]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 809]]

## Top bridge nodes
- [[session_manager.py (UserSessionManager)]] - degree 5, connects to 3 communities
- [[UserSession]] - degree 17, connects to 2 communities
- [[test_session_manager.py]] - degree 14, connects to 2 communities
- [[session_manager.py]] - degree 5, connects to 2 communities
- [[TestAtomicRegistryWrites]] - degree 10, connects to 1 community