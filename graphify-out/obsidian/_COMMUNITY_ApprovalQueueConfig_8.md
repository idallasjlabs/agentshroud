---
type: community
cohesion: 0.08
members: 25
---

# ApprovalQueueConfig

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[rbac()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager()_3]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager.py (UserSessionManager)]] - code - gateway/security/session_manager.py
- [[shared_memory()_1]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory.py (SharedMemoryManager)]] - code - gateway/security/shared_memory.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_RBACConfig]]
- 5 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_telegram_proxy.py]]
- 5 edges to [[_COMMUNITY_UserSessionManager_3]]
- 2 edges to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_UserSessionManager_1]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_2]]

## Top bridge nodes
- [[test_shared_memory_write_acl.py]] - degree 13, connects to 5 communities
- [[TestUserMemoryWriteACL]] - degree 9, connects to 4 communities
- [[TestAuthorizationHelper]] - degree 8, connects to 4 communities
- [[TestWriteFailurePath]] - degree 7, connects to 4 communities
- [[session_manager.py (UserSessionManager)]] - degree 5, connects to 4 communities
