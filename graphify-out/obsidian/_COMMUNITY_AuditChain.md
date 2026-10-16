---
type: community
cohesion: 0.04
members: 97
---

# AuditChain

**Cohesion:** 0.04 - loosely connected
**Members:** 97 nodes

## Members
- [[dot-__init__()_168]] - code - gateway/security/instruction_envelope.py
- [[dot-_compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[dot-_pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-sign()]] - code - gateway/security/instruction_envelope.py
- [[dot-test_blocked_request_decays_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_clean_request_does_not_touch_trust_score()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_missing_trust_manager_does_not_raise()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_outbound_filter_does_not_unbind()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-verify()_1]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - concept - gateway/tests/test_instruction_envelope.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[No trust_manager configured — the hook must no-op, not crash the         request]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner messages that would trip a guard are logged but never         blocked — re]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Regression filter_result was possibly-unbound in process_outbound when no     o]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[ScanResult_4]] - code - gateway/security/prompt_guard.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner.      Non-ow]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestOutboundFilterResultBinding]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_4]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[sign() + verify() should return True for unmodified content.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[skip_context_guard=True must prevent ContextGuard from running — used by Telegra]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[test_pipeline_unit.py]] - code - gateway/tests/test_pipeline_unit.py
- [[wrap_system_prompt() sets issuer='system' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_tool_result() sets issuer='toolname' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_PipelineAction]]
- 38 edges to [[_COMMUNITY_AgentTarget_2]]
- 21 edges to [[_COMMUNITY_TrustConfig]]
- 10 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 9 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 9 edges to [[_COMMUNITY_AsyncMock_1]]
- 9 edges to [[_COMMUNITY_InjectionAction]]
- 8 edges to [[_COMMUNITY_ContextSegment]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TestNewPatternsV080]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py_1]]
- 1 edge to [[_COMMUNITY_TestPathIsolationManager]]
- 1 edge to [[_COMMUNITY_Audit Ledger (SHA-256 hash only)_1]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger_1]]

## Top bridge nodes
- [[ThreatAction]] - degree 33, connects to 13 communities
- [[test_pipeline_unit.py]] - degree 31, connects to 6 communities
- [[_FakeAttack]] - degree 27, connects to 6 communities
- [[TestContextGuardInPipeline]] - degree 27, connects to 6 communities
- [[TestContextIntegrityInPipeline]] - degree 26, connects to 6 communities
