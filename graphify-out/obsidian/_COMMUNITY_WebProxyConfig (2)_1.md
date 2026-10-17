---
type: community
members: 12
---

# WebProxyConfig (2)

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
TABLE source_file, type FROM #community/WebProxyConfig_2
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_WebProxyConfig]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_ProxyAction]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestAllowlistMode]] - degree 17, connects to 4 communities
- [[dot-allowlist_config()]] - degree 2, connects to 1 community
- [[dot-allowlist_proxy()]] - degree 2, connects to 1 community
- [[dot-test_default_mode_is_denylist()]] - degree 2, connects to 1 community
