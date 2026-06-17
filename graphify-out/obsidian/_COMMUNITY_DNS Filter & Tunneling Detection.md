---
type: community
cohesion: 0.04
members: 65
---

# DNS Filter & Tunneling Detection

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[._cleanup_rate_window()]] - code - gateway/security/dns_filter.py
- [[._detect_tunneling()]] - code - gateway/security/dns_filter.py
- [[._domain_in_allowlist()]] - code - gateway/security/dns_filter.py
- [[.check()_3]] - code - gateway/security/dns_filter.py
- [[.get_audit_log()]] - code - gateway/security/dns_filter.py
- [[.get_flagged_queries()]] - code - gateway/security/dns_filter.py
- [[.shannon_entropy()]] - code - gateway/security/dns_filter.py
- [[.test_allowlist_blocks_unlisted_in_enforce()]] - code - gateway/tests/test_dns_filter.py
- [[.test_allowlist_permits_listed_domain()]] - code - gateway/tests/test_dns_filter.py
- [[.test_allowlist_permits_subdomain()]] - code - gateway/tests/test_dns_filter.py
- [[.test_base64_in_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_burst_queries_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_common_services_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[.test_default_allows_all_domains()]] - code - gateway/tests/test_dns_filter.py
- [[.test_default_mode_is_enforce()]] - code - gateway/tests/test_dns_filter.py
- [[.test_empty_string()]] - code - gateway/tests/test_dns_filter.py
- [[.test_enforce_mode_blocks_tunneling()]] - code - gateway/tests/test_dns_filter.py
- [[.test_flagged_queries_in_log()]] - code - gateway/tests/test_dns_filter.py
- [[.test_generous_defaults()]] - code - gateway/tests/test_dns_filter.py
- [[.test_hex_encoded_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_high_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[.test_high_entropy_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_log_contains_timestamp()]] - code - gateway/tests/test_dns_filter.py
- [[.test_log_contains_verdict()]] - code - gateway/tests/test_dns_filter.py
- [[.test_long_but_legitimate_domain()]] - code - gateway/tests/test_dns_filter.py
- [[.test_low_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[.test_monitor_mode_never_blocks()]] - code - gateway/tests/test_dns_filter.py
- [[.test_multiple_long_labels_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_no_allowlist_allows_all()]] - code - gateway/tests/test_dns_filter.py
- [[.test_normal_domain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[.test_normal_rate_not_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_private_ip_detection()]] - code - gateway/tests/test_dns_filter.py
- [[.test_public_ip_not_private()]] - code - gateway/tests/test_dns_filter.py
- [[.test_queries_logged()]] - code - gateway/tests/test_dns_filter.py
- [[.test_resolve_and_cache_empty_domain_graceful()]] - code - gateway/tests/test_dns_filter.py
- [[.test_stable_resolution_passes()]] - code - gateway/tests/test_dns_filter.py
- [[.test_strict_has_allowlist()]] - code - gateway/tests/test_dns_filter.py
- [[.test_subdomain_allowed()]] - code - gateway/tests/test_dns_filter.py
- [[.test_very_long_subdomain_flagged()]] - code - gateway/tests/test_dns_filter.py
- [[DNSQuery]] - code - gateway/security/dns_filter.py
- [[DNSVerdict]] - code - gateway/security/dns_filter.py
- [[Default mode is enforce after v0.8.0 enforcement hardening.]] - rationale - gateway/tests/test_dns_filter.py
- [[EntropyCalculator]] - code - gateway/security/dns_filter.py
- [[Even suspicious queries pass in monitor mode.]] - rationale - gateway/tests/test_dns_filter.py
- [[Known private ranges should be detected.]] - rationale - gateway/tests/test_dns_filter.py
- [[Public IPs should not be flagged as private.]] - rationale - gateway/tests/test_dns_filter.py
- [[Resolving a domain that fails should return empty string gracefully.]] - rationale - gateway/tests/test_dns_filter.py
- [[Seeding the same IP twice should not flag rebinding.]] - rationale - gateway/tests/test_dns_filter.py
- [[TestAuditLogging]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSAllowlist]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSFilterConfig]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSRebinding]] - code - gateway/tests/test_dns_filter.py
- [[TestDNSTunnelingDetection]] - code - gateway/tests/test_dns_filter.py
- [[TestEntropyCalculator]] - code - gateway/tests/test_dns_filter.py
- [[TestNormalDNSResolution]] - code - gateway/tests/test_dns_filter.py
- [[TestRateLimiting]] - code - gateway/tests/test_dns_filter.py
- [[TunnelingPattern]] - code - gateway/security/dns_filter.py
- [[default_config()]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter()]] - code - gateway/tests/test_dns_filter.py
- [[dns_filter.py]] - code - gateway/security/dns_filter.py
- [[monitor_config()]] - code - gateway/tests/test_dns_filter.py
- [[monitor_filter()]] - code - gateway/tests/test_dns_filter.py
- [[strict_config()]] - code - gateway/tests/test_dns_filter.py
- [[strict_filter()]] - code - gateway/tests/test_dns_filter.py
- [[test_dns_filter.py]] - code - gateway/tests/test_dns_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DNS_Filter__Tunneling_Detection
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 9 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 4 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_Module Group 110]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Module Group 66]]
- 1 edge to [[_COMMUNITY_Module Group 137]]

## Top bridge nodes
- [[EntropyCalculator]] - degree 34, connects to 9 communities
- [[test_dns_filter.py]] - degree 17, connects to 1 community
- [[TestDNSTunnelingDetection]] - degree 10, connects to 1 community
- [[TestDNSRebinding]] - degree 9, connects to 1 community
- [[TestNormalDNSResolution]] - degree 9, connects to 1 community