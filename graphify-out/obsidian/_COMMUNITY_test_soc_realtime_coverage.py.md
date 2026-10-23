---
type: community
cohesion: 0.03
members: 119
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.03 - loosely connected
**Members:** 119 nodes

## Members
- [[NOTE api.telegram.org is intentionally NOT listed here.  The bot is]] - rationale - gateway/proxy/http_proxy.py
- [[dot-__init__()_4]] - code - gateway/proxy/web_proxy.py
- [[dot-__init__()_5]] - code - gateway/proxy/web_proxy.py
- [[dot-__init__()_109]] - code - gateway/proxy/http_proxy.py
- [[dot-check()]] - code - gateway/proxy/web_proxy.py
- [[dot-get_domain_settings()]] - code - gateway/proxy/web_config.py
- [[dot-is_domain_allowed()]] - code - gateway/proxy/web_config.py
- [[dot-is_domain_denied()]] - code - gateway/proxy/web_config.py
- [[dot-readline()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[dot-reset()]] - code - gateway/proxy/web_proxy.py
- [[dot-test_allowed_domain_passes()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_audit_chain_valid()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_aws_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_base64_encoded_injection_in_html()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_base64_in_query_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_base64_in_url_path_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_blocked_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_case_insensitive()_2]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_clean_comment_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_clean_content_no_injection()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_custom_denylist()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_custom_domain_size_limit()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_data_exfil_instruction_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_domain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_domain_malware()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_denied_subdomain_blocked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_different_domains_independent()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_domain_denied()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_domain_not_in_denylist_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_empty_allowlist_blocks_everything()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_exact_match()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_get_domain_settings_custom()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_get_domain_settings_default()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_github_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ignore_instructions_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_adds_security_headers()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_hidden_div()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_html_comment()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_invisible_text()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_in_meta_tag()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_injection_stats()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_large_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_long_query_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_no_audit_chain_no_crash()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_normal_content_type_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_normal_response_not_flagged_for_size()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_adds_header()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_allows_everything()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_mode_default_off()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_passthrough_skips_content_scan()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_url_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_private_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_rate_limit_blocks_excess()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_rate_limiter_reset()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_request_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_response_audited()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_role_override_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_single_zwc_not_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ssn_in_url_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_stackoverflow_passes()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_stats_tracked()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_suspicious_content_type_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_system_delimiter_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_tool_invocation_detected()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_does_not_match_other_root()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_domain_settings()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_matches_root_domain()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_wildcard_matches_subdomain()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_zero_width_chars_detected()]] - code - gateway/tests/test_web_proxy.py
- [[CONNECT tunnel must NOT allow api.telegram.org — forces traffic through reverse]] - rationale - gateway/tests/test_http_proxy.py
- [[Check if a domain is on the allowlist (used when mode == 'allowlist').]] - rationale - gateway/proxy/web_config.py
- [[Check if a domain is on the denylist.]] - rationale - gateway/proxy/web_config.py
- [[Check if request is within rate limit. Returns True if allowed.]] - rationale - gateway/proxy/web_proxy.py
- [[Configuration for the web traffic proxy.      Default-allow all URLs pass unles]] - rationale - gateway/proxy/web_config.py
- [[DomainSettings]] - code - gateway/proxy/web_config.py
- [[EgressFilter_2]] - code - gateway/proxy/http_proxy.py
- [[Get settings for a specific domain, falling back to defaults.]] - rationale - gateway/proxy/web_config.py
- [[HTTP web traffic proxy for OpenClaw. Intercepts all outbound web requests, runs…]] - rationale - gateway/proxy/web_proxy.py
- [[Per-domain configuration overrides.]] - rationale - gateway/proxy/web_config.py
- [[Proxy works without an audit chain.]] - rationale - gateway/tests/test_web_proxy.py
- [[RateLimiter]] - code - gateway/proxy/web_proxy.py
- [[Simple in-memory per-domain rate limiter using sliding window.]] - rationale - gateway/proxy/web_proxy.py
- [[Single zero-width chars are normal (e.g., word joiners).]] - rationale - gateway/tests/test_web_proxy.py
- [[TestAuditChain_1]] - code - gateway/tests/test_web_proxy.py
- [[TestContentTypeFiltering]] - code - gateway/tests/test_web_proxy.py
- [[TestDataExfiltration_1]] - code - gateway/tests/test_web_proxy.py
- [[TestDomainDenylist]] - code - gateway/tests/test_web_proxy.py
- [[TestEncodedPayloads]] - code - gateway/tests/test_web_proxy.py
- [[TestHiddenContent]] - code - gateway/tests/test_web_proxy.py
- [[TestIsDomainAllowed]] - code - gateway/tests/test_web_proxy.py
- [[TestPIIDetection_2]] - code - gateway/tests/test_web_proxy.py
- [[TestPassthroughMode]] - code - gateway/tests/test_web_proxy.py
- [[TestPromptInjectionDetection]] - code - gateway/tests/test_web_proxy.py
- [[TestRateLimiting_1]] - code - gateway/tests/test_web_proxy.py
- [[TestResponseSizeLimits]] - code - gateway/tests/test_web_proxy.py
- [[TestStats_1]] - code - gateway/tests/test_web_proxy.py
- [[TestWebProxyConfig]] - code - gateway/tests/test_web_proxy.py
- [[TestZeroWidthAttacks]] - code - gateway/tests/test_web_proxy.py
- [[URLAnalyzer]] - code
- [[Unit tests for WebProxyConfig.is_domain_allowed().]] - rationale - gateway/tests/test_web_proxy.py
- [[WebProxy]] - code - gateway/proxy/web_proxy.py
- [[WebProxy_1]] - code - gateway/proxy/http_proxy.py
- [[WebProxyConfig]] - code - gateway/proxy/web_config.py
- [[WebProxyConfig_1]] - code
- [[_TimeoutReader]] - code - gateway/tests/test_http_proxy_coverage.py
- [[audit_chain()]] - code - gateway/tests/test_web_proxy.py
- [[config()_1]] - code - gateway/tests/test_web_proxy.py
- [[hc-ping.com must be egress-allowlisted or Hermes dead-man's-switch heartbeat fires permanently]] - rationale - gateway/tests/test_heartbeat_egress.py
- [[http_proxy.py]] - code - gateway/proxy/http_proxy.py
- [[passthrough_proxy()]] - code - gateway/tests/test_web_proxy.py
- [[proxy()_2]] - code - gateway/tests/test_web_proxy.py
- [[readline() always raises TimeoutError — simulates a stalled client.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[test_hc_ping_allowed()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_hc_ping_subdomain_not_blocked()]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_heartbeat_egress.py]] - code - gateway/tests/test_heartbeat_egress.py
- [[test_telegram_api_blocked_in_connect_proxy()]] - code - gateway/tests/test_http_proxy.py
- [[test_web_proxy.py]] - code - gateway/tests/test_web_proxy.py
- [[web_config.py]] - code - gateway/proxy/web_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_scanner_integration.py]]
- 24 edges to [[_COMMUNITY__pcm_bytes]]
- 17 edges to [[_COMMUNITY_AuditChain]]
- 16 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 8 edges to [[_COMMUNITY_TestAllowlistMode]]
- 6 edges to [[_COMMUNITY_Usage]]
- 5 edges to [[_COMMUNITY_AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap]]
- 4 edges to [[_COMMUNITY_GitHub Skill]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_TestDataExfiltration]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[WebProxy]] - degree 70, connects to 8 communities
- [[http_proxy.py]] - degree 15, connects to 8 communities
- [[WebProxyConfig]] - degree 71, connects to 6 communities
- [[test_web_proxy.py]] - degree 27, connects to 4 communities
- [[RateLimiter]] - degree 26, connects to 3 communities
