---
type: community
cohesion: 0.02
members: 125
---

# KeyVaultConfig

**Cohesion:** 0.02 - loosely connected
**Members:** 125 nodes

## Members
- [[.__init__()_115]] - code - gateway/security/session_manager.py
- [[._load_sessions()]] - code - gateway/security/session_manager.py
- [[._save_sessions()]] - code - gateway/security/session_manager.py
- [[._session_key()]] - code - gateway/security/session_manager.py
- [[._validate_bot_id()]] - code - gateway/security/session_manager.py
- [[._validate_user_id()]] - code - gateway/security/session_manager.py
- [[.add_conversation_message()]] - code - gateway/security/session_manager.py
- [[.can_user_access_group()]] - code - gateway/security/session_manager.py
- [[.can_user_access_session()]] - code - gateway/security/session_manager.py
- [[.cleanup_old_sessions()_1]] - code - gateway/security/session_manager.py
- [[.from_dict()_11]] - code - gateway/security/session_manager.py
- [[.get_merged_context()]] - code - gateway/security/session_manager.py
- [[.get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[.get_or_create_session()]] - code - gateway/security/session_manager.py
- [[.get_session_context()]] - code - gateway/security/session_manager.py
- [[.get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[.get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[.list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[.reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[.test_add_message()]] - code - gateway/tests/test_session_manager.py
- [[.test_atomic_save_never_leaves_partial_registry_on_crash()]] - code - gateway/tests/test_session_manager.py
- [[.test_concurrent_saves_do_not_lose_entries()]] - code - gateway/tests/test_session_manager.py
- [[.test_conversation_histories_are_bot_scoped()]] - code - gateway/tests/test_session_manager.py
- [[.test_conversation_history_limit()]] - code - gateway/tests/test_session_manager.py
- [[.test_default_bot_id_is_openclaw()]] - code - gateway/tests/test_session_manager.py
- [[.test_default_trust_level_is_untrusted()]] - code - gateway/tests/test_session_manager.py
- [[.test_different_bots_get_different_memory_files()]] - code - gateway/tests/test_session_manager.py
- [[.test_different_bots_get_different_workspace_dirs()]] - code - gateway/tests/test_session_manager.py
- [[.test_empty_user_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_or_create_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_get_session_context_contains_user_id()]] - code - gateway/tests/test_session_manager.py
- [[.test_invalid_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_lazy_migration_copies_legacy_memory()]] - code - gateway/tests/test_session_manager.py
- [[.test_legacy_session_promoted_on_load()]] - code - gateway/tests/test_session_manager.py
- [[.test_load_tolerates_corrupt_registry()]] - code - gateway/tests/test_session_manager.py
- [[.test_load_tolerates_empty_registry()]] - code - gateway/tests/test_session_manager.py
- [[.test_long_bot_id_rejected()]] - code - gateway/tests/test_session_manager.py
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
- [[.test_same_bot_same_user_returns_same_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_save_uses_atomic_replace()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_bot_id_stored_correctly()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_context_includes_bot_id()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_registry_uses_compound_key()]] - code - gateway/tests/test_session_manager.py
- [[.test_session_to_dict_and_back()]] - code - gateway/tests/test_session_manager.py
- [[.test_sessions_are_isolated()]] - code - gateway/tests/test_session_manager.py
- [[.test_special_chars_rejected()]] - code - gateway/tests/test_session_manager.py
- [[.test_update_trust_level()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_can_access_own_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_user_cannot_access_other_session()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_directory_created()]] - code - gateway/tests/test_session_manager.py
- [[.test_workspace_paths_under_bot_namespace()]] - code - gateway/tests/test_session_manager.py
- [[.to_dict()_12]] - code - gateway/security/session_manager.py
- [[.update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A corruptpartial registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[A successful save leaves only the final registry file, no .tmp.]] - rationale - gateway/tests/test_session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[An empty registry file must not crash construction.]] - rationale - gateway/tests/test_session_manager.py
- [[Any_59]] - code - gateway/security/session_manager.py
- [[Atomically persist current sessions to the metadata file.          Writes are se]] - rationale - gateway/security/session_manager.py
- [[Check if a user can access another user's session.]] - rationale - gateway/security/session_manager.py
- [[Clean up sessions that haven't been active for the specified number of days.]] - rationale - gateway/security/session_manager.py
- [[Concurrent add_conversation_message calls (each of which saves) must         not]] - rationale - gateway/tests/test_session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Create a UserSessionManager with a temp base workspace and an owner.]] - rationale - gateway/tests/test_session_manager.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[Existing plain user_id keys (no separator) are promoted to useropenclaw.]] - rationale - gateway/tests/test_session_manager.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[History should be capped at 1000 messages.]] - rationale - gateway/tests/test_session_manager.py
- [[If legacy users{uid}MEMORY.md exists, first openclaw session copies it.]] - rationale - gateway/tests/test_session_manager.py
- [[If the write to the temp file fails mid-flight, the existing         registry on]] - rationale - gateway/tests/test_session_manager.py
- [[Initialize session manager.          Args             base_workspace Base dire]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see.          Returns t]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file.          Handles both the new ``{use]] - rationale - gateway/security/session_manager.py
- [[Manages per-user, per-bot session isolation.      Sessions are keyed by (user_id]] - rationale - gateway/security/session_manager.py
- [[Original system prompt content is always preserved in the output.]] - rationale - gateway/tests/test_session_manager.py
- [[Path_18]] - code - gateway/security/session_manager.py
- [[Preamble contains a security notice keyword.]] - rationale - gateway/tests/test_session_manager.py
- [[Re-anchoring prepends a security notice to the system prompt.]] - rationale - gateway/tests/test_session_manager.py
- [[Registry writes must be atomic (os.replace) and serialized (lock).      The sess]] - rationale - gateway/tests/test_session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Represents an isolated session for a user within a specific bot workspace.]] - rationale - gateway/security/session_manager.py
- [[Return True if user_id is a member of group_id.          Checks rbac_config.get_]] - rationale - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[Return user MEMORY.md + all accessible group MEMORY.md contents for prompt injec]] - rationale - gateway/security/session_manager.py
- [[Test File Sandbox Message Gate Suite]] - code - gateway/tests/test_file_sandbox_message_gate.py
- [[TestAccessControl_2]] - code - gateway/tests/test_session_manager.py
- [[TestAtomicRegistryWrites]] - code - gateway/tests/test_session_manager.py
- [[TestConversationHistory]] - code - gateway/tests/test_session_manager.py
- [[TestInputValidation]] - code - gateway/tests/test_session_manager.py
- [[TestMultiBotIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSerialization_1]] - code - gateway/tests/test_session_manager.py
- [[TestSessionContext]] - code - gateway/tests/test_session_manager.py
- [[TestSessionIsolation]] - code - gateway/tests/test_session_manager.py
- [[TestSystemPromptReanchoring]] - code - gateway/tests/test_session_manager.py
- [[TestTrustLevel]] - code - gateway/tests/test_session_manager.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[UserSession]] - code - gateway/security/session_manager.py
- [[UserSessionManager]] - code - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal.          Allows alphanum]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal.          Only allows al]] - rationale - gateway/security/session_manager.py
- [[Verify that different bots get independent workspaces per user.]] - rationale - gateway/tests/test_session_manager.py
- [[_save_sessions must go through os.replace(tmp, final), never a         partial i]] - rationale - gateway/tests/test_session_manager.py
- [[mgr()_2]] - code - gateway/tests/test_session_manager.py
- [[openclaw and hermes sessions for the same user must not share a directory.]] - rationale - gateway/tests/test_session_manager.py
- [[session_manager.py]] - code - gateway/security/session_manager.py
- [[test_session_manager.py]] - code - gateway/tests/test_session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KeyVaultConfig
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_test_security_audit.py]]
- 16 edges to [[_COMMUNITY_TrustManager]]
- 7 edges to [[_COMMUNITY_GitHub Copilot CLI Setup Guide]]
- 7 edges to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 7 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 7 edges to [[_COMMUNITY_The 8D Investigation Process]]
- 5 edges to [[_COMMUNITY_MCPInspector]]
- 5 edges to [[_COMMUNITY_CredentialValidator]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_AgentShroud™ Communication Templates]]
- 3 edges to [[_COMMUNITY_Himalaya Email CLI]]
- 3 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 2 edges to [[_COMMUNITY_Pre-Purge Secret Rotation Checklist]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_check_message()]]
- 1 edge to [[_COMMUNITY_Core Principles]]
- 1 edge to [[_COMMUNITY_v0.8.0 Watchtower — Security Fixes + Module Wi]]
- 1 edge to [[_COMMUNITY_GSDE&G Development Master Checklist (MC)]]
- 1 edge to [[_COMMUNITY_Apple Platform Integration]]
- 1 edge to [[_COMMUNITY_Socrates — Dialogue Architect]]
- 1 edge to [[_COMMUNITY_Security Hardening Plan Reset — Real Agent Conta]]
- 1 edge to [[_COMMUNITY_MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_dockerscriptssecurity-scan.sh]]
- 1 edge to [[_COMMUNITY_i-gg SKILL — Git Workflow Guardian (GIT-GUARD)]]
- 1 edge to [[_COMMUNITY_icloudscriptscalendar.js]]
- 1 edge to [[_COMMUNITY_TestAuditStore]]
- 1 edge to [[_COMMUNITY_Skill Hermes Dev Workflow (HDEV)]]
- 1 edge to [[_COMMUNITY_agentshroud.yaml]]

## Top bridge nodes
- [[UserSessionManager]] - degree 146, connects to 30 communities
- [[test_session_manager.py]] - degree 14, connects to 1 community
- [[.from_dict()_11]] - degree 7, connects to 1 community
- [[session_manager.py]] - degree 5, connects to 1 community
- [[Test File Sandbox Message Gate Suite]] - degree 2, connects to 1 community