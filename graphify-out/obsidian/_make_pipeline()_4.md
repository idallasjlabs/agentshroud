---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "code"
community: "SOC RBAC & Auth"
location: "L53"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# _make_pipeline()

## Connections
- [[EncodingDetector]] - `calls` [EXTRACTED]
- [[PIIConfig]] - `calls` [EXTRACTED]
- [[PIISanitizer]] - `calls` [EXTRACTED]
- [[Pipeline wired with the guards relevant to inbound encoding defence.      No Tru]] - `rationale_for` [EXTRACTED]
- [[PromptGuard]] - `calls` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[SecurityPipeline_2]] - `references` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `calls` [EXTRACTED]
- [[test_inbound_base64_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_benign_base64_not_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_benign_rot13_prose_not_decoded_or_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_encoding_detector_error_fails_closed()]] - `calls` [EXTRACTED]
- [[test_inbound_hex_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_nested_base64_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_owner_encoded_injection_allowed()]] - `calls` [EXTRACTED]
- [[test_inbound_plain_benign_message_not_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_rot13_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_unicode_homoglyph_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_inbound_url_encoded_injection_blocked()]] - `calls` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SOC_RBAC__Auth