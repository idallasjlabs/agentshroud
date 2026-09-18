---
source_file: "gateway/security/dns_filter.py"
type: "code"
community: "DNSFilterConfig"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DNSFilterConfig
---

# DNSFilter

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_154]] - `calls` [EXTRACTED]
- [[.__init__()_171]] - `method` [EXTRACTED]
- [[._cleanup_rate_window()]] - `method` [EXTRACTED]
- [[._detect_tunneling()]] - `method` [EXTRACTED]
- [[._domain_in_allowlist()]] - `method` [EXTRACTED]
- [[._is_private_ip()_2]] - `method` [EXTRACTED]
- [[.check()_4]] - `method` [EXTRACTED]
- [[.check_rebinding()]] - `method` [EXTRACTED]
- [[.dns_filter()]] - `calls` [EXTRACTED]
- [[.get_audit_log()_6]] - `method` [EXTRACTED]
- [[.get_flagged_queries()]] - `method` [EXTRACTED]
- [[.resolve_and_cache()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestAuditLogging_1]] - `uses` [INFERRED]
- [[TestDNSAllowlist]] - `uses` [INFERRED]
- [[TestDNSFilterConfig]] - `uses` [INFERRED]
- [[TestDNSRebinding]] - `uses` [INFERRED]
- [[TestDNSTunnelingDetection]] - `uses` [INFERRED]
- [[TestEntropyCalculator]] - `uses` [INFERRED]
- [[TestNormalDNSResolution]] - `uses` [INFERRED]
- [[TestRateLimiting_3]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[WebContentScanner]] - `semantically_similar_to` [INFERRED]
- [[dns_filter()]] - `calls` [EXTRACTED]
- [[dns_filter.py_2]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[monitor_filter()]] - `calls` [EXTRACTED]
- [[strict_filter()]] - `calls` [EXTRACTED]
- [[test_dns_filter.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DNSFilterConfig