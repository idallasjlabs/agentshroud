---
type: community
members: 35
---

# EncodingDetector

**Members:** 35 nodes

## Members
- [[dot-__init__()_144]] - code - gateway/security/encoding_detector.py
- [[dot-analyze()_2]] - code - gateway/security/encoding_detector.py
- [[dot-decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_hex()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_rot13()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_url()]] - code - gateway/security/encoding_detector.py
- [[dot-replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[dot-setup_method()_25]] - code - gateway/tests/test_encoding_detector.py
- [[dot-strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[dot-test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_short_base64_not_flagged()_1]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Decode rot13-obfuscated injection payloads. rot13 is self-inverse and applies…]] - rationale - gateway/security/encoding_detector.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[The check_rot13 config flag gates the rot13 layer.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[replacer()]] - code - gateway/security/encoding_detector.py
- [[replacer()_1]] - code - gateway/security/encoding_detector.py
- [[replacer()_2]] - code - gateway/security/encoding_detector.py
- [[rot13 decode is NOT applied to benign prose (no injection indicators).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector.py]] - code - gateway/tests/test_encoding_detector.py
- [[test_encoding_detector_rot13_can_be_disabled()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EncodingDetector
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 7 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 2 edges to [[_COMMUNITY_run]]
- 2 edges to [[_COMMUNITY_test_encoding_detector_decodes_rot13_injection]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EncodingDetector]] - degree 35, connects to 9 communities
- [[encoding_detector.py]] - degree 10, connects to 4 communities
- [[EncodingConfig]] - degree 7, connects to 1 community
- [[test_encoding_detector_rot13_can_be_disabled()]] - degree 4, connects to 1 community
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - degree 3, connects to 1 community
