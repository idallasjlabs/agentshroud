---
type: community
members: 52
---

# DNSFilterConfig

**Members:** 52 nodes

## Members
- [[dot-__init__()_50]] - code - gateway/proxy/web_proxy.py
- [[dot-__init__()_51]] - code - gateway/security/dns_filter.py
- [[dot-_cleanup_rate_window()]] - code - gateway/security/dns_filter.py
- [[dot-_detect_tunneling()]] - code - gateway/security/dns_filter.py
- [[dot-_domain_in_allowlist()]] - code - gateway/security/dns_filter.py
- [[dot-_is_private_ip()_1]] - code - gateway/security/dns_filter.py
- [[dot-check()_1]] - code - gateway/security/dns_filter.py
- [[dot-dns_filter()]] - code - gateway/tests/test_dns_filter.py
- [[dot-get_audit_log()_1]] - code - gateway/security/dns_filter.py
- [[dot-get_flagged_queries()]] - code - gateway/security/dns_filter.py
- [[dot-resolve_and_cache()]] - code - gateway/security/dns_filter.py
- [[dot-test_allowlist_blocks_unlisted_in_enforce()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_allowlist_permits_listed_domain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_allowlist_permits_subdomain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_burst_queries_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_dns_filter_config()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_flagged_queries_in_log()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_log_contains_timestamp()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_log_contains_verdict()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_no_allowlist_allows_all()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_normal_rate_not_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_private_ip_detection()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_public_ip_not_private()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_queries_logged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_resolve_and_cache_empty_domain_graceful()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_stable_resolution_passes()]] - code - gateway/tests/test_dns_filter.py
- [[DNSFilter]] - code - gateway/security/dns_filter.py
- [[DNSFilterConfig]] - code - gateway/security/dns_filter.py
- [[DNSQuery]] - code - gateway/security/dns_filter.py
- [[DNSVerdict]] - code - gateway/security/dns_filter.py
- [[Known private ranges should be detected.]] - rationale - gateway/tests/test_dns_filter.py
- [[Public IPs should not be flagged as private.]] - rationale - gateway/tests/test_dns_filter.py
- [[Resolve domain to an IP and cache it for 5 minutes.]] - rationale - gateway/security/dns_filter.py
- [[Resolving a domain that fails should return empty string gracefully.]] - rationale - gateway/tests/test_dns_filter.py
- [[Return True if the IP address is in a private  loopback range.]] - rationale - gateway/security/dns_filter.py
- [[Seeding the same IP twice should not flag rebinding.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestAuditLogging]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSAllowlist]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSRebinding]] - code - gateway/tests/test_dns_filter.py
- [[TestRateLimiting]] - code - gateway/tests/test_dns_filter.py
- [[Tests for DNS exfiltration prevention.]] - rationale - gateway/tests/test_dns_filter.py
- [[TunnelingPattern]] - code - gateway/security/dns_filter.py
- [[default_config()]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter()]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter.py_2]] - code - gateway/security/dns_filter.py
- [[fixture_34]] - code
- [[monitor_config()]] - code - gateway/tests/test_dns_filter.py
- [[monitor_filter()]] - code - gateway/tests/test_dns_filter.py
- [[strict_config()]] - code - gateway/tests/test_dns_filter.py
- [[strict_filter()]] - code - gateway/tests/test_dns_filter.py
- [[t_dns()]] - code - gateway/ingest_api/main.py
- [[test_dns_filter.py]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DNSFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_WebProxy]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_TestExfiltrationDetection]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestModuleConfigDefaults]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 1 edge to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_TestNormalDNSResolution]]
- 1 edge to [[_COMMUNITY_TestDNSTunnelingDetection]]
- 1 edge to [[_COMMUNITY_TestDNSFilterConfig]]
- 1 edge to [[_COMMUNITY_BrowserSecurityGuard]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_OAuthSecurityValidator]]

## Top bridge nodes
- [[DNSFilterConfig]] - degree 23, connects to 9 communities
- [[dot-__init__()_50]] - degree 12, connects to 7 communities
- [[test_dns_filter.py]] - degree 19, connects to 4 communities
- [[dns_filter.py_2]] - degree 10, connects to 4 communities
- [[DNSFilter]] - degree 22, connects to 3 communities
