---
source_file: "gateway/security/encoding_detector.py"
type: "code"
community: "test_ws_e_rt2_inbound_encoding.py"
location: "L68"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_ws_e_rt2_inbound_encodingpy
---

# EncodingDetector

## Connections
- [[dot-__init__()_228]] - `method` [EXTRACTED]
- [[dot-analyze()_2]] - `method` [EXTRACTED]
- [[dot-decode_base64_segments()]] - `method` [EXTRACTED]
- [[dot-decode_hex()]] - `method` [EXTRACTED]
- [[dot-decode_rot13()]] - `method` [EXTRACTED]
- [[dot-decode_url()]] - `method` [EXTRACTED]
- [[dot-replace_homoglyphs()]] - `method` [EXTRACTED]
- [[dot-setup_method()_38]] - `calls` [EXTRACTED]
- [[dot-strip_zero_width()]] - `method` [EXTRACTED]
- [[dot-test_config_disable_base64()]] - `calls` [EXTRACTED]
- [[TestEncodingDetector]] - `uses` [INFERRED]
- [[_make_full_pipeline()]] - `calls` [EXTRACTED]
- [[_make_pipeline()_4]] - `calls` [EXTRACTED]
- [[build_edge_service()]] - `calls` [EXTRACTED]
- [[edge()]] - `uses` [INFERRED]
- [[encoding_detector.py]] - `contains` [EXTRACTED]
- [[enforcement-audit-script.py]] - `imports` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[pipeline()]] - `uses` [INFERRED]
- [[run()_1]] - `calls` [EXTRACTED]
- [[service.py]] - `imports` [EXTRACTED]
- [[stack()]] - `uses` [INFERRED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector_decodes_rot13_injection()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_can_be_disabled()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_empty_text()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - `calls` [EXTRACTED]
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - `calls` [EXTRACTED]
- [[test_inbound_encoding_detector_error_fails_closed()]] - `uses` [INFERRED]
- [[test_redteam_probes.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_ws_e_rt2_inbound_encodingpy
