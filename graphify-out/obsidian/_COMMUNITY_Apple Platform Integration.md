---
type: community
cohesion: 0.33
members: 6
---

# Apple Platform Integration

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_clean_message_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_dict_message_handled()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_direct_no_session_manager_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_non_owner_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestCrossSessionAccess]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Apple_Platform_Integration
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_CredentialValidator]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[TestCrossSessionAccess]] - degree 10, connects to 4 communities
- [[.test_non_owner_blocked()]] - degree 2, connects to 1 community
- [[.test_owner_allowed()]] - degree 2, connects to 1 community