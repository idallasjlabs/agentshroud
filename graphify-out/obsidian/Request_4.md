---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "Approval Routing & Event Bus"
location: "L126"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Approval_Routing__Event_Bus
---

# Request

## Connections
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[_process_inbound()]] - `references` [EXTRACTED]
- [[auth_dep()_2]] - `references` [EXTRACTED]
- [[email_send()]] - `references` [EXTRACTED]
- [[email_send_owner()]] - `references` [EXTRACTED]
- [[forward_content()]] - `references` [EXTRACTED]
- [[forward_content_stream()]] - `references` [EXTRACTED]
- [[telegram_webhook()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Approval_Routing__Event_Bus