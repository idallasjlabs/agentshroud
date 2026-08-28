---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "code"
community: "Community 47"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_47
---

# test_ws_e_rt2_inbound_encoding.py

## Connections
- [[EncodingConfig]] - `imports` [EXTRACTED]
- [[EncodingDetector]] - `references` [EXTRACTED]
- [[InjectionAction]] - `imports` [EXTRACTED]
- [[PIIConfig]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[PipelineAction]] - `imports` [EXTRACTED]
- [[PromptGuard]] - `references` [EXTRACTED]
- [[SecurityPipeline]] - `references` [EXTRACTED]
- [[ToolResultInjectionScanner]] - `references` [EXTRACTED]
- [[_make_pipeline()_4]] - `contains` [EXTRACTED]
- [[test_encoding_detector_decodes_rot13_injection()]] - `contains` [EXTRACTED]
- [[test_encoding_detector_rot13_can_be_disabled()]] - `contains` [EXTRACTED]
- [[test_encoding_detector_rot13_empty_text()]] - `contains` [EXTRACTED]
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - `contains` [EXTRACTED]
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - `contains` [EXTRACTED]
- [[test_inbound_base64_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_benign_base64_not_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_benign_rot13_prose_not_decoded_or_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_encoding_detector_error_fails_closed()]] - `contains` [EXTRACTED]
- [[test_inbound_hex_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_nested_base64_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_owner_encoded_injection_allowed()]] - `contains` [EXTRACTED]
- [[test_inbound_plain_benign_message_not_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_rot13_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_unicode_homoglyph_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_inbound_url_encoded_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_prompt_guard_double_encoded_uses_full_ruleset()]] - `contains` [EXTRACTED]
- [[test_prompt_guard_encoded_check_uses_full_ruleset()]] - `contains` [EXTRACTED]
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - `contains` [EXTRACTED]
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - `contains` [EXTRACTED]
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_47