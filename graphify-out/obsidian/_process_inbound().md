---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "email_send"
location: "L386"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/email_send
---

# _process_inbound()

## Connections
- [[ForwardRequest]] - `uses` [INFERRED]
- [[RBACConfig]] - `calls` [EXTRACTED]
- [[Request_3]] - `references` [EXTRACTED]
- [[Target resolution + P1 middleware + inbound security pipeline — shared by the…]] - `rationale_for` [EXTRACTED]
- [[_InboundResult]] - `calls` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[forward_content()]] - `calls` [EXTRACTED]
- [[forward_content_stream()]] - `calls` [EXTRACTED]
- [[source()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/email_send
