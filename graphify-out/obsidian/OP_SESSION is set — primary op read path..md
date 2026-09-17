---
source_file: "gateway/tests/test_gmail_credential_retrieval.py"
type: "rationale"
community: "_get_gmail_app_password()"
location: "L126"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_get_gmail_app_password
---

# OP_SESSION is set — primary op read path.

## Connections
- [[TestGetGmailAppPasswordWithSession]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_get_gmail_app_password