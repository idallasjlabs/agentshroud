---
source_file: "gateway/proxy/web_proxy.py"
type: "code"
community: "lifespan.py"
location: "L140"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/lifespanpy
---

# WebProxy

## Connections
- [[dot-__init__()_156]] - `references` [EXTRACTED]
- [[dot-__init__()_159]] - `method` [EXTRACTED]
- [[dot-_audit()]] - `method` [EXTRACTED]
- [[dot-allowlist_proxy()]] - `calls` [EXTRACTED]
- [[dot-check_request()]] - `method` [EXTRACTED]
- [[dot-get_stats()_8]] - `method` [EXTRACTED]
- [[dot-scan_response()_2]] - `method` [EXTRACTED]
- [[dot-setUp()]] - `calls` [EXTRACTED]
- [[dot-test_custom_denylist()]] - `calls` [EXTRACTED]
- [[dot-test_custom_domain_size_limit()]] - `calls` [EXTRACTED]
- [[dot-test_different_domains_independent()]] - `calls` [EXTRACTED]
- [[dot-test_no_audit_chain_no_crash()]] - `calls` [EXTRACTED]
- [[dot-test_rate_limit_blocks_excess()]] - `calls` [EXTRACTED]
- [[BrowserSecurityGuard]] - `uses` [INFERRED]
- [[DNSFilter]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[EgressChannel]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressMonitor]] - `uses` [INFERRED]
- [[EgressMonitorConfig]] - `uses` [INFERRED]
- [[HTTP web traffic proxy for OpenClaw. Intercepts all outbound web requests, runs…]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[NetworkValidator]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `uses` [INFERRED]
- [[TestAllowlistMode]] - `uses` [INFERRED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestDomainDenylist]] - `uses` [INFERRED]
- [[TestRateLimiting_1]] - `uses` [INFERRED]
- [[TestResponseSizeLimits]] - `uses` [INFERRED]
- [[TestWebProxySecurityIntegration]] - `uses` [INFERRED]
- [[URLAnalyzer]] - `uses` [INFERRED]
- [[WebContentScanner]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_allowlist_proxy()]] - `calls` [EXTRACTED]
- [[http_proxy.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[passthrough_proxy()_1]] - `uses` [INFERRED]
- [[proxy()_2]] - `uses` [INFERRED]
- [[test_blocked_domain_is_tracked_in_recent()]] - `uses` [INFERRED]
- [[test_connect_blocked_domain_returns_403()]] - `uses` [INFERRED]
- [[test_connect_denied_by_egress_filter_returns_403()]] - `uses` [INFERRED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `uses` [INFERRED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `uses` [INFERRED]
- [[test_http_proxy.py]] - `imports` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `imports` [EXTRACTED]
- [[test_proxy_created_with_custom_web_proxy()]] - `calls` [EXTRACTED]
- [[test_telegram_api_blocked_in_connect_proxy()]] - `calls` [EXTRACTED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]
- [[test_web_proxy_security.py]] - `imports` [EXTRACTED]
- [[web_proxy.py_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/lifespanpy
