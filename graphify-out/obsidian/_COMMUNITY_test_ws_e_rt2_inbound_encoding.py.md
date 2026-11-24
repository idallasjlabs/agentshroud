---
type: community
members: 36
---

# test_ws_e_rt2_inbound_encoding.py

**Members:** 36 nodes

## Members
- [[A homoglyph-obfuscated injection is normalized-and-blocked inbound. The payload…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A nested base64(base64(injection)) payload is peeled and blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[A plain unencoded benign message is untouched by the encoding step.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Double-base64 encoded lower-ranked injection is caught (was top-5 only).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Fully percent-encoded injection is decoded-and-blocked on inbound. The…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[If the encoding detector raises, non-owner traffic is blocked (fail-closed).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Ordinary base64 content with no injection indicators is forwarded.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Owner encoded-injection is audited and allowed, never blocked.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Pipeline wired with the guards relevant to inbound encoding defence. No…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[WS-E RT-2 — Inbound encoding bypass (HIGH) regression tests. Before this fix an…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[_make_pipeline()_4]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[`_check_encoded_content` now matches rules beyond the old top-5 slice. Failing-…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[`_detect_encoded_injection` matches rules beyond the old top-6 slice.…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[analyze()_1]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[asyncio_89]] - code
- [[base64-wrapped DAN injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[hex-encoded injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[hex-encoded lower-ranked injection is caught by the full ruleset.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-looking prose with no injection indicators is left alone.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13-obfuscated injection is decoded-and-blocked on the inbound path.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
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
- [[test_ws_e_rt2_inbound_encoding.py]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ws_e_rt2_inbound_encodingpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_lifespan.py]]
- 8 edges to [[_COMMUNITY_EncodingDetector]]
- 7 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_test_encoding_detector_decodes_rot13_injection]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[test_ws_e_rt2_inbound_encoding.py]] - degree 38, connects to 8 communities
- [[_make_pipeline()_4]] - degree 19, connects to 4 communities
- [[test_inbound_encoding_detector_error_fails_closed()]] - degree 6, connects to 1 community
- [[test_inbound_base64_injection_blocked()]] - degree 5, connects to 1 community
- [[test_inbound_owner_encoded_injection_allowed()]] - degree 5, connects to 1 community
