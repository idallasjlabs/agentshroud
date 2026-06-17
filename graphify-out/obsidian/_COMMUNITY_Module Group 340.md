---
type: community
cohesion: 0.17
members: 12
---

# Module Group 340

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_10_x_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_127_0_0_1_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_169_254_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_192_168_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_decimal_ip_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_hex_ip_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_ipv4_mapped_ipv6_192_168_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_ipv4_mapped_ipv6_blocked()_2]] - code - gateway/tests/test_web_proxy.py
- [[.test_ipv6_loopback_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_localhost_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_public_ip_allowed()_1]] - code - gateway/tests/test_web_proxy.py
- [[TestSSRFBlocking]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_340
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 1 edge to [[_COMMUNITY_Security Pipeline & Audit Chain]]

## Top bridge nodes
- [[TestSSRFBlocking]] - degree 18, connects to 2 communities