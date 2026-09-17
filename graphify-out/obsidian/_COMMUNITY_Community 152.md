---
type: community
cohesion: 0.06
members: 43
---

# Community 152

**Cohesion:** 0.06 - loosely connected
**Members:** 43 nodes

## Members
- [[A homoglyph-obfuscated injection is normalized-and-blocked inbound.      The pay]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A nested base64(base64(injection)) payload is peeled and blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A plain unencoded benign message is untouched by the encoding step.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Double-base64 encoded lower-ranked injection is caught (was top-5 only).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Fully percent-encoded injection is decoded-and-blocked on inbound.      The dete]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[If the encoding detector raises, non-owner traffic is blocked (fail-closed).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Ordinary base64 content with no injection indicators is forwarded.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Owner encoded-injection is audited and allowed, never blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Pipeline wired with the guards relevant to inbound encoding defence.      No Tru]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[_make_pipeline()_1]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[`_check_encoded_content` now matches rules beyond the old top-5 slice.      Fail]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[`_detect_encoded_injection` matches rules beyond the old top-6 slice.      `jail]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[base64-wrapped DAN injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[hex-encoded injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[hex-encoded lower-ranked injection is caught by the full ruleset.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 decode is NOT applied to benign prose (no injection indicators).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 layer is surfaced when the decoded text reveals injection language.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-looking prose with no injection indicators is left alone.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-obfuscated injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_decodes_rot13_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
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
- [[test_prompt_guard_double_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_prompt_guard_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_ws_e_rt2_inbound_encoding.py]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_152
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Canary Tripwire]]
- 5 edges to [[_COMMUNITY_Community 101]]
- 4 edges to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 4 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 2 edges to [[_COMMUNITY_Tool Result Sanitizer & XML Injection Filtering]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 1 edge to [[_COMMUNITY_Community 109]]

## Top bridge nodes
- [[test_ws_e_rt2_inbound_encoding.py]] - degree 31, connects to 7 communities
- [[_make_pipeline()_1]] - degree 20, connects to 6 communities
- [[test_encoding_detector_decodes_rot13_injection()]] - degree 3, connects to 1 community
- [[test_encoding_detector_rot13_empty_text()]] - degree 3, connects to 1 community
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - degree 3, connects to 1 community