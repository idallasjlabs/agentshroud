---
source_file: "gateway/proxy/http_proxy.py"
type: "code"
community: "Gateway Security Module"
location: "L111"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Security_Module
---

# WebProxy

## Connections
- [[.__init__()_22]] - `references` [EXTRACTED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_allowlist_proxy()]] - `calls` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[test_blocked_domain_is_tracked_in_recent()]] - `calls` [INFERRED]
- [[test_connect_blocked_domain_returns_403()]] - `calls` [INFERRED]
- [[test_connect_denied_by_egress_filter_returns_403()]] - `calls` [INFERRED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `calls` [INFERRED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `calls` [INFERRED]
- [[test_proxy_created_with_custom_web_proxy()]] - `calls` [INFERRED]
- [[test_telegram_api_blocked_in_connect_proxy()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Gateway_Security_Module