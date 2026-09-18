---
type: community
cohesion: 0.17
members: 13
---

# .from_dict()

**Cohesion:** 0.17 - loosely connected
**Members:** 13 nodes

## Members
- [[.__init__()_179]] - code - gateway/security/session_manager.py
- [[._load_sessions()]] - code - gateway/security/session_manager.py
- [[._session_key()]] - code - gateway/security/session_manager.py
- [[.from_dict()_7]] - code - gateway/security/session_manager.py
- [[.list_sessions_for_user()]] - code - gateway/security/session_manager.py
- [[A single message in a conversation.]] - rationale - gateway/security/session_manager.py
- [[ConversationMessage]] - code - gateway/security/session_manager.py
- [[Create session from dictionary.]] - rationale - gateway/security/session_manager.py
- [[Initialize session manager.          Args             base_workspace Base dire]] - rationale - gateway/security/session_manager.py
- [[List session keys that the requesting user is allowed to see.          Returns t]] - rationale - gateway/security/session_manager.py
- [[Load existing sessions from metadata file.          Handles both the new ``{use]] - rationale - gateway/security/session_manager.py
- [[Path_44]] - code - gateway/security/session_manager.py
- [[Return the cache key string for a (user_id, bot_id) pair.]] - rationale - gateway/security/session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/from_dict
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_.get_or_create_session()]]
- 1 edge to [[_COMMUNITY_UserSession]]
- 1 edge to [[_COMMUNITY_cls]]

## Top bridge nodes
- [[.from_dict()_7]] - degree 7, connects to 3 communities
- [[._session_key()]] - degree 5, connects to 2 communities
- [[ConversationMessage]] - degree 4, connects to 2 communities
- [[._load_sessions()]] - degree 5, connects to 1 community
- [[.__init__()_179]] - degree 4, connects to 1 community