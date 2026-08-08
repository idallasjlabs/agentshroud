---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "Gateway Ingest API"
location: "L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Ingest_API
---

# _process_inbound()

## Connections
- [[ForwardRequest]] - `shares_data_with` [EXTRACTED]
- [[ForwardRequest_2]] - `references` [EXTRACTED]
- [[JSONResponse]] - `calls` [INFERRED]
- [[MiddlewareManager.process_request()]] - `calls` [EXTRACTED]
- [[MultiAgentRouter.resolve_target()]] - `calls` [EXTRACTED]
- [[RBACConfig_1]] - `calls` [EXTRACTED]
- [[Request_1]] - `references` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - `rationale_for` [EXTRACTED]
- [[_InboundResult]] - `references` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[forward_content()]] - `calls` [EXTRACTED]
- [[forward_content_stream()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Ingest_API