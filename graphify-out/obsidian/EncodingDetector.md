---
source_file: "gateway/security/encoding_detector.py"
type: "code"
community: "Canary Tripwire"
location: "L68"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Canary_Tripwire
---

# EncodingDetector

## Connections
- [[dot-__init__()_94]] - `method` [EXTRACTED]
- [[dot-analyze()]] - `method` [EXTRACTED]
- [[dot-decode_base64_segments()]] - `method` [EXTRACTED]
- [[dot-decode_hex()]] - `method` [EXTRACTED]
- [[dot-decode_rot13()]] - `method` [EXTRACTED]
- [[dot-decode_url()]] - `method` [EXTRACTED]
- [[dot-replace_homoglyphs()]] - `method` [EXTRACTED]
- [[dot-setup_method()_22]] - `calls` [EXTRACTED]
- [[dot-strip_zero_width()]] - `method` [EXTRACTED]
- [[dot-test_config_disable_base64()]] - `calls` [EXTRACTED]
- [[PIISanitizer_3]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
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
- [[_make_pipeline()_1]] - `calls` [EXTRACTED]
- [[encoding_detector.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[pipeline()_1]] - `calls` [EXTRACTED]
- [[run()_4]] - `calls` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector_decodes_rot13_injection()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_can_be_disabled()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_empty_text()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - `calls` [EXTRACTED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Canary_Tripwire