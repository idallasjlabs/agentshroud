---
type: community
cohesion: 0.06
members: 41
---

# Module Group 111

**Cohesion:** 0.06 - loosely connected
**Members:** 41 nodes

## Members
- [[.test_add_message()]] - code - gateway/tests/test_session_manager.py
- [[.test_conversation_history_limit()]] - code - gateway/tests/test_session_manager.py
- [[.test_default_trust_level_is_untrusted()]] - code - gateway/tests/test_session_manager.py
- [[.test_empty_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_or_create_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_session_context_contains_user_id()]] - code - gateway/tests/test_session_manager.py
- [[.test_long_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_memory_file_created()]] - code - gateway/tests/test_session_manager.py
- [[.test_non_owner_cannot_view_other_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_non_owner_empty_when_no_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_access_any_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_owner_can_view_all_sessions()]] - code - gateway/tests/test_session_manager.py
- [[.test_path_traversal_rejected()_1]] - code - gateway/tests/test_session_manager.py
- [[.test_prompt_addition_mentions_isolation()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_contains_security_notice()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_prepends_preamble()]] - code - gateway/tests/test_session_manager.py
- [[.test_reanchor_preserves_original_content()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_to_dict_and_back()]] - code - gateway/tests/test_session_manager.py
- [[.test_sessions_are_isolated()]] - code - gateway/tests/test_session_manager.py
- [[.test_special_chars_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_update_trust_level()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_can_access_own_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_cannot_access_other_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_directory_created()]] - code - gateway/tests/test_session_manager.py
- [[Create a UserSessionManager with a temp base workspace and an owner.]] - rationale - gateway/tests/test_session_manager.py
- [[History should be capped at 1000 messages.]] - rationale - gateway/tests/test_session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[Represents an isolated session for a user within a specific bot workspace.]] - rationale - gateway/security/session_manager.py
- [[TestAccessControl_2]] - code - gateway/tests/test_session_manager.py
- [[TestConversationHistory]] - code - gateway/tests/test_session_manager.py
- [[TestInputValidation]] - code - gateway/tests/test_session_manager.py
- [[TestSerialization_1]] - code - gateway/tests/test_session_manager.py
- [[TestSessionContext]] - code - gateway/tests/test_session_manager.py
- [[TestSessionIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py
- [[TestTrustLevel]] - code - gateway/tests/test_session_manager.py
- [[UserSession]] - code - gateway/security/session_manager.py
- [[mgr()_2]] - code - gateway/tests/test_session_manager.py
- [[test_session_manager.py]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_111
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Webhook Receiver]]
- 13 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 2 edges to [[_COMMUNITY_Module Group 259]]
- 1 edge to [[_COMMUNITY_Module Group 189]]

## Top bridge nodes
- [[UserSession]] - degree 21, connects to 4 communities
- [[test_session_manager.py]] - degree 13, connects to 3 communities
- [[TestAccessControl_2]] - degree 10, connects to 2 communities
- [[TestSessionIsolation]] - degree 9, connects to 2 communities
- [[TestInputValidation]] - degree 8, connects to 2 communities