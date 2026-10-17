---
type: community
members: 15
---

# AuditChain (2)

**Members:** 15 nodes

## Members
- [[dot-test_different_keys_fail_verification()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_different_signers_same_key_verify()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_system_prompt()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_envelope_wraps_tool_result()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_sign_and_verify_roundtrip()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_content_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[dot-test_tampered_signature_fails()]] - code - gateway/tests/test_instruction_envelope.py
- [[Envelopes signed with one key should not verify with a different key.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying content after signing should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[Modifying the signature directly should fail verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[TestEnvelopeSigner]] - code - gateway/tests/test_instruction_envelope.py
- [[Two signers sharing the same key can cross-verify envelopes.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[sign() + verify() should return True for unmodified content.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_system_prompt() sets issuer='system' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py
- [[wrap_tool_result() sets issuer='toolname' and passes verification.]] - rationale - gateway/tests/test_instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain_2
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_AuditChain]]

## Top bridge nodes
- [[TestEnvelopeSigner]] - degree 10, connects to 1 community
- [[dot-test_different_keys_fail_verification()]] - degree 3, connects to 1 community
- [[dot-test_different_signers_same_key_verify()]] - degree 3, connects to 1 community
