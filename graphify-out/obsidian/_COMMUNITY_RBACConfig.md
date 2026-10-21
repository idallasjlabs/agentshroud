---
type: community
members: 75
---

# RBACConfig

**Members:** 75 nodes

## Members
- [[dot-__init__()_170]] - code - gateway/security/session_manager.py
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
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[dot-session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_complete_user_isolation()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_owner_admin_access()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_session_persistence()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[dot-to_dict()_11]] - code - gateway/security/session_manager.py
- [[dot-update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_69]] - code - gateway/security/session_manager.py
- [[Atomically persist current sessions to the metadata file.          Writes are se]] - rationale - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[Clean up sessions that haven't been active for the specified number of days.]] - rationale - gateway/security/session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[End-to-end integration tests for session isolation.]] - rationale - gateway/tests/test_session_isolation.py
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
- [[Path_54]] - code - gateway/security/session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return True if user_id is a member of group_id.          Checks rbac_config.get_]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[Return user MEMORY.md + all accessible group MEMORY.md contents for prompt injec]] - rationale - gateway/security/session_manager.py
- [[Test File Sandbox Message Gate Suite]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test complete isolation between two users.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that owneradmin can access all user sessions.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that sessions persist across manager restarts.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestSessionIsolationEndToEnd]] - code - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal.          Allows alphanum]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal.          Only allows al]] - rationale - gateway/security/session_manager.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[test_session_isolation.py]] - code - gateway/tests/test_session_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RBACConfig
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_MiddlewareManager]]
- 17 edges to [[_COMMUNITY_RBACConfig (2)]]
- 13 edges to [[_COMMUNITY_TestProductionCompose]]
- 11 edges to [[_COMMUNITY_export_bot]]
- 11 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 8 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_TestToolChainAnalyzer (2)]]
- 5 edges to [[_COMMUNITY_TELEGRAM_ISSUES]]
- 5 edges to [[_COMMUNITY_TestToolChainAnalyzer (3)]]
- 4 edges to [[_COMMUNITY_KillSwitchMonitor (5)]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (3)]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (4)]]
- 3 edges to [[_COMMUNITY_api.py (2)]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_RBACConfig (3)]]
- 2 edges to [[_COMMUNITY__make_proxy()]]
- 2 edges to [[_COMMUNITY_Remediation]]
- 1 edge to [[_COMMUNITY_AgentShroud v1.2.0 — Red Team Assessment]]
- 1 edge to [[_COMMUNITY_CICD Quality Gates (14 jobs, 6 workflows)]]
- 1 edge to [[_COMMUNITY_api.py (2) (2)]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]
- 1 edge to [[_COMMUNITY_Local LLM Support — Implementation Review]]

## Top bridge nodes
- [[UserSessionManager]] - degree 132, connects to 22 communities
- [[test_session_isolation.py]] - degree 8, connects to 5 communities
- [[TestWebhookReceiverIntegration]] - degree 13, connects to 4 communities
- [[TestSessionIsolationEndToEnd]] - degree 10, connects to 4 communities
- [[dot-from_dict()_6]] - degree 7, connects to 2 communities
