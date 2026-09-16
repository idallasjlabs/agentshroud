---
source_file: "gateway/security/canary_tripwire.py"
type: "code"
community: "Canary Tripwire"
location: "L44"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Canary_Tripwire
---

# CanaryTripwire

## Connections
- [[dot-__init__()_93]] - `method` [EXTRACTED]
- [[dot-_check_encoded()]] - `method` [EXTRACTED]
- [[dot-_check_plain()]] - `method` [EXTRACTED]
- [[dot-_normalize()]] - `method` [EXTRACTED]
- [[dot-_record()_1]] - `method` [EXTRACTED]
- [[dot-detection_count()]] - `method` [EXTRACTED]
- [[dot-register_canary()]] - `method` [EXTRACTED]
- [[dot-scan()_1]] - `method` [EXTRACTED]
- [[dot-scan_response()]] - `method` [EXTRACTED]
- [[dot-setup_method()_21]] - `calls` [EXTRACTED]
- [[dot-test_custom_config()_1]] - `calls` [EXTRACTED]
- [[dot-test_no_canaries()]] - `calls` [EXTRACTED]
- [[dot-test_scan_response_no_block_when_block_disabled()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/Canary_Tripwire