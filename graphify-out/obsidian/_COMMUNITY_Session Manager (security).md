---
type: community
cohesion: 0.25
members: 8
---

# Session Manager (security)

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[._validate_user_id()]] - code - gateway/security/session_manager.py
- [[.get_merged_context()]] - code - gateway/security/session_manager.py
- [[.get_or_create_group_session()]] - code - gateway/security/session_manager.py
- [[Get or create a shared workspace + MEMORY.md for a group.]] - rationale - gateway/security/session_manager.py
- [[GroupSession]] - code - gateway/security/session_manager.py
- [[Represents a shared workspace + memory for a group.]] - rationale - gateway/security/session_manager.py
- [[Return user MEMORY.md + all accessible group MEMORY.md contents for prompt injec]] - rationale - gateway/security/session_manager.py
- [[Validate and sanitize user_id to prevent path traversal.          Only allows al]] - rationale - gateway/security/session_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Session_Manager_security
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Middleware & Session Isolation]]
- 2 edges to [[_COMMUNITY_Session Manager (security)]]

## Top bridge nodes
- [[.get_merged_context()]] - degree 4, connects to 2 communities
- [[._validate_user_id()]] - degree 4, connects to 2 communities
- [[.get_or_create_group_session()]] - degree 5, connects to 1 community
- [[GroupSession]] - degree 3, connects to 1 community