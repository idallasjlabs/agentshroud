---
type: community
members: 37
---

# test_agent_cve_registry.py (2)

**Members:** 37 nodes

## Members
- [[dot-__init__()_82]] - code - gateway/security/encoding_detector.py
- [[dot-analyze()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_hex()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_rot13()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_url()]] - code - gateway/security/encoding_detector.py
- [[dot-replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[dot-setup_method()_14]] - code - gateway/tests/test_encoding_detector.py
- [[dot-strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[dot-test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_short_base64_not_flagged()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a]] - rationale - gateway/security/encoding_detector.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[The check_rot13 config flag gates the rot13 layer.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[rot13 decode is NOT applied to benign prose (no injection indicators).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 layer is surfaced when the decoded text reveals injection language.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector.py]] - code - gateway/tests/test_encoding_detector.py
- [[test_encoding_detector_decodes_rot13_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_can_be_disabled()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_empty_text()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_agent_cve_registrypy_2
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[EncodingDetector]] - degree 43, connects to 4 communities
- [[encoding_detector.py]] - degree 7, connects to 3 communities
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - degree 4, connects to 3 communities
- [[EncodingConfig]] - degree 8, connects to 1 community
- [[test_encoding_detector_rot13_can_be_disabled()]] - degree 4, connects to 1 community
