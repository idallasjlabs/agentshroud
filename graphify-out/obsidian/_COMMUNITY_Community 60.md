---
type: community
members: 37
---

# Community 60

**Members:** 37 nodes

## Members
- [[.test_cross_group_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_legacy_no_rbac_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_non_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_unknown_group_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A legitimate group member's write lands.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A member of group B cannot write into group A's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user who is NOT a member of the target group cannot poison its memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat with no RBAC context supplied, the namespace-isolation         call]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any group's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Writing to a group that does not exist in the RBAC config is denied.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[rbac()_5]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory.py (SharedMemoryManager)]] - code - gateway/security/shared_memory.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_60
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 1]]
- 7 edges to [[_COMMUNITY_Community 61]]
- 6 edges to [[_COMMUNITY_Community 196]]
- 6 edges to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 479]]

## Top bridge nodes
- [[test_shared_memory_write_acl.py]] - degree 13, connects to 4 communities
- [[TestGroupMemoryWriteACL]] - degree 11, connects to 4 communities
- [[TestUserMemoryWriteACL]] - degree 9, connects to 4 communities
- [[TestAuthorizationHelper]] - degree 8, connects to 4 communities
- [[TestWriteFailurePath]] - degree 7, connects to 4 communities