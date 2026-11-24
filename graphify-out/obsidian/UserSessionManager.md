---
source_file: "gateway/security/session_manager.py"
type: "code"
community: "UserSessionManager"
location: "L121"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/UserSessionManager
---

# UserSessionManager

## Connections
- [[dot-__init__()]] - `calls` [EXTRACTED]
- [[dot-__init__()_184]] - `calls` [EXTRACTED]
- [[dot-__init__()_185]] - `method` [EXTRACTED]
- [[dot-_load_sessions()]] - `method` [EXTRACTED]
- [[dot-_save_sessions()]] - `method` [EXTRACTED]
- [[dot-_session_key()]] - `method` [EXTRACTED]
- [[dot-_validate_bot_id()]] - `method` [EXTRACTED]
- [[dot-_validate_user_id()]] - `method` [EXTRACTED]
- [[dot-add_conversation_message()]] - `method` [EXTRACTED]
- [[dot-can_user_access_session()]] - `method` [EXTRACTED]
- [[dot-get_or_create_group_session()]] - `method` [EXTRACTED]
- [[dot-get_or_create_session()]] - `method` [EXTRACTED]
- [[dot-get_session_context()]] - `method` [EXTRACTED]
- [[dot-get_session_prompt_addition()]] - `method` [EXTRACTED]
- [[dot-get_user_workspace_path()]] - `method` [EXTRACTED]
- [[dot-list_sessions_for_user()]] - `method` [EXTRACTED]
- [[dot-middleware_manager()]] - `calls` [EXTRACTED]
- [[dot-reanchor_system_prompt()]] - `method` [EXTRACTED]
- [[dot-session_manager()]] - `calls` [EXTRACTED]
- [[dot-session_manager()_1]] - `calls` [EXTRACTED]
- [[dot-test_complete_user_isolation()]] - `calls` [EXTRACTED]
- [[dot-test_lazy_migration_copies_legacy_memory()]] - `calls` [EXTRACTED]
- [[dot-test_legacy_session_promoted_on_load()]] - `calls` [EXTRACTED]
- [[dot-test_load_tolerates_corrupt_registry()]] - `calls` [EXTRACTED]
- [[dot-test_load_tolerates_empty_registry()]] - `calls` [EXTRACTED]
- [[dot-test_owner_admin_access()]] - `calls` [EXTRACTED]
- [[dot-test_session_persistence()]] - `calls` [EXTRACTED]
- [[dot-update_user_trust_level()]] - `method` [EXTRACTED]
- [[AppState]] - `uses` [INFERRED]
- [[Manages per-user, per-bot session isolation. Sessions are keyed by (user_id,…]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[TestAtomicRegistryWrites]] - `uses` [INFERRED]
- [[TestMiddlewareSessionEnforcement]] - `uses` [INFERRED]
- [[TestMultiBotIsolation]] - `uses` [INFERRED]
- [[TestSessionIsolationEndToEnd]] - `uses` [INFERRED]
- [[TestUserSessionManager]] - `uses` [INFERRED]
- [[TestWebhookReceiverIntegration]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[mgr()_2]] - `uses` [INFERRED]
- [[middleware.py_2]] - `imports` [EXTRACTED]
- [[run()]] - `calls` [EXTRACTED]
- [[session_manager()_3]] - `uses` [INFERRED]
- [[session_manager()_4]] - `uses` [INFERRED]
- [[session_manager()]] - `uses` [INFERRED]
- [[session_manager()_1]] - `uses` [INFERRED]
- [[session_manager()_2]] - `uses` [INFERRED]
- [[session_manager.py]] - `contains` [EXTRACTED]
- [[session_mgr()]] - `uses` [INFERRED]
- [[shared_memory.py]] - `imports` [EXTRACTED]
- [[state.py]] - `imports` [EXTRACTED]
- [[test_file_sandbox_message_gate.py]] - `imports` [EXTRACTED]
- [[test_group_isolation.py]] - `imports` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]
- [[test_middleware_coverage.py]] - `imports` [EXTRACTED]
- [[test_security_regressions_v1_2.py]] - `imports` [EXTRACTED]
- [[test_session_isolation.py]] - `imports` [EXTRACTED]
- [[test_session_manager.py]] - `imports` [EXTRACTED]
- [[test_shared_memory.py]] - `imports` [EXTRACTED]
- [[test_shared_memory_write_acl.py]] - `imports` [EXTRACTED]
- [[usm()]] - `uses` [INFERRED]
- [[webhook_receiver.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/UserSessionManager
