---
type: community
cohesion: 0.02
members: 145
---

# Security Pipeline & Audit Chain

**Cohesion:** 0.02 - loosely connected
**Members:** 145 nodes

## Members
- [[.__init__()_25]] - code - gateway/proxy/pipeline.py
- [[.__init__()_61]] - code - gateway/security/encoding_detector.py
- [[.__len__()_1]] - code - gateway/proxy/pipeline.py
- [[.analyze()_1]] - code - gateway/security/encoding_detector.py
- [[.append()]] - code - gateway/proxy/pipeline.py
- [[.append_block()]] - code - gateway/proxy/pipeline.py
- [[.check_response()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[.decode_base64_segments()]] - code - gateway/security/encoding_detector.py
- [[.decode_hex()]] - code - gateway/security/encoding_detector.py
- [[.decode_url()]] - code - gateway/security/encoding_detector.py
- [[.entries()_1]] - code - gateway/proxy/pipeline.py
- [[.get_stats()_6]] - code - gateway/proxy/pipeline.py
- [[.last_hash()_1]] - code - gateway/proxy/pipeline.py
- [[.process_inbound()]] - code - gateway/proxy/pipeline.py
- [[.process_outbound()]] - code - gateway/proxy/pipeline.py
- [[.replace_homoglyphs()]] - code - gateway/security/encoding_detector.py
- [[.sanitize()_2]] - code - gateway/tests/test_e2e_watchtower.py
- [[.set_global_mode()]] - code - gateway/proxy/pipeline.py
- [[.setup_method()_5]] - code - gateway/tests/test_encoding_detector.py
- [[.strip_zero_width()]] - code - gateway/security/encoding_detector.py
- [[.test_agents_process_independently()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_base64_content_decoded()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_base64_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_benign_message_passes()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_blocked_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_canary_token_triggers_block()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_classic_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_clean_response_not_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_clean_response_passes_unchanged()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_config_disable_base64()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_credit_card_stripped_from_response()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_cross_context_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_default_window_is_10k()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_different_content_different_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_email_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_empty_input()_1]] - code - gateway/tests/test_encoding_detector.py
- [[.test_encoding_detector_is_wired()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_forwarded_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_homoglyph_replaced()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_jailbreak_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_low_trust_cannot_delete_file()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_metadata()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_nested_encoding()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_phone_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_pii_from_agent_a_not_in_agent_b_audit()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_pipeline_raises_with_only_prompt_guard()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_pipeline_raises_without_pii_sanitizer()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_plain_text_no_detection()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_short_base64_not_flagged()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_ssn_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_trusted_agent_can_send_message()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_url_encoding_detected()]] - code - gateway/tests/test_encoding_detector.py
- [[.test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_chain_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_valid()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_zero_width_stripped()]] - code - gateway/tests/test_encoding_detector.py
- [[.to_dict()_1]] - code - gateway/proxy/pipeline.py
- [[.total_appended()_1]] - code - gateway/proxy/pipeline.py
- [[.verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[.verify_chain()_1]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_16]] - code - gateway/proxy/pipeline.py
- [[Append to the chain with guaranteed SQLite persistence.          Used exclusivel]] - rationale - gateway/proxy/pipeline.py
- [[Attempting to create a pipeline with no PII sanitizer raises RuntimeError.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[Blocking agent A does not affect agent B's processing.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[DecodedLayer]] - code - gateway/security/encoding_detector.py
- [[E2E-01 PromptGuard blocks high-confidence injection payloads.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-02 Social security numbers and email are redacted before forwarding.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-03 PII in agent responses is stripped before delivery.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-04 ContextGuard detects session-level injection in multi-turn context.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-05 Canary tokens in responses trigger full block.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-06 Base64 and Unicode encoding bypasses are decoded and processed.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-07 Low-trust agent cannot perform high-risk actions.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-08 Every pipeline event — block or forward — produces an audit entry.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-09 Two agents process independently with no cross-contamination.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Encoding detector is active in the pipeline.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[EncodingConfig]] - code - gateway/security/encoding_detector.py
- [[EncodingDetector]] - code - gateway/security/encoding_detector.py
- [[EncodingResult]] - code - gateway/security/encoding_detector.py
- [[Even with PromptGuard, pipeline refuses to start without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[If an agent response contains a registered canary value, block it.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Injecting a system-level override via a follow-up message is blocked.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Main security pipeline that all messages pass through.      Wires together Prom]] - rationale - gateway/proxy/pipeline.py
- [[OutputCanary that always crashes.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Owner messages should NOT be blocked when security module crashes (owner exempti]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[PII redacted for agent A does not leak into agent B's audit trail.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when OutputCanary crashes for non-owner.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Response containing base64-encoded payload is decoded by the pipeline.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[Sanitizer that always crashes — simulates module failure.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[SecurityPipeline]] - code - gateway/proxy/pipeline.py
- [[Set global observatory mode for all security modules.          Args]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[TestE2E01PromptGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E02InboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E03OutboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E04ContextGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E05CanaryTripwire]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E06EncodingBypassDetection]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E07TrustEnforcement]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E08AuditChainIntegrity]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E09SessionIsolation]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E10FailClosed]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestEncodingDetector]] - code - gateway/tests/test_encoding_detector.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify the integrity of the retained hash-chain window.          When the bounde]] - rationale - gateway/proxy/pipeline.py
- [[_BrokenOutputCanary]] - code - gateway/tests/test_e2e_watchtower.py
- [[_BrokenSanitizer]] - code - gateway/tests/test_e2e_watchtower.py
- [[audit_chain()]] - code - gateway/tests/test_web_proxy.py
- [[encoding_detector.py]] - code - gateway/security/encoding_detector.py
- [[pii_config()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[pipeline()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[sanitizer()_2]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_audit_chain_empty_valid()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_single_entry()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_e2e_watchtower.py]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_encoding_detector.py]] - code - gateway/tests/test_encoding_detector.py
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_output_canary_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_e2e_watchtower.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Pipeline__Audit_Chain
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 34 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 29 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 18 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 17 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 16 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 14 edges to [[_COMMUNITY_Module Group 115]]
- 10 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 8 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 7 edges to [[_COMMUNITY_Module Group 72]]
- 6 edges to [[_COMMUNITY_Module Group 126]]
- 6 edges to [[_COMMUNITY_Module Group 63]]
- 5 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 4 edges to [[_COMMUNITY_Module Group 76]]
- 3 edges to [[_COMMUNITY_Module Group 177]]
- 3 edges to [[_COMMUNITY_Module Group 233]]
- 2 edges to [[_COMMUNITY_Module Group 98]]
- 2 edges to [[_COMMUNITY_Module Group 92]]
- 2 edges to [[_COMMUNITY_Module Group 184]]
- 2 edges to [[_COMMUNITY_Module Group 322]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 505]]
- 1 edge to [[_COMMUNITY_Module Group 448]]
- 1 edge to [[_COMMUNITY_Module Group 340]]
- 1 edge to [[_COMMUNITY_Module Group 488]]
- 1 edge to [[_COMMUNITY_Module Group 336]]
- 1 edge to [[_COMMUNITY_Module Group 489]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[SecurityPipeline]] - degree 85, connects to 20 communities
- [[AuditChain]] - degree 78, connects to 9 communities
- [[test_e2e_watchtower.py]] - degree 30, connects to 6 communities
- [[_BrokenSanitizer]] - degree 16, connects to 6 communities
- [[TestE2E01PromptGuardBlocking]] - degree 16, connects to 6 communities