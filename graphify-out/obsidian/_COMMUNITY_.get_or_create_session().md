---
type: community
cohesion: 0.10
members: 23
---

# .get_or_create_session()

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Members
- [[._save_sessions()]] - code - gateway/security/session_manager.py
- [[._validate_bot_id()]] - code - gateway/security/session_manager.py
- [[.add_conversation_message()]] - code - gateway/security/session_manager.py
- [[.cleanup_old_sessions()_1]] - code - gateway/security/session_manager.py
- [[.get_or_create_session()]] - code - gateway/security/session_manager.py
- [[.get_session_context()]] - code - gateway/security/session_manager.py
- [[.get_session_prompt_addition()]] - code - gateway/security/session_manager.py
- [[.get_user_workspace_path()]] - code - gateway/security/session_manager.py
- [[.reanchor_system_prompt()]] - code - gateway/security/session_manager.py
- [[.to_dict()_10]] - code - gateway/security/session_manager.py
- [[.update_user_trust_level()]] - code - gateway/security/session_manager.py
- [[Add a message to the user's conversation history for a specific bot.]] - rationale - gateway/security/session_manager.py
- [[Any_50]] - code - gateway/security/session_manager.py
- [[Atomically persist current sessions to the metadata file.          Writes are se]] - rationale - gateway/security/session_manager.py
- [[Clean up sessions that haven't been active for the specified number of days.]] - rationale - gateway/security/session_manager.py
- [[Convert session to dictionary for serialization.]] - rationale - gateway/security/session_manager.py
- [[Get existing session or create a new one for the (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py
- [[Get session context for injection into agent request.]] - rationale - gateway/security/session_manager.py
- [[Get session-specific prompt addition for the agent.]] - rationale - gateway/security/session_manager.py
- [[Get the workspace path for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Return the system prompt with a re-anchoring preamble prepended.          Called]] - rationale - gateway/security/session_manager.py
- [[Update the trust level for a user within a bot's namespace.]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize bot_id to prevent path traversal.          Allows alphanum]] - rationale - gateway/security/session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_or_create_session
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_.from_dict()]]
- 2 edges to [[_COMMUNITY_.get_or_create_group_session()]]
- 2 edges to [[_COMMUNITY_UserSession]]

## Top bridge nodes
- [[.get_or_create_session()]] - degree 13, connects to 4 communities
- [[.add_conversation_message()]] - degree 6, connects to 2 communities
- [[._save_sessions()]] - degree 7, connects to 1 community
- [[Any_50]] - degree 5, connects to 1 community
- [[.to_dict()_10]] - degree 4, connects to 1 community