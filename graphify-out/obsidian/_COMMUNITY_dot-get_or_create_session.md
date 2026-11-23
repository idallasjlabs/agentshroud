---
type: community
members: 32
---

# .get_or_create_session

**Members:** 32 nodes

## Members
- [[dot-__init__()_180]] - code - gateway/security/session_manager.py
- [[dot-_load_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_save_sessions()]] - code - gateway/security/session_manager.py
- [[dot-_session_key()]] - code - gateway/security/session_manager.py
- [[dot-_validate_bot_id()]] - code - gateway/security/session_manager.py
- [[dot-add_conversation_message()]] - code - gateway/security/session_manager.py
- [[dot-get_or_create_session()]] - code - gateway/security/session_manager.py
- [[dot-get_session_context()]] - code - gateway/security/session_manager.py
- [[dot-get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[dot-get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[dot-list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[dot-reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[dot-to_dict()_7]] - code - gateway/security/session_manager.py
- [[dot-update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_70]] - code
- [[Atomically persist current sessions to the metadata file. Writes are serialized…]] - rationale - gateway/security/session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair. Each…]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Initialize session manager. Args base_workspace Base directory for user…]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see. Returns the full…]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file. Handles both the new…]] - rationale - gateway/security/session_manager.py
- [[Path_64]] - code
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended. Called after a…]] - rationale - gateway/security/session_manager.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal. Allows alphanumeric…]] - rationale - gateway/security/session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_or_create_session
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_UserSessionManager]]
- 5 edges to [[_COMMUNITY_test_session_manager.py]]

## Top bridge nodes
- [[dot-get_or_create_session()]] - degree 12, connects to 2 communities
- [[dot-_load_sessions()]] - degree 5, connects to 2 communities
- [[ConversationMessage]] - degree 4, connects to 2 communities
- [[dot-add_conversation_message()]] - degree 6, connects to 1 community
- [[dot-_save_sessions()]] - degree 5, connects to 1 community
