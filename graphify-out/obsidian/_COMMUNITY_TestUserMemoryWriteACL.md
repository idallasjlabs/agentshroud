---
type: community
cohesion: 0.22
members: 9
---

# TestUserMemoryWriteACL

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestUserMemoryWriteACL
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestUserMemoryWriteACL]] - degree 9, connects to 3 communities