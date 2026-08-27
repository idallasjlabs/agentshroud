---
source_file: "gateway/ingest_api/router.py"
type: "code"
community: "Community 38"
location: "L36"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_38
---

# ForwardError

## Connections
- [[.forward_to_agent()]] - `calls` [EXTRACTED]
- [[.forward_to_agent_stream()]] - `calls` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[Raised when forwarding to agent fails]] - `rationale_for` [EXTRACTED]
- [[RouterConfig]] - `uses` [INFERRED]
- [[_BlockingPipeline]] - `uses` [INFERRED]
- [[_PassthroughPipeline]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[router.py]] - `contains` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_forward_stream_forward_error_still_emits_done_event()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_router_openai_translation.py]] - `imports` [EXTRACTED]
- [[test_router_streaming.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_38