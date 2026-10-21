---
type: community
members: 13
---

# Audit Ledger (SHA-256 hash only) (2)

**Members:** 13 nodes

## Members
- [[dot-test_cross_group_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_legacy_no_rbac_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_member_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_non_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_owner_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_unknown_group_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A legitimate group member's write lands.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A member of group B cannot write into group A's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user who is NOT a member of the target group cannot poison its memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat with no RBAC context supplied, the namespace-isolation         call]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any group's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Writing to a group that does not exist in the RBAC config is denied.]] - rationale - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Ledger_SHA-256_hash_only_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[TestGroupMemoryWriteACL]] - degree 11, connects to 3 communities
