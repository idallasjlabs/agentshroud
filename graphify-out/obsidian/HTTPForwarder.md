---
source_file: "gateway/proxy/forwarder.py"
type: "code"
community: "HTTP Forwarder"
location: "L49"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_Forwarder
---

# HTTPForwarder

## Connections
- [[.__init__()_23]] - `method` [EXTRACTED]
- [[.forward()]] - `method` [EXTRACTED]
- [[.get_stats()_3]] - `method` [EXTRACTED]
- [[.health_check()_1]] - `method` [EXTRACTED]
- [[.is_healthy()]] - `method` [EXTRACTED]
- [[.last_forward_time()]] - `method` [EXTRACTED]
- [[.set_response_handler()]] - `method` [EXTRACTED]
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - `rationale_for` [EXTRACTED]
- [[_PassInboundPipeline]] - `uses` [INFERRED]
- [[_StubForwarder]] - `uses` [INFERRED]
- [[forwarder()]] - `calls` [EXTRACTED]
- [[forwarder.py]] - `contains` [EXTRACTED]
- [[healthy_forwarder()]] - `calls` [EXTRACTED]
- [[test_canary.py]] - `imports` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_forwarder_error_handling()]] - `calls` [EXTRACTED]
- [[unhealthy_forwarder()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_Forwarder