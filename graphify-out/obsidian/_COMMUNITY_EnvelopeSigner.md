---
type: community
cohesion: 0.07
members: 41
---

# EnvelopeSigner

**Cohesion:** 0.07 - loosely connected
**Members:** 41 nodes

## Members
- [[dot-__init__()_76]] - code - gateway/security/instruction_envelope.py
- [[dot-_compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[dot-sign()]] - code - gateway/security/instruction_envelope.py
- [[dot-test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_metadata_in_audit_entry()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_no_signer_leaves_envelope_empty()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_signer_failure_never_blocks()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tool_result_uses_wrap_tool_result()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-verify()]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - concept - gateway/tests/test_instruction_envelope.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[EnvelopeSigner must attest outbound responses — C46 wiring.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[TestEnvelopeSignerInPipeline]] - code - gateway/tests/test_pipeline_unit.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_make_signer_pipeline()]] - code - gateway/tests/test_pipeline_unit.py
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[sign() + verify() should return True for unmodified content.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[wrap_system_prompt() sets issuer='system' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_tool_result() sets issuer='toolname' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EnvelopeSigner
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 7 edges to [[_COMMUNITY__FakeAttack]]
- 5 edges to [[_COMMUNITY_AuditChain]]
- 5 edges to [[_COMMUNITY_KeyVault]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_InjectionAction]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[TestEnvelopeSignerInPipeline]] - degree 22, connects to 8 communities
- [[EnvelopeSigner]] - degree 30, connects to 5 communities
- [[InstructionEnvelope]] - degree 22, connects to 4 communities
- [[_make_signer_pipeline()]] - degree 7, connects to 3 communities
- [[dot-test_no_signer_leaves_envelope_empty()]] - degree 2, connects to 1 community
