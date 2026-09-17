---
source_file: "gateway/security/canary_tripwire.py"
type: "code"
community: "TrustManager"
location: "L44"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TrustManager
---

# CanaryTripwire

## Connections
- [[.__init__()_93]] - `method` [EXTRACTED]
- [[._check_encoded()]] - `method` [EXTRACTED]
- [[._check_plain()]] - `method` [EXTRACTED]
- [[._normalize()]] - `method` [EXTRACTED]
- [[._record()_1]] - `method` [EXTRACTED]
- [[.detection_count()]] - `method` [EXTRACTED]
- [[.register_canary()]] - `method` [EXTRACTED]
- [[.scan()_1]] - `method` [EXTRACTED]
- [[.scan_response()]] - `method` [EXTRACTED]
- [[.setup_method()_21]] - `calls` [EXTRACTED]
- [[.test_custom_config()_1]] - `calls` [EXTRACTED]
- [[.test_no_canaries()]] - `calls` [EXTRACTED]
- [[.test_scan_response_no_block_when_block_disabled()]] - `calls` [EXTRACTED]
- [[TestCanaryTripwire]] - `uses` [INFERRED]
- [[TestE2E01PromptGuardBlocking]] - `uses` [INFERRED]
- [[TestE2E02InboundPIIRedaction]] - `uses` [INFERRED]
- [[TestE2E03OutboundPIIRedaction]] - `uses` [INFERRED]
- [[TestE2E04ContextGuardBlocking]] - `uses` [INFERRED]
- [[TestE2E05CanaryTripwire]] - `uses` [INFERRED]
- [[TestE2E06EncodingBypassDetection]] - `uses` [INFERRED]
- [[TestE2E07TrustEnforcement]] - `uses` [INFERRED]
- [[TestE2E08AuditChainIntegrity]] - `uses` [INFERRED]
- [[TestE2E09SessionIsolation]] - `uses` [INFERRED]
- [[TestE2E10FailClosed]] - `uses` [INFERRED]
- [[_BrokenOutputCanary]] - `uses` [INFERRED]
- [[_BrokenSanitizer]] - `uses` [INFERRED]
- [[canary_tripwire.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[pipeline()_1]] - `calls` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_canary_tripwire.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TrustManager