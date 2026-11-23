---
type: community
members: 65
---

# test_e2e_watchtower.py

**Members:** 65 nodes

## Members
- [[dot-check_response()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-sanitize()_1]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_agents_process_independently()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_base64_content_decoded()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_benign_message_passes()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_blocked_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_canary_token_triggers_block()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_classic_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_clean_response_not_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_clean_response_passes_unchanged()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_credit_card_stripped_from_response()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_cross_context_injection_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_email_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_encoding_detector_is_wired()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_forwarded_message_has_audit_entry()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_jailbreak_blocked()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_low_trust_cannot_delete_file()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_phone_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_pii_from_agent_a_not_in_agent_b_audit()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_ssn_redacted()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_trusted_agent_can_send_message()]] - code - gateway/tests/test_e2e_watchtower.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Batch F1 — v0.8.0 Watchtower E2E Test Suite (10 enforcement scenarios). These…]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Blocking agent A does not affect agent B's processing.]] - rationale - gateway/tests/test_e2e_watchtower.py
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
- [[Owner messages should NOT be blocked when security module crashes (owner…]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[PII redacted for agent A does not leak into agent B's audit trail.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes…]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Pipeline must BLOCK (not pass through) when OutputCanary crashes for non-owner.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Response containing base64-encoded payload is decoded by the pipeline.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Sanitizer that always crashes — simulates module failure.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[TestE2E01PromptGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E02InboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E03OutboundPIIRedaction]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E04ContextGuardBlocking]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E05CanaryTripwire]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E06EncodingBypassDetection]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E07TrustEnforcement]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E08AuditChainIntegrity]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestE2E09SessionIsolation]] - code - gateway/tests/test_e2e_watchtower.py
- [[_BrokenOutputCanary]] - code - gateway/tests/test_e2e_watchtower.py
- [[_BrokenSanitizer]] - code - gateway/tests/test_e2e_watchtower.py
- [[asyncio_9]] - code
- [[fixture_15]] - code
- [[pii_config()]] - code - gateway/tests/test_e2e_watchtower.py
- [[pipeline()]] - code - gateway/tests/test_e2e_watchtower.py
- [[sanitizer()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_e2e_watchtower.py]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_fails_closed_on_output_canary_error()]] - code - gateway/tests/test_e2e_watchtower.py
- [[test_pipeline_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_e2e_watchtower.py
- [[trust_manager()]] - code - gateway/tests/test_e2e_watchtower.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2e_watchtowerpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_SecurityPipeline]]
- 5 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_CanaryTripwire]]
- 3 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[test_e2e_watchtower.py]] - degree 39, connects to 13 communities
- [[pipeline()]] - degree 7, connects to 5 communities
- [[trust_manager()]] - degree 4, connects to 2 communities
- [[TestE2E01PromptGuardBlocking]] - degree 6, connects to 1 community
- [[TestE2E08AuditChainIntegrity]] - degree 6, connects to 1 community
