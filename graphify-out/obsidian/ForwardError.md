---
source_file: "gateway/ingest_api/router.py"
type: "code"
community: "Forward Routing & Approval"
location: "L36"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Forward_Routing__Approval
---

# ForwardError

## Connections
- [[.forward_to_agent()]] - `calls` [EXTRACTED]
- [[.forward_to_agent_stream()]] - `calls` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Raised when forwarding to agent fails]] - `rationale_for` [EXTRACTED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[_BlockingPipeline]] - `uses` [INFERRED]
- [[_PassthroughPipeline]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[router.py]] - `contains` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_forward_stream_forward_error_still_emits_done_event()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_router_openai_translation.py]] - `imports` [EXTRACTED]
- [[test_router_streaming.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Forward_Routing__Approval