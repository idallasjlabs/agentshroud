---
source_file: "gateway/tests/test_gmail_credential_retrieval.py"
type: "code"
community: "_get_gmail_app_password"
location: "L86"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_get_gmail_app_password
---

# .test_falls_back_to_op_signin_when_account_add_fails()

## Connections
- [[TestGetGmailAppPasswordNoSession]] - `method` [EXTRACTED]
- [[_get_gmail_app_password()]] - `calls` [EXTRACTED]
- [[fake_path()_1]] - `contains` [EXTRACTED]
- [[fake_path()_2]] - `indirect_call` [INFERRED]
- [[fake_run()_4]] - `contains` [EXTRACTED]
- [[fake_run()_5]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/_get_gmail_app_password
