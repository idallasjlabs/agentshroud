---
type: community
cohesion: 0.06
members: 52
---

# Module Group 77

**Cohesion:** 0.06 - loosely connected
**Members:** 52 nodes

## Members
- [[.__init__()_143]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_145]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_144]] - code - gateway/tests/test_web_proxy_security.py
- [[._audit()]] - code - gateway/proxy/web_proxy.py
- [[.check()_1]] - code - gateway/proxy/web_proxy.py
- [[.check_request()]] - code - gateway/proxy/web_proxy.py
- [[.flagged()_2]] - code - gateway/proxy/web_proxy.py
- [[.get_stats()_10]] - code - gateway/proxy/web_proxy.py
- [[.scan_response()]] - code - gateway/proxy/web_proxy.py
- [[.setUp()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_browser_security_blocks_high_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_browser_security_flags_medium_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_browser_security_skips_non_browser_user_agents()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_dns_filter_blocks_suspicious_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_dns_filter_flags_but_allows_questionable_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_egress_monitor_logs_responses()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_browser_security_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_dns_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_egress_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_multiple_security_modules_integration()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_oauth_security_error_handling()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_oauth_security_flags_auth_headers()]] - code - gateway/tests/test_web_proxy_security.py
- [[.to_dict()_2]] - code - gateway/proxy/web_proxy.py
- [[Any_20]] - code - gateway/proxy/web_proxy.py
- [[Check an outbound HTTP request before it's sent.          This is the pre-flight]] - rationale - gateway/proxy/web_proxy.py
- [[Check if request is within rate limit. Returns True if allowed.]] - rationale - gateway/proxy/web_proxy.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/web_proxy.py
- [[MockDNSVerdict]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressChannel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressEvent]] - code - gateway/tests/test_web_proxy_security.py
- [[MockThreatLevel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockURLResult]] - code - gateway/tests/test_web_proxy_security.py
- [[Record an audit entry in the hash chain.]] - rationale - gateway/proxy/web_proxy.py
- [[Result of proxying a web request.]] - rationale - gateway/proxy/web_proxy.py
- [[Scan a response body for prompt injection, PII, and hidden content.          Thi]] - rationale - gateway/proxy/web_proxy.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that DNS filter blocks suspicious domains.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that DNS filter errors cause fail-closed behavior.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that DNS filter flags questionable domains but allows them through.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that OAuth security errors don't block requests.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that OAuth security flags requests with authorization headers.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that browser security blocks high-risk URLs for browser user agents.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that browser security checks are skipped for non-browser user agents.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that browser security errors cause fail-closed behavior.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that browser security flags medium-risk URLs.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that egress monitor logs all outbound connections.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that egress monitoring errors don't break response processing.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that multiple security modules work together correctly.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Test that security modules are properly integrated into web proxy.]] - rationale - gateway/tests/test_web_proxy_security.py
- [[TestWebProxySecurityIntegration]] - code - gateway/tests/test_web_proxy_security.py
- [[WebProxyResult]] - code - gateway/proxy/web_proxy.py
- [[test_web_proxy_security.py]] - code - gateway/tests/test_web_proxy_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_77
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 3 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 62]]
- 2 edges to [[_COMMUNITY_Module Group 199]]
- 2 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[WebProxyResult]] - degree 16, connects to 4 communities
- [[Any_20]] - degree 6, connects to 3 communities
- [[test_web_proxy_security.py]] - degree 10, connects to 2 communities
- [[.scan_response()]] - degree 5, connects to 2 communities
- [[MockEgressChannel]] - degree 5, connects to 2 communities