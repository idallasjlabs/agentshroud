---
type: community
members: 73
---

# DNSFilterConfig

**Members:** 73 nodes

## Members
- [[dot-__init__()_182]] - code - gateway/security/dns_filter.py
- [[dot-_cleanup_rate_window()]] - code - gateway/security/dns_filter.py
- [[dot-_detect_tunneling()]] - code - gateway/security/dns_filter.py
- [[dot-_domain_in_allowlist()]] - code - gateway/security/dns_filter.py
- [[dot-_is_private_ip()_2]] - code - gateway/security/dns_filter.py
- [[dot-check()_5]] - code - gateway/security/dns_filter.py
- [[dot-check_rebinding()]] - code - gateway/security/dns_filter.py
- [[dot-dns_filter()]] - code - gateway/tests/test_dns_filter.py
- [[dot-get_audit_log()_6]] - code - gateway/security/dns_filter.py
- [[dot-get_flagged_queries()]] - code - gateway/security/dns_filter.py
- [[dot-resolve_and_cache()]] - code - gateway/security/dns_filter.py
- [[dot-shannon_entropy()]] - code - gateway/security/dns_filter.py
- [[dot-test_allowlist_blocks_unlisted_in_enforce()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_allowlist_permits_listed_domain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_allowlist_permits_subdomain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_base64_in_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_burst_queries_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_common_services_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_default_allows_all_domains()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_default_mode_is_enforce()_6]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_empty_string()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_enforce_mode_blocks_tunneling()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_flagged_queries_in_log()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_generous_defaults()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_hex_encoded_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_high_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_high_entropy_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_log_contains_timestamp()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_log_contains_verdict()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_long_but_legitimate_domain()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_low_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_monitor_mode_never_blocks()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_multiple_long_labels_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_no_allowlist_allows_all()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_normal_domain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_normal_rate_not_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_private_ip_detection()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_public_ip_not_private()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_queries_logged()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_resolve_and_cache_empty_domain_graceful()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_stable_resolution_passes()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_strict_has_allowlist()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_subdomain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_very_long_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[DNSFilter]] - code - gateway/security/dns_filter.py
- [[DNSQuery_1]] - code - gateway/security/dns_filter.py
- [[DNSVerdict]] - code - gateway/security/dns_filter.py
- [[Default mode is enforce after v0.8.0 enforcement hardening._2]] - rationale - gateway/tests/test_dns_filter.py
- [[Even suspicious queries pass in monitor mode.]] - rationale - gateway/tests/test_dns_filter.py
- [[Known private ranges should be detected.]] - rationale - gateway/tests/test_dns_filter.py
- [[Public IPs should not be flagged as private.]] - rationale - gateway/tests/test_dns_filter.py
- [[Resolve domain to an IP and cache it for 5 minutes.]] - rationale - gateway/security/dns_filter.py
- [[Resolving a domain that fails should return empty string gracefully.]] - rationale - gateway/tests/test_dns_filter.py
- [[Return True if a DNS rebinding attack is detected.          Re-resolves the doma]] - rationale - gateway/security/dns_filter.py
- [[Return True if the IP address is in a private  loopback range.]] - rationale - gateway/security/dns_filter.py
- [[Seeding the same IP twice should not flag rebinding.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestAuditLogging]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSAllowlist]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSFilterConfig]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSRebinding]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSTunnelingDetection]] - code - gateway/tests/test_dns_filter.py
- [[TestEntropyCalculator]] - code - gateway/tests/test_dns_filter.py
- [[TestNormalDNSResolution]] - code - gateway/tests/test_dns_filter.py
- [[TestRateLimiting_4]] - code - gateway/tests/test_dns_filter.py
- [[TunnelingPattern]] - code - gateway/security/dns_filter.py
- [[default_config()_4]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter()]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter.py_2]] - code - gateway/security/dns_filter.py
- [[monitor_config()_2]] - code - gateway/tests/test_dns_filter.py
- [[monitor_filter()]] - code - gateway/tests/test_dns_filter.py
- [[strict_config()_2]] - code - gateway/tests/test_dns_filter.py
- [[strict_filter()]] - code - gateway/tests/test_dns_filter.py
- [[test_dns_filter.py]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DNSFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_AlertDispatcher]]
- 12 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_ProxyAction]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_test_dns_canvas_coverage.py]]

## Top bridge nodes
- [[dns_filter.py_2]] - degree 9, connects to 4 communities
- [[DNSFilter]] - degree 36, connects to 3 communities
- [[test_dns_filter.py]] - degree 18, connects to 3 communities
- [[TestDNSTunnelingDetection]] - degree 10, connects to 2 communities
- [[TestDNSRebinding]] - degree 9, connects to 2 communities
