---
source_file: "gateway/security/encoding_detector.py"
type: "code"
community: "Canary Tripwire"
location: "L43"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Canary_Tripwire
---

# EncodingConfig

## Connections
- [[dot-__init__()_94]] - `references` [EXTRACTED]
- [[dot-test_config_disable_base64()]] - `calls` [EXTRACTED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TestEncodingDetector]] - `uses` [INFERRED]
- [[encoding_detector.py]] - `contains` [EXTRACTED]
- [[test_encoding_detector.py]] - `imports` [EXTRACTED]
- [[test_encoding_detector_rot13_can_be_disabled()]] - `calls` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Canary_Tripwire