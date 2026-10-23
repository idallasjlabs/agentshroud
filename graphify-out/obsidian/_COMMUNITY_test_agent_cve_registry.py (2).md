---
type: community
cohesion: 0.05
members: 68
---

# test_agent_cve_registry.py (2)

**Cohesion:** 0.05 - loosely connected
**Members:** 68 nodes

## Members
- [[dot-__init__()_190]] - code - gateway/security/encoding_detector.py
- [[dot-analyze()_1]] - code - gateway/security/encoding_detector.py
- [[dot-decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_hex()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_rot13()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_url()]] - code - gateway/security/encoding_detector.py
- [[dot-replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[dot-setup_method()_36]] - code - gateway/tests/test_encoding_detector.py
- [[dot-strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[dot-test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_empty_input()_3]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_short_base64_not_flagged()_1]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[A homoglyph-obfuscated injection is normalized-and-blocked inbound.      The pay]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A nested base64(base64(injection)) payload is peeled and blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A plain unencoded benign message is untouched by the encoding step.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a]] - rationale - gateway/security/encoding_detector.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Fully percent-encoded injection is decoded-and-blocked on inbound.      The dete]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[If the encoding detector raises, non-owner traffic is blocked (fail-closed).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Ordinary base64 content with no injection indicators is forwarded.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Owner encoded-injection is audited and allowed, never blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Pipeline wired with the guards relevant to inbound encoding defence.      No Tru]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[SecurityPipeline_2]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[The check_rot13 config flag gates the rot13 layer.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[_make_pipeline()_4]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[`_detect_encoded_injection` matches rules beyond the old top-6 slice.      `jail]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[base64-wrapped DAN injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[hex-encoded injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[hex-encoded lower-ranked injection is caught by the full ruleset.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 decode is NOT applied to benign prose (no injection indicators).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 layer is surfaced when the decoded text reveals injection language.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-looking prose with no injection indicators is left alone.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-obfuscated injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector.py]] - code - gateway/tests/test_encoding_detector.py
- [[test_encoding_detector_decodes_rot13_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_can_be_disabled()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_empty_text()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_base64_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_benign_base64_not_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_benign_rot13_prose_not_decoded_or_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_encoding_detector_error_fails_closed()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_hex_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_nested_base64_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_owner_encoded_injection_allowed()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_plain_benign_message_not_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_rot13_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_unicode_homoglyph_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_inbound_url_encoded_injection_blocked()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_ws_e_rt2_inbound_encoding.py]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_agent_cve_registrypy_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 8 edges to [[_COMMUNITY_Any]]
- 8 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 5 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[EncodingDetector]] - degree 43, connects to 7 communities
- [[test_ws_e_rt2_inbound_encoding.py]] - degree 31, connects to 6 communities
- [[SecurityPipeline_2]] - degree 10, connects to 6 communities
- [[_make_pipeline()_4]] - degree 20, connects to 5 communities
- [[encoding_detector.py]] - degree 7, connects to 3 communities
