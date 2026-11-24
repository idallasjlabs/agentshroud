---
type: community
members: 70
---

# EnvelopeSigner

**Members:** 70 nodes

## Members
- [[dot-__init__()_203]] - code - gateway/inbound_edge/facades.py
- [[dot-__init__()_204]] - code - gateway/inbound_edge/facades.py
- [[dot-__init__()_205]] - code - gateway/security/instruction_envelope.py
- [[dot-_age_hours()]] - code - gateway/inbound_edge/facades.py
- [[dot-_compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[dot-_parse()]] - code - gateway/inbound_edge/facades.py
- [[dot-run()_9]] - code - gateway/inbound_edge/facades.py
- [[dot-run()_10]] - code - gateway/inbound_edge/facades.py
- [[dot-run()_11]] - code - gateway/inbound_edge/facades.py
- [[dot-sign()]] - code - gateway/security/instruction_envelope.py
- [[dot-test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_outbound_response_is_signed_and_verifiable()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-verify()_1]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[Any_81]] - code
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[HermesDelegate]] - code - gateway/inbound_edge/facades.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[PkeStatus]] - code - gateway/inbound_edge/facades.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return ``(content, source)`` if ``wrapped`` is intact and correctly signed.]] - rationale - gateway/security/instruction_envelope.py
- [[Return ``content`` wrapped and signed as untrusted third-party input.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py
- [[Signed Instruction Envelopes — C46 Wraps instructions and tool results in HMAC-…]] - rationale - gateway/security/instruction_envelope.py
- [[Signs and verifies InstructionEnvelopes. Usage signer = EnvelopeSigner() env…]] - rationale - gateway/security/instruction_envelope.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[Tests for EnvelopeSigner (C46 — Signed Instruction Envelopes).]] - rationale - gateway/tests/test_instruction_envelope.py
- [[The signed descriptor says freshness per feed — a stale feed (e.g. a GitHub…]] - rationale - gateway/tests/test_edge_facades.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_defang()]] - code - gateway/security/instruction_envelope.py
- [[_id()]] - code - gateway/tests/test_untrusted_envelope.py
- [[datetime_9]] - code
- [[facades.py]] - code - gateway/inbound_edge/facades.py
- [[fixture_133]] - code
- [[handler()_2]] - code - gateway/tests/test_edge_facades.py
- [[handler()_3]] - code - gateway/tests/test_edge_facades.py
- [[handler()_4]] - code - gateway/tests/test_edge_facades.py
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
TABLE source_file, type FROM #community/EnvelopeSigner
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_edge_fuzz.py]]
- 6 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 5 edges to [[_COMMUNITY_SecurityPipeline]]
- 3 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EnvelopeSigner]] - degree 34, connects to 7 communities
- [[HermesDelegate]] - degree 10, connects to 3 communities
- [[facades.py]] - degree 10, connects to 3 communities
- [[test_edge_facades.py]] - degree 14, connects to 2 communities
- [[PkeStatus]] - degree 12, connects to 2 communities
