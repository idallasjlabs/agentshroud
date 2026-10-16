---
type: community
cohesion: 0.29
members: 7
---

# ProxyAction

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_response_audited()]] - code - gateway/tests/test_web_proxy.py
- [[Proxy works without an audit chain.]] - rationale - gateway/tests/test_web_proxy.py
- [[TestAuditChain]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProxyAction
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_WebProxyConfig]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_ProxyAction]]
- 1 edge to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestAuditChain]] - degree 12, connects to 4 communities
- [[dot-test_no_audit_chain_no_crash()]] - degree 3, connects to 1 community
