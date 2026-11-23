---
type: community
members: 20
---

# EnvelopeSigner

**Members:** 20 nodes

## Members
- [[dot-__init__()_215]] - code - gateway/security/instruction_envelope.py
- [[EnvelopeSigner]] - code - gateway/security/instruction_envelope.py
- [[Return ``(content, source)`` if ``wrapped`` is intact and correctly signed.]] - rationale - gateway/security/instruction_envelope.py
- [[Return ``content`` wrapped and signed as untrusted third-party input.]] - rationale - gateway/security/instruction_envelope.py
- [[Signed Instruction Envelopes — C46 Wraps instructions and tool results in HMAC-…]] - rationale - gateway/security/instruction_envelope.py
- [[Signs and verifies InstructionEnvelopes. Usage signer = EnvelopeSigner() env…]] - rationale - gateway/security/instruction_envelope.py
- [[Tests for EnvelopeSigner (C46 — Signed Instruction Envelopes).]] - rationale - gateway/tests/test_instruction_envelope.py
- [[_defang()]] - code - gateway/security/instruction_envelope.py
- [[_id()]] - code - gateway/tests/test_untrusted_envelope.py
- [[fixture_133]] - code
- [[instruction_envelope.py]] - code - gateway/security/instruction_envelope.py
- [[signer()]] - code - gateway/tests/test_instruction_envelope.py
- [[test_embedded_delimiters_are_neutralised()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_instruction_envelope.py]] - code - gateway/tests/test_instruction_envelope.py
- [[test_signature_verifies_and_detects_tampering()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_source_is_sanitised()]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_untrusted_envelope.py]] - code - gateway/tests/test_untrusted_envelope.py
- [[test_wrapped_content_is_delimited_and_labelled()]] - code - gateway/tests/test_untrusted_envelope.py
- [[unwrap_untrusted()]] - code - gateway/security/instruction_envelope.py
- [[wrap_untrusted()]] - code - gateway/security/instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EnvelopeSigner
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_edge_facades.py]]
- 8 edges to [[_COMMUNITY_InstructionEnvelope]]
- 4 edges to [[_COMMUNITY_TestEnvelopeSigner]]
- 3 edges to [[_COMMUNITY_asyncio_1]]
- 3 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 2 edges to [[_COMMUNITY_test_edge_fuzz.py]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[EnvelopeSigner]] - degree 34, connects to 9 communities
- [[instruction_envelope.py]] - degree 12, connects to 3 communities
- [[unwrap_untrusted()]] - degree 8, connects to 2 communities
- [[test_instruction_envelope.py]] - degree 6, connects to 2 communities
- [[wrap_untrusted()]] - degree 11, connects to 1 community
