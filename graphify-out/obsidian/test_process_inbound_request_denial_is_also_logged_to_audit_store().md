---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "A2AProxy"
location: "L487"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2AProxy
---

# test_process_inbound_request_denial_is_also_logged_to_audit_store()

## Connections
- [[A2AProxy]] - `uses` [INFERRED]
- [[_StubAuditStore]] - `calls` [EXTRACTED]
- [[_StubForwarder_1]] - `references` [EXTRACTED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[_jsonrpc()]] - `calls` [EXTRACTED]
- [[asyncio_85]] - `references` [EXTRACTED]
- [[test_a2a_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2AProxy
