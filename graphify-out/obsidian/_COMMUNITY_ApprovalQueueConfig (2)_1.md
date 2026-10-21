---
type: community
members: 81
---

# ApprovalQueueConfig (2)

**Members:** 81 nodes

## Members
- [[dot-__init__()_152]] - code - gateway/security/instruction_envelope.py
- [[dot-_compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[dot-_pipeline_with_trust()]] - code - gateway/tests/test_pipeline_unit.py
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
- [[dot-test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_non_owner_block_does_not_emit_owner_bypass()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_audited_at_every_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_bypass_is_recorded_in_audit_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - code - gateway/tests/test_pipeline_unit.py
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
- [[dot-verify()]] - code - gateway/security/instruction_envelope.py
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
- [[Owner messages that would trip a guard are logged but never         blocked — re]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestTrustViolationRecording]] - code - gateway/tests/test_pipeline_unit.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_4]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[sign() + verify() should return True for unmodified content.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[skip_context_guard=True must prevent ContextGuard from running — used by Telegra]] - rationale - gateway/tests/test_pipeline_unit.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[wrap_system_prompt() sets issuer='system' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_tool_result() sets issuer='toolname' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_2
SORT file.name ASC
```

## Connections to other communities
- 47 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 17 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 7 edges to [[_COMMUNITY_api.py (2)]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 5 edges to [[_COMMUNITY_FetchOutcome]]
- 5 edges to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[_FakeAttack]] - degree 27, connects to 7 communities
- [[TestContextGuardInPipeline]] - degree 27, connects to 7 communities
- [[TestContextIntegrityInPipeline]] - degree 26, connects to 7 communities
- [[TestTrustViolationRecording]] - degree 23, connects to 7 communities
- [[TestEnvelopeSignerInPipeline]] - degree 22, connects to 7 communities
