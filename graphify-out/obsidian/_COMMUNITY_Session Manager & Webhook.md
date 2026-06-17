---
type: community
cohesion: 0.04
members: 67
---

# Session Manager & Webhook

**Cohesion:** 0.04 - loosely connected
**Members:** 67 nodes

## Members
- [[.__init__()_91]] - code - gateway/security/session_manager.py
- [[._load_sessions()]] - code - gateway/security/session_manager.py
- [[._save_sessions()]] - code - gateway/security/session_manager.py
- [[._session_key()]] - code - gateway/security/session_manager.py
- [[._validate_bot_id()]] - code - gateway/security/session_manager.py
- [[.add_conversation_message()]] - code - gateway/security/session_manager.py
- [[.can_user_access_group()]] - code - gateway/security/session_manager.py
- [[.can_user_access_session()]] - code - gateway/security/session_manager.py
- [[.cleanup_old_sessions()_1]] - code - gateway/security/session_manager.py
- [[.from_dict()_9]] - code - gateway/security/session_manager.py
- [[.get_or_create_session()]] - code - gateway/security/session_manager.py
- [[.get_session_context()]] - code - gateway/security/session_manager.py
- [[.get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[.get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[.list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[.middleware_manager()]] - code - gateway/tests/test_session_isolation.py
- [[.reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[.session_manager()]] - code - gateway/tests/test_session_isolation.py
- [[.session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[.test_absolute_and_relative_paths()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[.test_editor_command_and_quotes()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_exception_fails_open()_1]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_filter_applied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_filter_not_applied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_filter_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_paths()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[.test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[.to_dict()_11]] - code - gateway/security/session_manager.py
- [[.update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_52]] - code - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[Clean up sessions that haven't been active for the specified number of days.]] - rationale - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a session manager with temporary workspace.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create middleware manager with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Initialize session manager.          Args             base_workspace Base dire]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see.          Returns t]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file.          Handles both the new ``{use]] - rationale - gateway/security/session_manager.py
- [[Manages per-user, per-bot session isolation.      Sessions are keyed by (user_id]] - rationale - gateway/security/session_manager.py
- [[MiddlewareManager with real session_manager, all other deps mocked.      Uses __]] - rationale - gateway/tests/test_file_sandbox_message_gate.py
- [[Path_16]] - code - gateway/security/session_manager.py
- [[Return True if user_id is a member of group_id.          Checks rbac_config.get_]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[Save current sessions to metadata file.]] - rationale - gateway/security/session_manager.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestExtractFilePaths]] - code - gateway/tests/test_middleware_coverage.py
- [[TestFilterOutboundResponse]] - code - gateway/tests/test_middleware_coverage.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal.          Allows alphanum]] - rationale - gateway/security/session_manager.py
- [[manager()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[session_manager()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[temp_workspace()]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[test_file_sandbox_message_gate.py]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Session_Manager__Webhook
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 16 edges to [[_COMMUNITY_Webhook Receiver]]
- 16 edges to [[_COMMUNITY_Middleware Coverage Tests]]
- 13 edges to [[_COMMUNITY_Module Group 111]]
- 9 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 9 edges to [[_COMMUNITY_Module Group 75]]
- 9 edges to [[_COMMUNITY_Module Group 209]]
- 8 edges to [[_COMMUNITY_Module Group 189]]
- 7 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_Module Group 214]]
- 3 edges to [[_COMMUNITY_Module Group 292]]
- 3 edges to [[_COMMUNITY_Module Group 259]]
- 2 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 2 edges to [[_COMMUNITY_Module Group 196]]
- 2 edges to [[_COMMUNITY_Module Group 74]]
- 1 edge to [[_COMMUNITY_Module Group 195]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Module Group 443]]
- 1 edge to [[_COMMUNITY_Module Group 469]]

## Top bridge nodes
- [[UserSessionManager]] - degree 120, connects to 16 communities
- [[TestFilterOutboundResponse]] - degree 9, connects to 3 communities
- [[TestExtractFilePaths]] - degree 8, connects to 3 communities
- [[webhook_receiver.py]] - degree 4, connects to 3 communities
- [[.get_or_create_session()]] - degree 14, connects to 2 communities