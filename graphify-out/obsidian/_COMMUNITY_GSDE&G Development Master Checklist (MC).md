---
type: community
cohesion: 0.50
members: 4
---

# GSDE&G Development Master Checklist (MC)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_browser_exception_fails_closed()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_high_threat_blocked()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_low_threat_allowed()]] - code - gateway/tests/test_middleware_coverage.py
- [[TestBrowserSecurity]] - code - gateway/tests/test_middleware_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GSDEG_Development_Master_Checklist_MC
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_CredentialValidator]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[TestBrowserSecurity]] - degree 8, connects to 4 communities
- [[.test_browser_exception_fails_closed()]] - degree 2, connects to 1 community
- [[.test_high_threat_blocked()]] - degree 2, connects to 1 community
- [[.test_low_threat_allowed()]] - degree 2, connects to 1 community