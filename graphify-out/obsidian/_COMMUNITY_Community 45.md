---
type: community
members: 99
---

# Community 45

**Members:** 99 nodes

## Members
- [[.__init__()_60]] - code - gateway/security/canary_tripwire.py
- [[._check_encoded()]] - code - gateway/security/canary_tripwire.py
- [[._check_plain()]] - code - gateway/security/canary_tripwire.py
- [[._normalize()]] - code - gateway/security/canary_tripwire.py
- [[._record()]] - code - gateway/security/canary_tripwire.py
- [[.detection_count()]] - code - gateway/security/canary_tripwire.py
- [[.register_canary()]] - code - gateway/security/canary_tripwire.py
- [[.scan()_2]] - code - gateway/security/canary_tripwire.py
- [[.scan_response()_1]] - code - gateway/security/canary_tripwire.py
- [[.setup_method()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_agents_process_independently()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_base64_content_decoded()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_benign_message_passes()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_blocked_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_canary_token_triggers_block()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_case_insensitive()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_classic_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_clean_response_not_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_clean_response_passes_unchanged()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_credit_card_stripped_from_response()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_cross_context_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_custom_config()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_email_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_empty_input()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_encoding_detector_is_wired()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_forwarded_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_jailbreak_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_low_trust_cannot_delete_file()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_no_canaries()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_normal_content_passes()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_phone_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_pii_from_agent_a_not_in_agent_b_audit()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_plain_canary_detected()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_reversed_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_rot13_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_blocks_on_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_no_block_when_block_disabled()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_passes_clean_text()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_records_scan_method()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_scan_response_returns_tripwire_response()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_spaced_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_ssn_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_trusted_agent_can_send_message()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_url_encoded_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[.test_zero_width_bypass()]] - code - gateway/tests/test_canary_tripwire.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Blocking agent A does not affect agent B's processing.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Bridge result returned by scan_response() for pipeline compatibility.]] - rationale - gateway/security/canary_tripwire.py
- [[CanaryConfig]] - code - gateway/security/canary_tripwire.py
- [[CanaryResult_1]] - code - gateway/security/canary_tripwire.py
- [[CanaryTripwire]] - code - gateway/security/canary_tripwire.py
- [[E2E-01 PromptGuard blocks high-confidence injection payloads.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-02 Social security numbers and email are redacted before forwarding.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-03 PII in agent responses is stripped before delivery.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-04 ContextGuard detects session-level injection in multi-turn context.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-05 Canary tokens in responses trigger full block.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-06 Base64 and Unicode encoding bypasses are decoded and processed.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-07 Low-trust agent cannot perform high-risk actions.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-08 Every pipeline event — block or forward — produces an audit entry.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-09 Two agents process independently with no cross-contamination.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Encoding detector is active in the pipeline.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[If an agent response contains a registered canary value, block it.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Injecting a system-level override via a follow-up message is blocked.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[OutputCanary that always crashes.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Owner messages should NOT be blocked when security module crashes (owner exempti]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[PII redacted for agent A does not leak into agent B's audit trail.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when OutputCanary crashes for non-owner.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline-compatible bridge scan response text and return TripwireResponse.]] - rationale - gateway/security/canary_tripwire.py
- [[Register a new canary value at runtime for dynamic tripwire testing.]] - rationale - gateway/security/canary_tripwire.py
- [[Response containing base64-encoded payload is decoded by the pipeline.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Sanitizer that always crashes — simulates module failure.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[TestCanaryTripwire]] - code - gateway/tests/test_canary_tripwire.py
- [[TestE2E01PromptGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E02InboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E03OutboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E04ContextGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E05CanaryTripwire]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E06EncodingBypassDetection]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E07TrustEnforcement]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E08AuditChainIntegrity]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E09SessionIsolation]] - code - gateway/tests/test_e2e_watchtower.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[_BrokenOutputCanary]] - code - gateway/tests/test_e2e_watchtower.py
- [[_BrokenSanitizer]] - code - gateway/tests/test_e2e_watchtower.py
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[pii_config()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[pipeline()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[sanitizer()_2]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py
- [[test_e2e_watchtower.py]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_output_canary_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_e2e_watchtower.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_45
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_Community 24]]
- 26 edges to [[_COMMUNITY_Community 7]]
- 25 edges to [[_COMMUNITY_Community 11]]
- 15 edges to [[_COMMUNITY_Community 22]]
- 13 edges to [[_COMMUNITY_Community 72]]
- 13 edges to [[_COMMUNITY_Community 84]]
- 12 edges to [[_COMMUNITY_Community 63]]
- 2 edges to [[_COMMUNITY_Community 26]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 2030]]
- 1 edge to [[_COMMUNITY_Community 984]]

## Top bridge nodes
- [[_BrokenSanitizer]] - degree 16, connects to 8 communities
- [[_BrokenOutputCanary]] - degree 15, connects to 8 communities
- [[test_e2e_watchtower.py]] - degree 30, connects to 7 communities
- [[TestE2E01PromptGuardBlocking]] - degree 16, connects to 7 communities
- [[TestE2E02InboundPIIRedaction]] - degree 16, connects to 7 communities