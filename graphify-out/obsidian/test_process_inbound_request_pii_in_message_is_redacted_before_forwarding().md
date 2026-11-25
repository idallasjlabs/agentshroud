---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "A2AProxy"
location: "L282"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2AProxy
---

# test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()

## Connections
- [[A SendMessage containing PII must have it redacted in what's forwarded to…]] - `rationale_for` [EXTRACTED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[_StubForwarder_2]] - `references` [EXTRACTED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[_jsonrpc()_2]] - `calls` [EXTRACTED]
- [[asyncio_87]] - `references` [EXTRACTED]
- [[test_a2a_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2AProxy
