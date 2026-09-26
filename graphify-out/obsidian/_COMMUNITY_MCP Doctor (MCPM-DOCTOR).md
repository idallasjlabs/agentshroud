---
type: community
cohesion: 0.50
members: 4
---

# MCP Doctor (MCPM-DOCTOR)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_blocked_non_owner_denied()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_blocked_owner_exempted()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_tracker_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestMultiTurnTracker]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Doctor_MCPM-DOCTOR
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_CredentialValidator]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[TestMultiTurnTracker]] - degree 8, connects to 4 communities
- [[.test_blocked_non_owner_denied()]] - degree 2, connects to 1 community
- [[.test_blocked_owner_exempted()]] - degree 2, connects to 1 community
- [[.test_tracker_exception_fails_closed()]] - degree 2, connects to 1 community