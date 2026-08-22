---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "Forward (routes)"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Forward_routes
---

# email_send()

## Connections
- [[ApprovalRequest_3]] - `calls` [EXTRACTED]
- [[AuthRequired_3]] - `references` [EXTRACTED]
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - `rationale_for` [EXTRACTED]
- [[EmailSendRequest_1]] - `references` [EXTRACTED]
- [[EmailSendResponse]] - `calls` [EXTRACTED]
- [[GatewayEmailService]] - `calls` [EXTRACTED]
- [[JSONResponse]] - `calls` [INFERRED]
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - `rationale_for` [EXTRACTED]
- [[Request_4]] - `references` [EXTRACTED]
- [[_is_email_recipient_allowed()]] - `calls` [EXTRACTED]
- [[email_send_owner()]] - `calls` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[test_email_owner_bypasses_pii.py]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Forward_routes