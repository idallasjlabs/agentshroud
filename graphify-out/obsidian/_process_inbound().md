---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "Approval Routing & Event Bus"
location: "L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Routing__Event_Bus
---

# _process_inbound()

## Connections
- [[ForwardRequest_2]] - `references` [EXTRACTED]
- [[ForwardRequest_1]] - `shares_data_with` [EXTRACTED]
- [[JSONResponse]] - `calls` [INFERRED]
- [[MiddlewareManager.process_request()]] - `calls` [EXTRACTED]
- [[RBACConfig_2]] - `calls` [EXTRACTED]
- [[Request_4]] - `references` [EXTRACTED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - `rationale_for` [EXTRACTED]
- [[_InboundResult]] - `references` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[forward_content()]] - `calls` [EXTRACTED]
- [[forward_content_stream()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Routing__Event_Bus