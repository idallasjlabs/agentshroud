---
source_file: "gateway/proxy/web_config.py"
type: "code"
community: "WebProxy"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/WebProxy
---

# WebProxyConfig

## Connections
- [[dot-__init__()_163]] - `calls` [EXTRACTED]
- [[dot-__init__()_50]] - `references` [EXTRACTED]
- [[dot-allowlist_config()]] - `calls` [EXTRACTED]
- [[dot-get_domain_settings()]] - `method` [EXTRACTED]
- [[dot-is_domain_allowed()]] - `method` [EXTRACTED]
- [[dot-is_domain_denied()]] - `method` [EXTRACTED]
- [[dot-test_case_insensitive()_2]] - `calls` [EXTRACTED]
- [[dot-test_custom_denylist()]] - `calls` [EXTRACTED]
- [[dot-test_custom_domain_size_limit()]] - `calls` [EXTRACTED]
- [[dot-test_default_mode_is_denylist()]] - `calls` [EXTRACTED]
- [[dot-test_different_domains_independent()]] - `calls` [EXTRACTED]
- [[dot-test_empty_allowlist_blocks_everything()]] - `calls` [EXTRACTED]
- [[dot-test_exact_match()]] - `calls` [EXTRACTED]
- [[dot-test_get_domain_settings_custom()]] - `calls` [EXTRACTED]
- [[dot-test_rate_limit_blocks_excess()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_does_not_match_other_root()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_domain_settings()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_matches_root_domain()]] - `calls` [EXTRACTED]
- [[dot-test_wildcard_matches_subdomain()]] - `calls` [EXTRACTED]
- [[Configuration for the web traffic proxy. Default-allow all URLs pass unless…]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[TestAllowlistMode]] - `uses` [INFERRED]
- [[TestDomainDenylist]] - `uses` [INFERRED]
- [[TestIsDomainAllowed]] - `uses` [INFERRED]
- [[TestRateLimiting_1]] - `uses` [INFERRED]
- [[TestResponseSizeLimits]] - `uses` [INFERRED]
- [[TestWebProxyConfig]] - `uses` [INFERRED]
- [[WebProxy]] - `uses` [INFERRED]
- [[_allowlist_proxy()]] - `calls` [EXTRACTED]
- [[config()_2]] - `uses` [INFERRED]
- [[http_proxy.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[passthrough_proxy()_1]] - `uses` [INFERRED]
- [[test_blocked_domain_is_tracked_in_recent()]] - `uses` [INFERRED]
- [[test_connect_blocked_domain_returns_403()]] - `uses` [INFERRED]
- [[test_connect_denied_by_egress_filter_returns_403()]] - `uses` [INFERRED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `uses` [INFERRED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `uses` [INFERRED]
- [[test_hc_ping_allowed()]] - `calls` [EXTRACTED]
- [[test_hc_ping_subdomain_not_blocked()]] - `calls` [EXTRACTED]
- [[test_heartbeat_egress.py]] - `imports` [EXTRACTED]
- [[test_http_proxy.py]] - `imports` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `imports` [EXTRACTED]
- [[test_proxy_created_with_custom_web_proxy()]] - `calls` [EXTRACTED]
- [[test_telegram_api_blocked_in_connect_proxy()]] - `calls` [EXTRACTED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]
- [[web_config.py_2]] - `contains` [EXTRACTED]
- [[web_proxy.py_2]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/WebProxy
