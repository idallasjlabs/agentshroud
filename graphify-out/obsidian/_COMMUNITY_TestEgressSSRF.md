---
type: community
cohesion: 0.18
members: 11
---

# TestEgressSSRF

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-setup_method()_27]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_mapped_ipv6_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv4_private()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_loopback()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_ipv6_ula()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_link_local()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_block_localhost_variants()]] - code - gateway/tests/test_security_hardening.py
- [[TestEgressSSRF]] - code - gateway/tests/test_security_hardening.py
- [[Tests for SSRF protection in egress filter.]] - rationale - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressSSRF
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]

## Top bridge nodes
- [[TestEgressSSRF]] - degree 28, connects to 8 communities
- [[dot-setup_method()_27]] - degree 3, connects to 2 communities
