---
source_file: "gateway/proxy/forwarder.py"
type: "code"
community: "AgentTarget"
location: "L49"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# HTTPForwarder

## Connections
- [[dot-__init__()_146]] - `method` [EXTRACTED]
- [[dot-forward()_3]] - `method` [EXTRACTED]
- [[dot-get_stats()_14]] - `method` [EXTRACTED]
- [[dot-health_check()_5]] - `method` [EXTRACTED]
- [[dot-is_healthy()]] - `method` [EXTRACTED]
- [[dot-last_forward_time()]] - `method` [EXTRACTED]
- [[dot-set_response_handler()]] - `method` [EXTRACTED]
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - `rationale_for` [EXTRACTED]
- [[HTTPConnectProxy_1]] - `conceptually_related_to` [INFERRED]
- [[MultiAgentRouter]] - `semantically_similar_to` [INFERRED]
- [[SecurityPipeline_1]] - `references` [EXTRACTED]
- [[_PassInboundPipeline]] - `uses` [INFERRED]
- [[_StubForwarder_2]] - `uses` [INFERRED]
- [[forwarder()_1]] - `calls` [EXTRACTED]
- [[forwarder.py]] - `contains` [EXTRACTED]
- [[healthy_forwarder()]] - `calls` [EXTRACTED]
- [[run_canary()_1]] - `calls` [INFERRED]
- [[test_canary.py]] - `imports` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_forwarder_error_handling()]] - `calls` [EXTRACTED]
- [[unhealthy_forwarder()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
