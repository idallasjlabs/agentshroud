---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "email_send"
location: "L176"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/email_send
---

# email_send()

## Connections
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[AuthRequired_3]] - `references` [EXTRACTED]
- [[Email send gateway (P3 channel ownership). The bot submits email send requests…]] - `rationale_for` [EXTRACTED]
- [[EmailSendRequest]] - `uses` [INFERRED]
- [[EmailSendResponse]] - `uses` [INFERRED]
- [[Request_3]] - `references` [EXTRACTED]
- [[_get_gmail_app_password()]] - `indirect_call` [INFERRED]
- [[_is_email_recipient_allowed()]] - `calls` [EXTRACTED]
- [[email_send_owner()]] - `calls` [EXTRACTED]
- [[forward.py]] - `contains` [EXTRACTED]
- [[post_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/email_send
