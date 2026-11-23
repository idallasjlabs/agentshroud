---
source_file: "gateway/tests/test_a2a_policy.py"
type: "code"
community: "A2APolicyEngine"
location: "L402"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2APolicyEngine
---

# test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()

## Connections
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyAction]] - `uses` [INFERRED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[_LegacyStubApprovalQueue]] - `calls` [EXTRACTED]
- [[_base_config()_1]] - `calls` [EXTRACTED]
- [[asyncio_73]] - `references` [EXTRACTED]
- [[test_a2a_policy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2APolicyEngine
