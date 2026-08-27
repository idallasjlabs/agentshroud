---
source_file: "gateway/tests/test_web_proxy_security.py"
type: "code"
community: "Community 119"
location: "L23"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_119
---

# MockDNSVerdict

## Connections
- [[.__init__()_192]] - `method` [EXTRACTED]
- [[.test_browser_security_blocks_high_risk_urls()]] - `calls` [EXTRACTED]
- [[.test_browser_security_flags_medium_risk_urls()]] - `calls` [EXTRACTED]
- [[.test_browser_security_skips_non_browser_user_agents()]] - `calls` [EXTRACTED]
- [[.test_dns_filter_blocks_suspicious_domains()]] - `calls` [EXTRACTED]
- [[.test_dns_filter_flags_but_allows_questionable_domains()]] - `calls` [EXTRACTED]
- [[.test_graceful_degradation_browser_security_error()]] - `calls` [EXTRACTED]
- [[.test_multiple_security_modules_integration()]] - `calls` [EXTRACTED]
- [[.test_oauth_security_error_handling()]] - `calls` [EXTRACTED]
- [[.test_oauth_security_flags_auth_headers()]] - `calls` [EXTRACTED]
- [[DNSVerdict]] - `shares_data_with` [AMBIGUOUS]
- [[ProxyAction]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyResult]] - `uses` [INFERRED]
- [[test_web_proxy_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_119