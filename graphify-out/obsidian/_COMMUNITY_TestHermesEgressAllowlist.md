---
type: community
cohesion: 0.17
members: 12
---

# TestHermesEgressAllowlist

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_ai_security_research_domains_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_duckduckgo_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_failover_search_engines_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hc_ping_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_nousresearch_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[AI-security researchcompetitive-intel domains must be allowlisted.          The]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes base image is from nousresearch.com — must be in egress allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes ddgs-based web search requires duckduckgo.com.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes heartbeat uses hc-ping.com for dead-man's switch.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[PR190 failover search engines must be allowlisted.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesEgressAllowlist]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verify that Hermes-specific egress destinations are in the canonical allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestHermesEgressAllowlist
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[TestHermesEgressAllowlist]] - degree 11, connects to 4 communities