---
type: community
cohesion: 0.06
members: 63
---

# ProxyAction

**Cohesion:** 0.06 - loosely connected
**Members:** 63 nodes

## Members
- [[dot-__init__()_52]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-__init__()_53]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-__init__()_54]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-_audit()]] - code - gateway/proxy/web_proxy.py
- [[dot-check_request()]] - code - gateway/proxy/web_proxy.py
- [[dot-flagged()_1]] - code - gateway/proxy/web_proxy.py
- [[dot-get_stats()]] - code - gateway/proxy/web_proxy.py
- [[dot-scan_response()]] - code - gateway/proxy/web_proxy.py
- [[dot-setUp()_1]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_browser_security_blocks_high_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_browser_security_flags_medium_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_browser_security_skips_non_browser_user_agents()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_dns_filter_blocks_suspicious_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_dns_filter_flags_but_allows_questionable_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_egress_monitor_logs_responses()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_graceful_degradation_browser_security_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_graceful_degradation_dns_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_graceful_degradation_egress_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_multiple_security_modules_integration()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_oauth_security_error_handling()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_oauth_security_flags_auth_headers()]] - code - gateway/tests/test_web_proxy_security.py
- [[dot-test_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_response_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-to_dict()]] - code - gateway/proxy/web_proxy.py
- [[Any_13]] - code
- [[Check an outbound HTTP request before it's sent. This is the pre-flight check.…]] - rationale - gateway/proxy/web_proxy.py
- [[Enum_2]] - code
- [[Get proxy statistics.]] - rationale - gateway/proxy/web_proxy.py
- [[HTTP web traffic proxy for OpenClaw. Intercepts all outbound web requests, runs…]] - rationale - gateway/proxy/web_proxy.py
- [[MockDNSVerdict]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressChannel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockEgressEvent]] - code - gateway/tests/test_web_proxy_security.py
- [[MockThreatLevel]] - code - gateway/tests/test_web_proxy_security.py
- [[MockURLResult]] - code - gateway/tests/test_web_proxy_security.py
- [[Proxy works without an audit chain.]] - rationale - gateway/tests/test_web_proxy.py
- [[ProxyAction]] - code - gateway/proxy/web_proxy.py
- [[Record an audit entry in the hash chain.]] - rationale - gateway/proxy/web_proxy.py
- [[Result of proxying a web request.]] - rationale - gateway/proxy/web_proxy.py
- [[Scan a response body for prompt injection, PII, and hidden content. This is…]] - rationale - gateway/proxy/web_proxy.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_web_proxy_security.py
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
- [[TestAuditChain]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxySecurityIntegration]] - code - gateway/tests/test_web_proxy_security.py
- [[WebProxy]] - code - gateway/proxy/web_proxy.py
- [[WebProxyResult]] - code - gateway/proxy/web_proxy.py
- [[str_2]] - code
- [[test_web_proxy_security.py]] - code - gateway/tests/test_web_proxy_security.py
- [[web_proxy.py]] - code - gateway/proxy/web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProxyAction
SORT file.name ASC
```

## Connections to other communities
- 47 edges to [[_COMMUNITY_WebProxyConfig]]
- 10 edges to [[_COMMUNITY_WebProxy]]
- 9 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 4 edges to [[_COMMUNITY_WebContentScanner]]
- 3 edges to [[_COMMUNITY__DummyTargetWriter]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_WebProxyConfig_2]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_egress_filter.py]]
- 2 edges to [[_COMMUNITY_dot-_process_connect]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_ConsentFramework_1]]
- 1 edge to [[_COMMUNITY_PipelineAction]]

## Top bridge nodes
- [[WebProxy]] - degree 72, connects to 10 communities
- [[web_proxy.py]] - degree 9, connects to 4 communities
- [[ProxyAction]] - degree 28, connects to 2 communities
- [[TestAuditChain]] - degree 12, connects to 2 communities
- [[MockEgressChannel]] - degree 6, connects to 2 communities
