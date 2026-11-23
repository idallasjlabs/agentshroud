---
type: community
members: 11
---

# InstructionEnvelope

**Members:** 11 nodes

## Members
- [[dot-_compute_signature()]] - code - gateway/security/instruction_envelope.py
- [[dot-sign()]] - code - gateway/security/instruction_envelope.py
- [[dot-verify()_1]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_system_prompt()]] - code - gateway/security/instruction_envelope.py
- [[dot-wrap_tool_result()]] - code - gateway/security/instruction_envelope.py
- [[A signed instruction or tool result.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a system prompt as issuer='system'.]] - rationale - gateway/security/instruction_envelope.py
- [[Convenience sign a tool result as issuer='tooltool_name'.]] - rationale - gateway/security/instruction_envelope.py
- [[InstructionEnvelope]] - code - gateway/security/instruction_envelope.py
- [[Return True if the envelope's signature is valid.]] - rationale - gateway/security/instruction_envelope.py
- [[Return a signed envelope for content.]] - rationale - gateway/security/instruction_envelope.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InstructionEnvelope
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_EnvelopeSigner]]
- 3 edges to [[_COMMUNITY_asyncio_1]]
- 1 edge to [[_COMMUNITY_TestEnvelopeSigner]]

## Top bridge nodes
- [[InstructionEnvelope]] - degree 12, connects to 3 communities
- [[dot-sign()]] - degree 6, connects to 1 community
- [[dot-verify()_1]] - degree 4, connects to 1 community
- [[dot-wrap_system_prompt()]] - degree 4, connects to 1 community
- [[dot-wrap_tool_result()]] - degree 4, connects to 1 community
