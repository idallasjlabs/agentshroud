---
type: community
cohesion: 0.15
members: 13
---

# agentshroud.yaml

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_cross_group_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_legacy_no_rbac_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_non_member_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_owner_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_unknown_group_write_is_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A legitimate group member's write lands.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A member of group B cannot write into group A's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user who is NOT a member of the target group cannot poison its memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Back-compat with no RBAC context supplied, the namespace-isolation         call]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[TestGroupMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any group's memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Writing to a group that does not exist in the RBAC config is denied.]] - rationale - gateway/tests/test_shared_memory_write_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroudyaml
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]

## Top bridge nodes
- [[TestGroupMemoryWriteACL]] - degree 11, connects to 4 communities