---
type: community
members: 20
---

# TestExfiltrationDetection

**Members:** 20 nodes

## Members
- [[dot-shannon_entropy()]] - code - gateway/security/dns_filter.py
- [[dot-test_dns_entropy_calculator()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dns_low_entropy_legit()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dns_tunneling_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_egress_monitor_loaded()_1]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_empty_string()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_env_guard_detects_data_access()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_high_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[dot-test_low_entropy_string()]] - code - gateway/tests/test_dns_filter.py
- [[Egress monitoring should be available.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[EntropyCalculator]] - code - gateway/security/dns_filter.py
- [[Environment guard should monitor data access patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard should catch credential patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[High-entropy DNS queries indicate tunneling.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[High-entropy domains (potential tunneling).]] - rationale - gateway/tests/test_security_audit.py
- [[Legit domains have lower entropy.]] - rationale - gateway/tests/test_security_audit.py
- [[Test detection of data exfiltration patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestEntropyCalculator]] - code - gateway/tests/test_dns_filter.py
- [[TestExfiltrationDetection]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestExfiltrationDetection
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_DNSFilterConfig]]
- 3 edges to [[_COMMUNITY_MetadataGuard]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_EnvironmentGuard]]
- 2 edges to [[_COMMUNITY_EgressEvent]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]

## Top bridge nodes
- [[TestExfiltrationDetection]] - degree 14, connects to 5 communities
- [[EntropyCalculator]] - degree 7, connects to 3 communities
- [[dot-shannon_entropy()]] - degree 8, connects to 1 community
- [[TestEntropyCalculator]] - degree 5, connects to 1 community
- [[dot-test_env_guard_detects_data_access()]] - degree 3, connects to 1 community
