---
type: community
members: 54
---

# Community 80

**Members:** 54 nodes

## Members
- [[.__init__()_20]] - code - gateway/inbound_edge/facades.py
- [[.__init__()_101]] - code - gateway/security/instruction_envelope.py
- [[._compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[.sign()]] - code - gateway/security/instruction_envelope.py
- [[.test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[.test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[.verify()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[.wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system promptstool results)]] - concept - gateway/tests/test_instruction_envelope.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/inbound_edge/facades.py
- [[EnvelopeSigner_1]] - code - gateway/security/instruction_envelope.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return ``(content, source)`` if ``wrapped`` is intact and correctly signed.]] - rationale - gateway/security/instruction_envelope.py
- [[Return ``content`` wrapped and signed as untrusted third-party input.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[Signs and verifies InstructionEnvelopes.      Usage          signer = Envelope]] - rationale - gateway/security/instruction_envelope.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[The signed descriptor says freshness per feed — a stale feed (e.g. a     GitHu]] - rationale - gateway/tests/test_edge_facades.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_defang()]] - code - gateway/security/instruction_envelope.py
- [[_id()]] - code - gateway/tests/test_untrusted_envelope.py
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[sign() + verify() should return True for unmodified content.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[test_delegate_wraps_task_as_untrusted_and_targets_restricted_profile()]] - code - gateway/tests/test_edge_facades.py
- [[test_edge_facades.py]] - code - gateway/tests/test_edge_facades.py
- [[test_embedded_delimiters_are_neutralised()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[test_lab_search_queries_fixed_endpoint_and_trims()]] - code - gateway/tests/test_edge_facades.py
- [[test_pke_status_freshness_is_none_without_dated_episodes()]] - code - gateway/tests/test_edge_facades.py
- [[test_pke_status_reports_broken_feed_without_raising()]] - code - gateway/tests/test_edge_facades.py
- [[test_pke_status_reports_freshness_the_descriptor_promises()]] - code - gateway/tests/test_edge_facades.py
- [[test_pke_status_summary_and_per_feed()]] - code - gateway/tests/test_edge_facades.py
- [[test_signature_verifies_and_detects_tampering()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_source_is_sanitised()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_untrusted_envelope.py]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_wrapped_content_is_delimited_and_labelled()]] - code - gateway/tests/test_untrusted_envelope.py
- [[unwrap_untrusted()]] - code - gateway/security/instruction_envelope.py
- [[wrap_system_prompt() sets issuer='system' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_tool_result() sets issuer='toolname' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_untrusted()]] - code - gateway/security/instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_80
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Community 32]]
- 20 edges to [[_COMMUNITY_Community 24]]
- 6 edges to [[_COMMUNITY_Community 531]]
- 2 edges to [[_COMMUNITY_Community 151]]
- 2 edges to [[_COMMUNITY_Community 1566]]
- 2 edges to [[_COMMUNITY_Community 1352]]
- 1 edge to [[_COMMUNITY_Community 41]]

## Top bridge nodes
- [[EnvelopeSigner_1]] - degree 55, connects to 7 communities
- [[InstructionEnvelope]] - degree 24, connects to 4 communities
- [[wrap_untrusted()]] - degree 12, connects to 1 community
- [[test_edge_facades.py]] - degree 11, connects to 1 community
- [[test_delegate_wraps_task_as_untrusted_and_targets_restricted_profile()]] - degree 4, connects to 1 community