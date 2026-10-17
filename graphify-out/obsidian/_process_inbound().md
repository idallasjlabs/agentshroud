---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "create_auth_dependency (2)"
location: "L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/create_auth_dependency_2
---

# _process_inbound()

## Connections
- [[ForwardRequest_1]] - `references` [EXTRACTED]
- [[ForwardRequest]] - `shares_data_with` [EXTRACTED]
- [[JSONResponse]] - `calls` [INFERRED]
- [[MiddlewareManager.process_request()]] - `calls` [EXTRACTED]
- [[RBACConfig_2]] - `calls` [EXTRACTED]
- [[Request_3]] - `references` [EXTRACTED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - `rationale_for` [EXTRACTED]
- [[_InboundResult]] - `references` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[forward_content()]] - `calls` [EXTRACTED]
- [[forward_content_stream()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/create_auth_dependency_2
