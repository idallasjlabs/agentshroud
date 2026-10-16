---
type: community
cohesion: 0.23
members: 12
---

# .get_merged_memory_for_user

**Cohesion:** 0.23 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-_strip_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-contains_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-get_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[dot-get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_user_memory()]] - code - gateway/security/shared_memory.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user.          Args             user_id The user]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving         to non-]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return memory from groups whose focus_topics match the query text.          For]] - rationale - gateway/security/shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_merged_memory_for_user
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[dot-get_merged_memory_for_user()]] - degree 7, connects to 1 community
- [[dot-get_topic_scoped_memory()]] - degree 7, connects to 1 community
- [[dot-contains_private_content()]] - degree 4, connects to 1 community
- [[dot-get_group_memory()]] - degree 4, connects to 1 community
- [[dot-get_user_memory()]] - degree 4, connects to 1 community
