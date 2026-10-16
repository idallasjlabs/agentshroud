---
type: community
cohesion: 0.03
members: 90
---

# UserSessionManager

**Cohesion:** 0.03 - loosely connected
**Members:** 90 nodes

## Members
- [[dot-__init__()_156]] - code - gateway/security/session_manager.py
- [[dot-_load_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_save_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_session_key()]] - code - gateway/security/session_manager.py
- [[dot-_validate_bot_id()]] - code - gateway/security/session_manager.py
- [[dot-_validate_user_id()]] - code - gateway/security/session_manager.py
- [[dot-add_conversation_message()]] - code - gateway/security/session_manager.py
- [[dot-can_user_access_group()]] - code - gateway/security/session_manager.py
- [[dot-can_user_access_session()]] - code - gateway/security/session_manager.py
- [[dot-cleanup_old_sessions()_1]] - code - gateway/security/session_manager.py
- [[dot-from_dict()_6]] - code - gateway/security/session_manager.py
- [[dot-get_merged_context()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_session()]] - code - gateway/security/session_manager.py
- [[dot-get_session_context()]] - code - gateway/security/session_manager.py
- [[dot-get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[dot-get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[dot-list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[dot-reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[dot-session_manager()]] - code - gateway/tests/test_session_isolation.py
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_absolute_and_relative_paths()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_critical_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_delete_action()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_direct_field()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_editor_command_and_quotes()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_exception_fails_open()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_execute_action_medium_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_filter_applied()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_filter_not_applied()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_high_tool_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_metadata_fallback()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_missing_returns_none()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_filter_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_paths()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_question_defaults_to_read_system()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_read_action_low_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_session_context_priority()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_unknown_defaults_to_tool_use()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_write_action_no_tier()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-to_dict()_10]] - code - gateway/security/session_manager.py
- [[dot-update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_57]] - code - gateway/security/session_manager.py
- [[Atomically persist current sessions to the metadata file.          Writes are se]] - rationale - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[Clean up sessions that haven't been active for the specified number of days.]] - rationale - gateway/security/session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a session manager with temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[Initialize session manager.          Args             base_workspace Base dire]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see.          Returns t]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file.          Handles both the new ``{use]] - rationale - gateway/security/session_manager.py
- [[Manages per-user, per-bot session isolation.      Sessions are keyed by (user_id]] - rationale - gateway/security/session_manager.py
- [[MiddlewareManager with real session_manager, all other deps mocked.      Uses __]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[Path_42]] - code - gateway/security/session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return True if user_id is a member of group_id.          Checks rbac_config.get_]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[Return user MEMORY.md + all accessible group MEMORY.md contents for prompt injec]] - rationale - gateway/security/session_manager.py
- [[Test File Sandbox Message Gate Suite]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestAnalyzeRequestForRBAC]] - code - gateway/tests/test_middleware_coverage.py
- [[TestExtractFilePaths]] - code - gateway/tests/test_middleware_coverage.py
- [[TestExtractUserId]] - code - gateway/tests/test_middleware_coverage.py
- [[TestFilterOutboundResponse]] - code - gateway/tests/test_middleware_coverage.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal.          Allows alphanum]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal.          Only allows al]] - rationale - gateway/security/session_manager.py
- [[manager()_2]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[session_manager()_2]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[temp_workspace()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[test_file_sandbox_message_gate.py]] - code - gateway/tests/test_file_sandbox_message_gate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserSessionManager
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_MiddlewareManager]]
- 20 edges to [[_COMMUNITY__req]]
- 17 edges to [[_COMMUNITY_UserSessionManager_1]]
- 11 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 10 edges to [[_COMMUNITY_RBACConfig]]
- 9 edges to [[_COMMUNITY_UserSessionManager]]
- 7 edges to [[_COMMUNITY_DataLedger]]
- 5 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig_8]]
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 3 edges to [[_COMMUNITY_UserSessionManager_2]]
- 3 edges to [[_COMMUNITY_test_hermes_model_resolver.py_1]]
- 2 edges to [[_COMMUNITY_AsyncMock_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager_8]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_diagramsREADME_1]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py_4]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_9]]
- 1 edge to [[_COMMUNITY_AWS Cloud Management & FinOps]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_Path_3]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_2]]

## Top bridge nodes
- [[UserSessionManager]] - degree 137, connects to 25 communities
- [[TestAnalyzeRequestForRBAC]] - degree 13, connects to 3 communities
- [[TestExtractUserId]] - degree 9, connects to 3 communities
- [[TestFilterOutboundResponse]] - degree 9, connects to 3 communities
- [[TestExtractFilePaths]] - degree 8, connects to 3 communities
