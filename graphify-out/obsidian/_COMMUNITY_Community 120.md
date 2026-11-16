---
type: community
members: 103
---

# Community 120

**Members:** 103 nodes

## Members
- [[.__init__()_58]] - code - gateway/proxy/web_proxy.py
- [[.__init__()_222]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_223]] - code - gateway/tests/test_web_proxy_security.py
- [[.__init__()_224]] - code - gateway/tests/test_web_proxy_security.py
- [[._audit()_1]] - code - gateway/proxy/web_proxy.py
- [[.check()_1]] - code - gateway/proxy/web_proxy.py
- [[.check_request()]] - code - gateway/proxy/web_proxy.py
- [[.flagged()_2]] - code - gateway/proxy/web_proxy.py
- [[.reset()]] - code - gateway/proxy/web_proxy.py
- [[.scan_response()]] - code - gateway/proxy/web_proxy.py
- [[.setUp()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[.test_aws_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_encoded_injection_in_html()]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_in_query_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_in_url_path_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_browser_security_blocks_high_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_browser_security_flags_medium_risk_urls()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_browser_security_skips_non_browser_user_agents()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_clean_comment_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_different_domains_independent()]] - code - gateway/tests/test_web_proxy.py
- [[.test_dns_filter_blocks_suspicious_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_dns_filter_flags_but_allows_questionable_domains()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_egress_monitor_logs_responses()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_browser_security_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_dns_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_graceful_degradation_egress_error()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_injection_in_hidden_div()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_html_comment()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_invisible_text()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_meta_tag()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_stats()]] - code - gateway/tests/test_web_proxy.py
- [[.test_long_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_multiple_security_modules_integration()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[.test_normal_content_type_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_oauth_security_error_handling()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_oauth_security_flags_auth_headers()]] - code - gateway/tests/test_web_proxy_security.py
- [[.test_passthrough_adds_header()]] - code - gateway/tests/test_web_proxy.py
- [[.test_passthrough_allows_everything()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_passthrough_skips_content_scan()]] - code - gateway/tests/test_web_proxy.py
- [[.test_pii_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_pii_in_url_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_private_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_rate_limit_blocks_excess()]] - code - gateway/tests/test_web_proxy.py
- [[.test_rate_limiter_reset()]] - code - gateway/tests/test_web_proxy.py
- [[.test_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_response_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_single_zwc_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_ssn_in_url_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_stats_tracked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_suspicious_content_type_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_zero_width_chars_detected()]] - code - gateway/tests/test_web_proxy.py
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
- [[RateLimiter_1]] - code - gateway/proxy/web_proxy.py
- [[Record an audit entry in the hash chain.]] - rationale - gateway/proxy/web_proxy.py
- [[Result of proxying a web request.]] - rationale - gateway/proxy/web_proxy.py
- [[Scan a response body for prompt injection, PII, and hidden content.          Thi]] - rationale - gateway/proxy/web_proxy.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_web_proxy_security.py
- [[Simple in-memory per-domain rate limiter using sliding window.]] - rationale - gateway/proxy/web_proxy.py
- [[Single zero-width chars are normal (e.g., word joiners).]] - rationale - gateway/tests/test_web_proxy.py
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
- [[TestDataExfiltration_1]] - code - gateway/tests/test_web_proxy.py
- [[TestEncodedPayloads]] - code - gateway/tests/test_web_proxy.py
- [[TestHiddenContent]] - code - gateway/tests/test_web_proxy.py
- [[TestPIIDetection_2]] - code - gateway/tests/test_web_proxy.py
- [[TestPassthroughMode_1]] - code - gateway/tests/test_web_proxy.py
- [[TestRateLimiting_4]] - code - gateway/tests/test_web_proxy.py
- [[TestStats_1]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxySecurityIntegration]] - code - gateway/tests/test_web_proxy_security.py
- [[TestZeroWidthAttacks]] - code - gateway/tests/test_web_proxy.py
- [[WebProxy_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxyResult]] - code - gateway/proxy/web_proxy.py
- [[audit_chain()]] - code - gateway/tests/test_web_proxy.py
- [[config()_4]] - code - gateway/tests/test_web_proxy.py
- [[passthrough_proxy()_1]] - code - gateway/tests/test_web_proxy.py
- [[proxy()_4]] - code - gateway/tests/test_web_proxy.py
- [[test_web_proxy.py]] - code - gateway/tests/test_web_proxy.py
- [[test_web_proxy_security.py]] - code - gateway/tests/test_web_proxy_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_120
SORT file.name ASC
```

## Connections to other communities
- 56 edges to [[_COMMUNITY_Community 27]]
- 16 edges to [[_COMMUNITY_Community 1566]]
- 12 edges to [[_COMMUNITY_Community 81]]
- 11 edges to [[_COMMUNITY_Community 93]]
- 10 edges to [[_COMMUNITY_Community 72]]
- 10 edges to [[_COMMUNITY_Community 86]]
- 5 edges to [[_COMMUNITY_Community 8]]
- 4 edges to [[_COMMUNITY_Community 1427]]
- 2 edges to [[_COMMUNITY_Community 151]]
- 2 edges to [[_COMMUNITY_Community 709]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 1000]]

## Top bridge nodes
- [[WebProxy_1]] - degree 73, connects to 9 communities
- [[ProxyAction]] - degree 31, connects to 6 communities
- [[RateLimiter_1]] - degree 28, connects to 5 communities
- [[test_web_proxy.py]] - degree 27, connects to 3 communities
- [[WebProxyResult]] - degree 16, connects to 3 communities