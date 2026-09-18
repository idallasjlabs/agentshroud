---
source_file: "gateway/tests/test_a2a_proxy.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L317"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DifferentialPIIDetector
---

# test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()

## Connections
- [[A2AProxy]] - `calls` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `calls` [EXTRACTED]
- [[DifferentialPIIDetector_1]] - `calls` [EXTRACTED]
- [[_StubForwarder]] - `references` [EXTRACTED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[_jsonrpc()]] - `calls` [EXTRACTED]
- [[test_a2a_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/DifferentialPIIDetector