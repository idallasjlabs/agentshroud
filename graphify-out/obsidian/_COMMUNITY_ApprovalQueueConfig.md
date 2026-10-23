---
type: community
cohesion: 0.03
members: 93
---

# ApprovalQueueConfig

**Cohesion:** 0.03 - loosely connected
**Members:** 93 nodes

## Members
- [[dot-__init__()_151]] - code - gateway/security/canary_tripwire.py
- [[dot-_check_encoded()]] - code - gateway/security/canary_tripwire.py
- [[dot-_check_plain()]] - code - gateway/security/canary_tripwire.py
- [[dot-_normalize()]] - code - gateway/security/canary_tripwire.py
- [[dot-_record()_1]] - code - gateway/security/canary_tripwire.py
- [[dot-check_response()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-detection_count()]] - code - gateway/security/canary_tripwire.py
- [[dot-register_canary()]] - code - gateway/security/canary_tripwire.py
- [[dot-sanitize()_4]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-scan()_4]] - code - gateway/security/canary_tripwire.py
- [[dot-scan_response()_1]] - code - gateway/security/canary_tripwire.py
- [[dot-setup_method()_24]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_agents_process_independently()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_api_key_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_base64_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_base64_content_decoded()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_benign_message_passes()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_canary_token_triggers_block()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_case_insensitive()_3]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_classic_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_clean_response_not_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_code_word_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_counter_increments()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_credit_card_stripped_from_response()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_cross_context_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_custom_config()_3]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_email_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_empty_input()_2]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_encoding_detector_is_wired()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_jailbreak_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_low_trust_cannot_delete_file()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_no_canaries()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_normal_content_passes()_1]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_phone_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_pii_from_agent_a_not_in_agent_b_audit()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_plain_canary_detected()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_reversed_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_rot13_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_blocks_on_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_no_block_when_block_disabled()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_passes_clean_text()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_records_scan_method()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_scan_response_returns_tripwire_response()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_spaced_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_ssn_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_trusted_agent_can_send_message()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_url_encoded_canary()]] - code - gateway/tests/test_canary_tripwire.py
- [[dot-test_zero_width_bypass()]] - code - gateway/tests/test_canary_tripwire.py
- [[Blocking agent A does not affect agent B's processing.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Bridge result returned by scan_response() for pipeline compatibility.]] - rationale - gateway/security/canary_tripwire.py
- [[CanaryConfig_1]] - code - gateway/security/canary_tripwire.py
- [[CanaryResult_2]] - code - gateway/security/canary_tripwire.py
- [[CanaryTripwire]] - code - gateway/security/canary_tripwire.py
- [[E2E-01 PromptGuard blocks high-confidence injection payloads.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-02 Social security numbers and email are redacted before forwarding.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-03 PII in agent responses is stripped before delivery.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-04 ContextGuard detects session-level injection in multi-turn context.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-05 Canary tokens in responses trigger full block.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-06 Base64 and Unicode encoding bypasses are decoded and processed.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[E2E-07 Low-trust agent cannot perform high-risk actions.]] - rationale - gateway/tests/test_e2e_watchtower.py
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
- [[TestE2E09SessionIsolation]] - code - gateway/tests/test_e2e_watchtower.py
- [[TripwireResponse]] - code - gateway/security/canary_tripwire.py
- [[_BrokenOutputCanary]] - code - gateway/tests/test_e2e_watchtower.py
- [[_BrokenSanitizer]] - code - gateway/tests/test_e2e_watchtower.py
- [[canary_tripwire.py]] - code - gateway/security/canary_tripwire.py
- [[pipeline()_2]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_canary_tripwire.py]] - code - gateway/tests/test_canary_tripwire.py
- [[test_e2e_watchtower.py]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_output_canary_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_e2e_watchtower.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 23 edges to [[_COMMUNITY_socrouter.py]]
- 13 edges to [[_COMMUNITY_AuditChain]]
- 12 edges to [[_COMMUNITY_ContextGuard]]
- 12 edges to [[_COMMUNITY_PromptGuard]]
- 12 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 12 edges to [[_COMMUNITY_MCPPermissionManager]]
- 12 edges to [[_COMMUNITY_test_agent_cve_registry.py (2)]]
- 2 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_FileSandbox]]

## Top bridge nodes
- [[test_e2e_watchtower.py]] - degree 30, connects to 8 communities
- [[_BrokenSanitizer]] - degree 16, connects to 8 communities
- [[TestE2E01PromptGuardBlocking]] - degree 16, connects to 8 communities
- [[TestE2E02InboundPIIRedaction]] - degree 16, connects to 8 communities
- [[_BrokenOutputCanary]] - degree 15, connects to 8 communities
