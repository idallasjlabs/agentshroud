---
type: community
members: 91
---

# MiddlewareManager (3)

**Members:** 91 nodes

## Members
- [[dot-__init__()_148]] - code - gateway/security/encoding_detector.py
- [[dot-analyze()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_hex()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_rot13()]] - code - gateway/security/encoding_detector.py
- [[dot-decode_url()]] - code - gateway/security/encoding_detector.py
- [[dot-replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[dot-setup_method()_30]] - code - gateway/tests/test_encoding_detector.py
- [[dot-strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[dot-test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_empty_input()_3]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_short_base64_not_flagged()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[dot-test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[Audit chain must detect tampering.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Build a SecurityPipeline with all guards wired up.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Cleartext injection is not re-rotated into noise (indicator already present).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Combined prompt injection + role override must be caught.]] - rationale - gateway/tests/test_redteam_probes.py
- [[ContextGuard must detect context window poisoning (massive payload).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Create a real PII sanitizer in regex mode (no spaCy).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a]] - rationale - gateway/security/encoding_detector.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector must detect base64 in outbound responses.]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingDetector must detect base64-encoded payloads on inbound.]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[Every pipeline operation must produce an audit chain entry.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Minimal approval queue mock that accepts items.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Non-owner collaborators must be blocked by prompt guard.]] - rationale - gateway/tests/test_redteam_probes.py
- [[One agent's session data must not leak to another.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Pipeline must refuse to start without PII sanitizer (fail-closed).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1 Agent exec must go through approval queue or be blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1b delete_file action must go through approval or be blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1c admin_action must require approval or be trust-blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6 EgressFilter must block non-allowlisted domains.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6b EgressFilter must block direct IP exfiltration.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6c EgressFilter must block internalprivate IP ranges.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9 PII sanitizer must redact SSN on inbound messages.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9b PII sanitizer must redact SSN on outbound responses.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9c PII sanitizer must redact credit card numbers.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9d PII sanitizer must redact email addresses on outbound.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must block classic 'ignore instructions' injection.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must block role-override injection.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must detect system prompt extraction attempts.]] - rationale - gateway/tests/test_redteam_probes.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[The check_rot13 config flag gates the rot13 layer.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Trust level must not allow exec from conversation alone.]] - rationale - gateway/tests/test_redteam_probes.py
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[_make_approval_queue()]] - code - gateway/tests/test_redteam_probes.py
- [[_make_full_pipeline()]] - code - gateway/tests/test_redteam_probes.py
- [[_make_pii_sanitizer()]] - code - gateway/tests/test_redteam_probes.py
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[pipeline()_2]] - code - gateway/tests/test_redteam_probes.py
- [[rot13 decode is NOT applied to benign prose (no injection indicators).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 layer is surfaced when the decoded text reveals injection language.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_admin_action_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_audit_chain_records_all_events()]] - code - gateway/tests/test_redteam_probes.py
- [[test_audit_chain_tamper_detection()]] - code - gateway/tests/test_redteam_probes.py
- [[test_combined_injection_techniques()]] - code - gateway/tests/test_redteam_probes.py
- [[test_context_poisoning_blocked()]] - code - gateway/tests/test_redteam_probes.py
- [[test_credit_card_redacted_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_internal_ip()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_ip_exfil()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_unknown_domain()]] - code - gateway/tests/test_redteam_probes.py
- [[test_email_redacted_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_encoding_detector.py]] - code - gateway/tests/test_encoding_detector.py
- [[test_encoding_detector_base64_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_encoding_detector_catches_base64_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_encoding_detector_decodes_rot13_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_can_be_disabled()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_empty_text()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_exec_delete_file_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_exec_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_non_owner_blocked_by_prompt_guard()]] - code - gateway/tests/test_redteam_probes.py
- [[test_pipeline_fails_closed_without_pii()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_extraction_attempt()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_ignore_instructions()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_role_override()]] - code - gateway/tests/test_redteam_probes.py
- [[test_redteam_probes.py]] - code - gateway/tests/test_redteam_probes.py
- [[test_session_isolation()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_trust_escalation_blocked()]] - code - gateway/tests/test_redteam_probes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_3
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_SecurityPipeline]]
- 14 edges to [[_COMMUNITY_PipelineAction]]
- 10 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_ContextSegment]]
- 3 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (5)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]

## Top bridge nodes
- [[test_redteam_probes.py]] - degree 40, connects to 9 communities
- [[_make_full_pipeline()]] - degree 20, connects to 7 communities
- [[EncodingDetector]] - degree 43, connects to 4 communities
- [[encoding_detector.py]] - degree 8, connects to 3 communities
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - degree 4, connects to 3 communities
