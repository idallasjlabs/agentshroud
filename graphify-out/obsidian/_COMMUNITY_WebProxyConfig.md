---
type: community
cohesion: 0.03
members: 122
---

# WebProxyConfig

**Cohesion:** 0.03 - loosely connected
**Members:** 122 nodes

## Members
- [[dot-__init__()_3]] - code - gateway/proxy/web_proxy.py
- [[dot-__init__()_106]] - code - gateway/proxy/http_proxy.py
- [[dot-allowlist_config()]] - code - gateway/tests/test_web_proxy.py
- [[dot-allowlist_proxy()]] - code - gateway/tests/test_web_proxy.py
- [[dot-check()]] - code - gateway/proxy/web_proxy.py
- [[dot-get_domain_settings()]] - code - gateway/proxy/web_config.py
- [[dot-is_domain_allowed()]] - code - gateway/proxy/web_config.py
- [[dot-is_domain_denied()]] - code - gateway/proxy/web_config.py
- [[dot-reset()]] - code - gateway/proxy/web_proxy.py
- [[dot-test_10_x_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_127_0_0_1_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_169_254_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_192_168_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_allowed_domain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_aws_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_base64_in_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_base64_in_url_path_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_case_insensitive()_2]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_clean_comment_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_clean_content_no_injection()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_custom_denylist()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_custom_domain_size_limit()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_data_exfil_instruction_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_decimal_ip_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_default_mode_is_denylist()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_domain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_domain_malware()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_subdomain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denylist_mode_still_works()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_different_domains_independent()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_domain_denied()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_domain_not_in_denylist_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_empty_allowlist_blocks_everything()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_exact_match()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_get_domain_settings_custom()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_get_domain_settings_default()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_github_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_hex_ip_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ignore_instructions_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_adds_security_headers()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_hidden_div()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_html_comment()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_invisible_text()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_meta_tag()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_stats()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ipv4_mapped_ipv6_192_168_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ipv4_mapped_ipv6_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ipv6_loopback_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_large_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_listed_domain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_localhost_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_long_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_normal_content_type_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_normal_response_not_flagged_for_size()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_adds_header()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_allows_everything()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_mode_default_off()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_skips_content_scan()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_url_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_private_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_public_ip_allowed()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_rate_limit_blocks_excess()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_rate_limiter_reset()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_role_override_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_single_zwc_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ssn_in_url_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ssrf_blocked_before_allowlist_check()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_stackoverflow_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_stats_tracked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_suspicious_content_type_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_system_delimiter_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_tool_invocation_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_unlisted_domain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_deeper_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_does_not_match_other_root()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_domain_settings()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_matches_root_domain()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_matches_subdomain()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_subdomain_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_zero_width_chars_detected()]] - code - gateway/tests/test_web_proxy.py
- [[CONNECT tunnel must NOT allow api.telegram.org — forces traffic through reverse]] - rationale - gateway/tests/test_http_proxy.py
- [[Check if a domain is on the allowlist (used when mode == 'allowlist').]] - rationale - gateway/proxy/web_config.py
- [[Check if a domain is on the denylist.]] - rationale - gateway/proxy/web_config.py
- [[Check if request is within rate limit. Returns True if allowed.]] - rationale - gateway/proxy/web_proxy.py
- [[Configuration for the web traffic proxy.      Default-allow all URLs pass unles]] - rationale - gateway/proxy/web_config.py
- [[Default (denylist) mode is unchanged.]] - rationale - gateway/tests/test_web_proxy.py
- [[Default-deny allowlist unlisted domains are blocked.]] - rationale - gateway/tests/test_web_proxy.py
- [[DomainSettings]] - code - gateway/proxy/web_config.py
- [[EgressFilter]] - code - gateway/proxy/http_proxy.py
- [[Get settings for a specific domain, falling back to defaults.]] - rationale - gateway/proxy/web_config.py
- [[Per-domain configuration overrides.]] - rationale - gateway/proxy/web_config.py
- [[RateLimiter]] - code - gateway/proxy/web_proxy.py
- [[Simple in-memory per-domain rate limiter using sliding window.]] - rationale - gateway/proxy/web_proxy.py
- [[Single zero-width chars are normal (e.g., word joiners).]] - rationale - gateway/tests/test_web_proxy.py
- [[TestAllowlistMode]] - code - gateway/tests/test_web_proxy.py
- [[TestContentTypeFiltering]] - code - gateway/tests/test_web_proxy.py
- [[TestDataExfiltration]] - code - gateway/tests/test_web_proxy.py
- [[TestDomainDenylist]] - code - gateway/tests/test_web_proxy.py
- [[TestHiddenContent]] - code - gateway/tests/test_web_proxy.py
- [[TestIsDomainAllowed]] - code - gateway/tests/test_web_proxy.py
- [[TestPIIDetection_2]] - code - gateway/tests/test_web_proxy.py
- [[TestPassthroughMode]] - code - gateway/tests/test_web_proxy.py
- [[TestPromptInjectionDetection]] - code - gateway/tests/test_web_proxy.py
- [[TestRateLimiting]] - code - gateway/tests/test_web_proxy.py
- [[TestResponseSizeLimits]] - code - gateway/tests/test_web_proxy.py
- [[TestSSRFBlocking]] - code - gateway/tests/test_web_proxy.py
- [[TestStats_1]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxyConfig]] - code - gateway/tests/test_web_proxy.py
- [[TestZeroWidthAttacks]] - code - gateway/tests/test_web_proxy.py
- [[Unit tests for WebProxyConfig.is_domain_allowed().]] - rationale - gateway/tests/test_web_proxy.py
- [[WebProxy_1]] - code - gateway/proxy/http_proxy.py
- [[WebProxyConfig]] - code - gateway/proxy/web_config.py
- [[config()]] - code - gateway/tests/test_web_proxy.py
- [[hc-ping.com must be egress-allowlisted or Hermes dead-man's-switch heartbeat fires permanently]] - rationale - gateway/tests/test_heartbeat_egress.py
- [[passthrough_proxy()]] - code - gateway/tests/test_web_proxy.py
- [[proxy()_1]] - code - gateway/tests/test_web_proxy.py
- [[test_hc_ping_allowed()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_hc_ping_subdomain_not_blocked()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_heartbeat_egress.py]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_telegram_api_blocked_in_connect_proxy()]] - code - gateway/tests/test_http_proxy.py
- [[test_web_proxy.py]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/WebProxyConfig
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_ProxyAction]]
- 17 edges to [[_COMMUNITY_AuditChain]]
- 10 edges to [[_COMMUNITY_WebProxy]]
- 10 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection]]
- 3 edges to [[_COMMUNITY__DummyTargetWriter]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_dot-_process_connect]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]

## Top bridge nodes
- [[WebProxyConfig]] - degree 73, connects to 8 communities
- [[TestDataExfiltration]] - degree 11, connects to 3 communities
- [[test_web_proxy.py]] - degree 27, connects to 2 communities
- [[RateLimiter]] - degree 26, connects to 2 communities
- [[DomainSettings]] - degree 24, connects to 2 communities
