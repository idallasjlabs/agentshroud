---
type: community
cohesion: 0.17
members: 12
---

# TestAllowlistMode

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-allowlist_config()]] - code - gateway/tests/test_web_proxy.py
- [[dot-allowlist_proxy()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_default_mode_is_denylist()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denylist_mode_still_works()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_listed_domain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ssrf_blocked_before_allowlist_check()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_unlisted_domain_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_deeper_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[Default (denylist) mode is unchanged.]] - rationale - gateway/tests/test_web_proxy.py
- [[Default-deny allowlist unlisted domains are blocked.]] - rationale - gateway/tests/test_web_proxy.py
- [[TestAllowlistMode]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAllowlistMode
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestAllowlistMode]] - degree 17, connects to 3 communities
- [[dot-allowlist_config()]] - degree 2, connects to 1 community
- [[dot-allowlist_proxy()]] - degree 2, connects to 1 community
- [[dot-test_default_mode_is_denylist()]] - degree 2, connects to 1 community
