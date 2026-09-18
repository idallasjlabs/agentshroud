---
type: community
cohesion: 0.06
members: 61
---

# WebProxy

**Cohesion:** 0.06 - loosely connected
**Members:** 61 nodes

## Members
- [[.__init__()_198]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_199]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_200]] - code - gateway/tests/test_web_proxy_security.py
- [[._audit()_1]] - code - gateway/proxy/web_proxy.py
- [[.check()_6]] - code - gateway/proxy/web_proxy.py
- [[.check_request()]] - code - gateway/proxy/web_proxy.py
- [[.flagged()_2]] - code - gateway/proxy/web_proxy.py
- [[.scan_response()_2]] - code - gateway/proxy/web_proxy.py
- [[.setUp()_1]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[.test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
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
- [[.test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[.test_normal_content_type_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_oauth_security_error_handling()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_oauth_security_flags_auth_headers()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_response_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_suspicious_content_type_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[Check an outbound HTTP request before it's sent.          This is the pre-flight]] - rationale - gateway/proxy/web_proxy.py
- [[Check if request is within rate limit. Returns True if allowed.]] - rationale - gateway/proxy/web_proxy.py
- [[HTTP web traffic proxy for OpenClaw.      Intercepts all outbound web requests,]] - rationale - gateway/proxy/web_proxy.py
- [[MockDNSVerdict]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressChannel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressEvent]] - code - gateway/tests/test_web_proxy_security.py
- [[MockThreatLevel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockURLResult]] - code - gateway/tests/test_web_proxy_security.py
- [[Proxy works without an audit chain.]] - rationale - gateway/tests/test_web_proxy.py
- [[ProxyAction]] - code - gateway/proxy/web_proxy.py
- [[Record an audit entry in the hash chain.]] - rationale - gateway/proxy/web_proxy.py
- [[Result of proxying a web request.]] - rationale - gateway/proxy/web_proxy.py
- [[Scan a response body for prompt injection, PII, and hidden content.          Thi]] - rationale - gateway/proxy/web_proxy.py
- [[Set up test fixtures._5]] - rationale - gateway/tests/test_web_proxy_security.py
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
- [[TestAuditChain_1]] - code - gateway/tests/test_web_proxy.py
- [[TestContentTypeFiltering]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxySecurityIntegration]] - code - gateway/tests/test_web_proxy_security.py
- [[WebProxy]] - code - gateway/proxy/web_proxy.py
- [[WebProxyResult]] - code - gateway/proxy/web_proxy.py
- [[test_web_proxy_security.py]] - code - gateway/tests/test_web_proxy_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebProxy
SORT file.name ASC
```

## Connections to other communities
- 50 edges to [[_COMMUNITY_WebProxyConfig]]
- 10 edges to [[_COMMUNITY_test_http_proxy.py]]
- 9 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 9 edges to [[_COMMUNITY_URLAnalyzer]]
- 8 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_Enum]]
- 3 edges to [[_COMMUNITY__DummyTargetWriter]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_._process_connect()]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_TestDataExfiltration]]
- 2 edges to [[_COMMUNITY_TestSSRFBlocking]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[WebProxy]] - degree 74, connects to 11 communities
- [[ProxyAction]] - degree 31, connects to 6 communities
- [[WebProxyResult]] - degree 16, connects to 3 communities
- [[TestAuditChain_1]] - degree 12, connects to 2 communities
- [[TestContentTypeFiltering]] - degree 9, connects to 2 communities