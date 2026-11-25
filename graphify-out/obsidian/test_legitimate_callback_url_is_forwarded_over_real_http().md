---
source_file: "gateway/tests/test_a2a_integration.py"
type: "code"
community: "A2APolicyEngine"
location: "L256"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2APolicyEngine
---

# test_legitimate_callback_url_is_forwarded_over_real_http()

## Connections
- [[dot-from_dict()_10]] - `calls` [EXTRACTED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[HermesA2AForwarder]] - `uses` [INFERRED]
- [[Negative control for the SSRF suite above — a genuinely public callback URL…]] - `rationale_for` [EXTRACTED]
- [[_jsonrpc()]] - `calls` [EXTRACTED]
- [[asyncio_72]] - `references` [EXTRACTED]
- [[test_a2a_integration.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2APolicyEngine
