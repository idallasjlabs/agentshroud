---
type: community
cohesion: 0.04
members: 112
---

# HTTP CONNECT Proxy & Egress

**Cohesion:** 0.04 - loosely connected
**Members:** 112 nodes

## Members
- [[.__init__()_15]] - code - gateway/proxy/http_proxy.py
- [[.__init__()_34]] - code - gateway/proxy/web_proxy.py
- [[.allowlist_config()]] - code - gateway/tests/test_web_proxy.py
- [[.allowlist_proxy()]] - code - gateway/tests/test_web_proxy.py
- [[.get_domain_settings()]] - code - gateway/proxy/web_config.py
- [[.is_domain_allowed()]] - code - gateway/proxy/web_config.py
- [[.is_domain_denied()]] - code - gateway/proxy/web_config.py
- [[.reset()]] - code - gateway/proxy/web_proxy.py
- [[.test_allowed_domain_passes()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[.test_aws_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_encoded_injection_in_html()]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_in_query_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_base64_in_url_path_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[.test_case_insensitive()_2]] - code - gateway/tests/test_web_proxy.py
- [[.test_clean_comment_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_custom_denylist()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_custom_domain_size_limit()]] - code - gateway/tests/test_web_proxy.py
- [[.test_default_mode_is_denylist()]] - code - gateway/tests/test_web_proxy.py
- [[.test_denied_domain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_denied_domain_malware()]] - code - gateway/tests/test_web_proxy.py
- [[.test_denied_subdomain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_denylist_mode_still_works()]] - code - gateway/tests/test_web_proxy.py
- [[.test_different_domains_independent()]] - code - gateway/tests/test_web_proxy.py
- [[.test_domain_denied()]] - code - gateway/tests/test_web_proxy.py
- [[.test_domain_not_in_denylist_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_empty_allowlist_blocks_everything()]] - code - gateway/tests/test_web_proxy.py
- [[.test_exact_match()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_get_domain_settings_custom()]] - code - gateway/tests/test_web_proxy.py
- [[.test_get_domain_settings_default()]] - code - gateway/tests/test_web_proxy.py
- [[.test_github_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_hidden_div()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_html_comment()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_invisible_text()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_in_meta_tag()]] - code - gateway/tests/test_web_proxy.py
- [[.test_injection_stats()]] - code - gateway/tests/test_web_proxy.py
- [[.test_large_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_listed_domain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_long_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[.test_normal_content_type_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_normal_response_not_flagged_for_size()]] - code - gateway/tests/test_web_proxy.py
- [[.test_passthrough_adds_header()]] - code - gateway/tests/test_web_proxy.py
- [[.test_passthrough_allows_everything()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_passthrough_mode_default_off()]] - code - gateway/tests/test_web_proxy.py
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
- [[.test_ssrf_blocked_before_allowlist_check()]] - code - gateway/tests/test_web_proxy.py
- [[.test_stackoverflow_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_stats_tracked()]] - code - gateway/tests/test_web_proxy.py
- [[.test_suspicious_content_type_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[.test_unlisted_domain_blocked()_1]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_deeper_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_does_not_match_other_root()]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_domain_settings()]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_matches_root_domain()]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_matches_subdomain()]] - code - gateway/tests/test_web_proxy.py
- [[.test_wildcard_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[.test_zero_width_chars_detected()]] - code - gateway/tests/test_web_proxy.py
- [[CONNECT tunnel must NOT allow api.telegram.org — forces traffic through reverse]] - rationale - gateway/tests/test_http_proxy.py
- [[Check if a domain is on the allowlist (used when mode == 'allowlist').]] - rationale - gateway/proxy/web_config.py
- [[Check if a domain is on the denylist.]] - rationale - gateway/proxy/web_config.py
- [[Configuration for the web traffic proxy.      Default-allow all URLs pass unles]] - rationale - gateway/proxy/web_config.py
- [[Default (denylist) mode is unchanged.]] - rationale - gateway/tests/test_web_proxy.py
- [[Default-deny allowlist unlisted domains are blocked.]] - rationale - gateway/tests/test_web_proxy.py
- [[DomainSettings]] - code - gateway/proxy/web_config.py
- [[EgressFilter]] - code - gateway/proxy/http_proxy.py
- [[Get settings for a specific domain, falling back to defaults.]] - rationale - gateway/proxy/web_config.py
- [[HTTP web traffic proxy for OpenClaw.      Intercepts all outbound web requests,]] - rationale - gateway/proxy/web_proxy.py
- [[Per-domain configuration overrides.]] - rationale - gateway/proxy/web_config.py
- [[Proxy works without an audit chain.]] - rationale - gateway/tests/test_web_proxy.py
- [[ProxyAction]] - code - gateway/proxy/web_proxy.py
- [[RateLimiter_1]] - code - gateway/proxy/web_proxy.py
- [[Simple in-memory per-domain rate limiter using sliding window.]] - rationale - gateway/proxy/web_proxy.py
- [[Single zero-width chars are normal (e.g., word joiners).]] - rationale - gateway/tests/test_web_proxy.py
- [[TestAllowlistMode]] - code - gateway/tests/test_web_proxy.py
- [[TestAuditChain_1]] - code - gateway/tests/test_web_proxy.py
- [[TestContentTypeFiltering]] - code - gateway/tests/test_web_proxy.py
- [[TestDataExfiltration_1]] - code - gateway/tests/test_web_proxy.py
- [[TestDomainDenylist]] - code - gateway/tests/test_web_proxy.py
- [[TestEncodedPayloads]] - code - gateway/tests/test_web_proxy.py
- [[TestHiddenContent]] - code - gateway/tests/test_web_proxy.py
- [[TestIsDomainAllowed]] - code - gateway/tests/test_web_proxy.py
- [[TestPIIDetection_2]] - code - gateway/tests/test_web_proxy.py
- [[TestPassthroughMode_1]] - code - gateway/tests/test_web_proxy.py
- [[TestRateLimiting_3]] - code - gateway/tests/test_web_proxy.py
- [[TestResponseSizeLimits]] - code - gateway/tests/test_web_proxy.py
- [[TestStats_1]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxyConfig]] - code - gateway/tests/test_web_proxy.py
- [[TestZeroWidthAttacks]] - code - gateway/tests/test_web_proxy.py
- [[Unit tests for WebProxyConfig.is_domain_allowed().]] - rationale - gateway/tests/test_web_proxy.py
- [[WebProxy_1]] - code - gateway/proxy/web_proxy.py
- [[WebProxy]] - code - gateway/proxy/http_proxy.py
- [[WebProxyConfig]] - code - gateway/proxy/web_config.py
- [[config()_3]] - code - gateway/tests/test_web_proxy.py
- [[passthrough_proxy()_1]] - code - gateway/tests/test_web_proxy.py
- [[proxy()_2]] - code - gateway/tests/test_web_proxy.py
- [[test_hc_ping_allowed()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_hc_ping_subdomain_not_blocked()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_heartbeat_egress.py]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_telegram_api_blocked_in_connect_proxy()]] - code - gateway/tests/test_http_proxy.py
- [[test_web_proxy.py]] - code - gateway/tests/test_web_proxy.py
- [[web_config.py]] - code - gateway/proxy/web_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HTTP_CONNECT_Proxy__Egress
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Module Group 65]]
- 22 edges to [[_COMMUNITY_Module Group 77]]
- 18 edges to [[_COMMUNITY_HTTP Proxy Coverage Tests]]
- 17 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 7 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Module Group 448]]
- 6 edges to [[_COMMUNITY_Module Group 340]]
- 6 edges to [[_COMMUNITY_Module Group 199]]
- 5 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 4 edges to [[_COMMUNITY_Module Group 303]]
- 4 edges to [[_COMMUNITY_Module Group 386]]
- 3 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 3 edges to [[_COMMUNITY_Module Group 240]]
- 3 edges to [[_COMMUNITY_Module Group 62]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]

## Top bridge nodes
- [[WebProxy_1]] - degree 74, connects to 13 communities
- [[WebProxyConfig]] - degree 82, connects to 12 communities
- [[ProxyAction]] - degree 31, connects to 7 communities
- [[RateLimiter_1]] - degree 28, connects to 6 communities
- [[web_config.py]] - degree 6, connects to 4 communities
