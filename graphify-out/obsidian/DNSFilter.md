---
source_file: "gateway/security/dns_filter.py"
type: "code"
community: "Dns Filter"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Dns_Filter
---

# DNSFilter

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[.__init__()_44]] - `calls` [EXTRACTED]
- [[.__init__()_72]] - `method` [EXTRACTED]
- [[._cleanup_rate_window()]] - `method` [EXTRACTED]
- [[._detect_tunneling()]] - `method` [EXTRACTED]
- [[._domain_in_allowlist()]] - `method` [EXTRACTED]
- [[._is_private_ip()_1]] - `method` [EXTRACTED]
- [[.check()_4]] - `method` [EXTRACTED]
- [[.check_rebinding()]] - `method` [EXTRACTED]
- [[.dns_filter()]] - `calls` [EXTRACTED]
- [[.get_audit_log()_3]] - `method` [EXTRACTED]
- [[.get_flagged_queries()]] - `method` [EXTRACTED]
- [[.resolve_and_cache()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestAuditLogging]] - `uses` [INFERRED]
- [[TestDNSAllowlist]] - `uses` [INFERRED]
- [[TestDNSFilterConfig]] - `uses` [INFERRED]
- [[TestDNSRebinding]] - `uses` [INFERRED]
- [[TestDNSTunnelingDetection]] - `uses` [INFERRED]
- [[TestEntropyCalculator]] - `uses` [INFERRED]
- [[TestNormalDNSResolution]] - `uses` [INFERRED]
- [[TestRateLimiting_1]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[WebContentScanner]] - `semantically_similar_to` [INFERRED]
- [[dns_filter()]] - `calls` [EXTRACTED]
- [[dns_filter.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[monitor_filter()]] - `calls` [EXTRACTED]
- [[strict_filter()]] - `calls` [EXTRACTED]
- [[test_dns_filter.py]] - `imports` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Dns_Filter