---
source_file: "gateway/security/canary_tripwire.py"
type: "code"
community: "Community 25"
location: "L44"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_25
---

# CanaryTripwire

## Connections
- [[.__init__()_75]] - `method` [EXTRACTED]
- [[._check_encoded()]] - `method` [EXTRACTED]
- [[._check_plain()]] - `method` [EXTRACTED]
- [[._normalize()]] - `method` [EXTRACTED]
- [[._record()_1]] - `method` [EXTRACTED]
- [[.detection_count()]] - `method` [EXTRACTED]
- [[.register_canary()]] - `method` [EXTRACTED]
- [[.scan()_2]] - `method` [EXTRACTED]
- [[.scan_response()_1]] - `method` [EXTRACTED]
- [[.setup_method()_1]] - `calls` [EXTRACTED]
- [[.test_custom_config()_1]] - `calls` [EXTRACTED]
- [[.test_no_canaries()]] - `calls` [EXTRACTED]
- [[.test_scan_response_no_block_when_block_disabled()]] - `calls` [EXTRACTED]
- [[Any_13]] - `uses` [INFERRED]
- [[Clock_1]] - `uses` [INFERRED]
- [[EdgeService]] - `uses` [INFERRED]
- [[EdgeStore_3]] - `uses` [INFERRED]
- [[Facade_1]] - `uses` [INFERRED]
- [[FakeFacade]] - `uses` [INFERRED]
- [[MemoryTokenStorage]] - `uses` [INFERRED]
- [[TestAuditRecord]] - `uses` [INFERRED]
- [[TestCanaryTripwire]] - `uses` [INFERRED]
- [[TestCommandCenterStats]] - `uses` [INFERRED]
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
- [[TestMonitorMode]] - `uses` [INFERRED]
- [[TestT1ToolAbuse]] - `uses` [INFERRED]
- [[TestT2Exfiltration]] - `uses` [INFERRED]
- [[TestT3Writes]] - `uses` [INFERRED]
- [[TestT4AuthN]] - `uses` [INFERRED]
- [[TestT9Abuse]] - `uses` [INFERRED]
- [[TestToolListing]] - `uses` [INFERRED]
- [[VendorProfile_3]] - `uses` [INFERRED]
- [[_BrokenOutputCanary]] - `uses` [INFERRED]
- [[_BrokenSanitizer]] - `uses` [INFERRED]
- [[build_edge_service()]] - `calls` [EXTRACTED]
- [[canary_tripwire.py]] - `contains` [EXTRACTED]
- [[edge()_1]] - `calls` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[pipeline()_1]] - `calls` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[service.py]] - `imports` [EXTRACTED]
- [[stack()]] - `calls` [EXTRACTED]
- [[test_canary_tripwire.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_25