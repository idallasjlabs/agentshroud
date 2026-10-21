---
type: community
members: 20
---

# Remediation

**Members:** 20 nodes

## Members
- [[dot-__init__()_143]] - code - gateway/proxy/webhook_receiver.py
- [[dot-_can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[dot-test_falls_back_to_op_signin_when_account_add_fails()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[dot-test_falls_back_to_secrets_when_op_read_fails()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[dot-test_falls_back_to_secrets_when_op_session_absent()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[dot-test_returns_none_when_all_paths_fail()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[dot-test_returns_none_when_no_session_and_no_secrets()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[dot-test_uses_existing_session_when_op_read_succeeds()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[CompletedProcess_5]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Core regression test empty OP_SESSION must NOT short-circuit the secrets path.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[OP_SESSION absent — must fall back to mounted secrets.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[OP_SESSION is set — primary op read path.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[Path_45]] - code - gateway/proxy/webhook_receiver.py
- [[Read Gmail app password from 1Password using the gateway's cached session.]] - rationale - gateway/ingest_api/routes/forward.py
- [[TestGetGmailAppPasswordNoSession]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[TestGetGmailAppPasswordWithSession]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[_completed()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[_get_gmail_app_password()]] - code - gateway/ingest_api/routes/forward.py
- [[test_gmail_credential_retrieval.py]] - code - gateway/tests/test_gmail_credential_retrieval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Remediation
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[dot-__init__()_143]] - degree 5, connects to 3 communities
- [[Path_45]] - degree 5, connects to 2 communities
- [[_get_gmail_app_password()]] - degree 10, connects to 1 community
- [[dot-_can_create_directory()]] - degree 4, connects to 1 community
