---
type: community
cohesion: 0.05
members: 79
---

# Pipeline Action & Instruction Envelope

**Cohesion:** 0.05 - loosely connected
**Members:** 79 nodes

## Members
- [[.__init__()_68]] - code - gateway/security/instruction_envelope.py
- [[._compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[._make_vault_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[._passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.sign()]] - code - gateway/security/instruction_envelope.py
- [[.test_clean_message_passes()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_clean_response_passes_unchanged()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_context_guard_error_fails_closed()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_critical_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_detector_failure_fails_closed_for_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_generic_key_pattern_audited_but_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_high_injection_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_high_score_forwards_and_records()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_key_leak_increments_sanitized_stat_and_audits()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_lockdown_block_is_audited()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_lockdown_score_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_lockdown_score_blocks_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_context_guard_passes_through()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_scorer_leaves_result_unscored()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_repetition_attack_does_not_block()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_error_allows_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_error_fails_closed_non_owner()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_scorer_invoked_with_session_segments()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_skip_context_guard_bypasses_step0()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_stored_key_value_redacted_from_outbound()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_warn_zone_forwards()]] - code - gateway/tests/test_pipeline_unit.py
- [[.verify()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[0.3 ≤ score  0.6 warns but never blocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Minimal SecurityPipeline with a real PII sanitizer stub.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PipelineAction]] - code - gateway/proxy/pipeline.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[TestContextGuardInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestContextIntegrityInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[TestKeyLeakDetection_1]] - code - gateway/tests/test_pipeline_unit.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_FakeAttack]] - code - gateway/tests/test_pipeline_unit.py
- [[_FakeIntegrityScore]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_integrity_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[_make_pipeline()_1]] - code - gateway/tests/test_pipeline_unit.py
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
TABLE source_file, type FROM #community/Pipeline_Action__Instruction_Envelope
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 24 edges to [[_COMMUNITY_Module Group 63]]
- 10 edges to [[_COMMUNITY_Module Group 177]]
- 4 edges to [[_COMMUNITY_Module Group 74]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 72]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Module Group 76]]
- 1 edge to [[_COMMUNITY_Module Group 184]]

## Top bridge nodes
- [[PipelineAction]] - degree 44, connects to 10 communities
- [[EnvelopeSigner]] - degree 25, connects to 2 communities
- [[test_pipeline_unit.py]] - degree 19, connects to 2 communities
- [[TestContextIntegrityInPipeline]] - degree 19, connects to 2 communities
- [[TestContextGuardInPipeline]] - degree 17, connects to 2 communities
