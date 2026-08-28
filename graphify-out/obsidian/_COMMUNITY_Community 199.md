---
type: community
cohesion: 0.08
members: 36
---

# Community 199

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[.__init__()_77]] - code - gateway/security/encoding_detector.py
- [[.analyze()_1]] - code - gateway/security/encoding_detector.py
- [[.decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[.decode_hex()]] - code - gateway/security/encoding_detector.py
- [[.decode_rot13()]] - code - gateway/security/encoding_detector.py
- [[.decode_url()]] - code - gateway/security/encoding_detector.py
- [[.replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[.setup_method()_5]] - code - gateway/tests/test_encoding_detector.py
- [[.strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[.test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_empty_input()_1]] - code - gateway/tests/test_encoding_detector.py
- [[.test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_short_base64_not_flagged()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a]] - rationale - gateway/security/encoding_detector.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[The check_rot13 config flag gates the rot13 layer.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
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
TABLE source_file, type FROM #community/Community_199
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 8 edges to [[_COMMUNITY_Community 47]]
- 4 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 2 edges to [[_COMMUNITY_Community 46]]
- 2 edges to [[_COMMUNITY_Community 116]]
- 1 edge to [[_COMMUNITY_Community 45]]
- 1 edge to [[_COMMUNITY_Community 137]]

## Top bridge nodes
- [[EncodingDetector]] - degree 45, connects to 4 communities
- [[encoding_detector.py]] - degree 8, connects to 3 communities
- [[EncodingConfig]] - degree 8, connects to 2 communities
- [[test_encoding_detector_rot13_can_be_disabled()]] - degree 4, connects to 1 community
- [[test_encoding_detector_decodes_rot13_injection()]] - degree 3, connects to 1 community