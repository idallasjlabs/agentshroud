---
source_file: "gateway/security/encoding_detector.py"
type: "code"
community: "SOC RBAC & Auth"
location: "L68"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# EncodingDetector

## Connections
- [[.__init__()_74]] - `method` [EXTRACTED]
- [[.analyze()_1]] - `method` [EXTRACTED]
- [[.decode_base64_segments()]] - `method` [EXTRACTED]
- [[.decode_hex()]] - `method` [EXTRACTED]
- [[.decode_rot13()]] - `method` [EXTRACTED]
- [[.decode_url()]] - `method` [EXTRACTED]
- [[.replace_homoglyphs()]] - `method` [EXTRACTED]
- [[.setup_method()_5]] - `calls` [EXTRACTED]
- [[.strip_zero_width()]] - `method` [EXTRACTED]
- [[.test_config_disable_base64()]] - `calls` [EXTRACTED]
- [[PIISanitizer_3]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
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
- [[TestEncodingDetector]] - `uses` [INFERRED]
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - `rationale_for` [EXTRACTED]
- [[_BrokenOutputCanary]] - `uses` [INFERRED]
- [[_BrokenSanitizer]] - `uses` [INFERRED]
- [[_make_full_pipeline()]] - `calls` [EXTRACTED]
- [[_make_pipeline()_4]] - `calls` [EXTRACTED]
- [[encoding_detector.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[pipeline()_1]] - `calls` [EXTRACTED]
- [[run()_3]] - `calls` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector_decodes_rot13_injection()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_can_be_disabled()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_empty_text()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - `calls` [EXTRACTED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_RBAC__Auth