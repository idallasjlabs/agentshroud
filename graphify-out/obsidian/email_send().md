---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "ingest_api/models.py"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ingest_api/modelspy
---

# email_send()

## Connections
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[AuthRequired]] - `references` [EXTRACTED]
- [[Email send gateway (P3 channel ownership). The bot submits email send requests…]] - `rationale_for` [EXTRACTED]
- [[EmailSendRequest]] - `uses` [INFERRED]
- [[EmailSendResponse]] - `uses` [INFERRED]
- [[Request_3]] - `references` [EXTRACTED]
- [[_get_gmail_app_password()]] - `indirect_call` [INFERRED]
- [[_is_email_recipient_allowed()]] - `calls` [EXTRACTED]
- [[email_send_owner()]] - `calls` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[post_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ingest_api/modelspy
