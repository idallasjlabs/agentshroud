---
type: community
cohesion: 0.36
members: 8
---

# test_security_regressions_v1_2.py

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[fixture]] - code
- [[session_manager()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[tmp_workspace()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[v1.2.0 Security Regression Tests Every test in this file corresponds to a…]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_regressions_v1_2py
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_TestBotIdIsolationInSharedMemory]]
- 1 edge to [[_COMMUNITY_TestCrossBotTrustPivot]]
- 1 edge to [[_COMMUNITY_TestSessionPathSeparation]]
- 1 edge to [[_COMMUNITY_TestHermesTrustSeeding]]
- 1 edge to [[_COMMUNITY_TestHermesDashboardForwarderBinding]]
- 1 edge to [[_COMMUNITY_TestHermesEgressAllowlist]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_TestRewriteRequestHeaders]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 13, connects to 8 communities
- [[trust_manager()]] - degree 3, connects to 1 community
