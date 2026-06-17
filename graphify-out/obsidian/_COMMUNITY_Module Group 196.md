---
type: community
cohesion: 0.11
members: 24
---

# Module Group 196

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_36]] - code - gateway/proxy/webhook_receiver.py
- [[._can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[._run()]] - code - gateway/runtime/engine.py
- [[.test_falls_back_to_op_signin_when_account_add_fails()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[.test_falls_back_to_secrets_when_op_read_fails()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[.test_falls_back_to_secrets_when_op_session_absent()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[.test_returns_none_when_all_paths_fail()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[.test_returns_none_when_no_session_and_no_secrets()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[.test_uses_existing_session_when_op_read_succeeds()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[CompletedProcess]] - code - gateway/runtime/engine.py
- [[CompletedProcess_1]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[Core regression test empty OP_SESSION must NOT short-circuit the secrets path.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[OP_SESSION absent — must fall back to mounted secrets.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[OP_SESSION is set — primary op read path.]] - rationale - gateway/tests/test_gmail_credential_retrieval.py
- [[Path_4]] - code - gateway/proxy/webhook_receiver.py
- [[Read Gmail app password from 1Password using the gateway's cached session.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Run a CLI command and return the result.]] - rationale - gateway/runtime/engine.py
- [[Start a container. Returns container id.]] - rationale - gateway/runtime/engine.py
- [[TestGetGmailAppPasswordNoSession]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[TestGetGmailAppPasswordWithSession]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[_completed()]] - code - gateway/tests/test_gmail_credential_retrieval.py
- [[_get_gmail_app_password()]] - code - gateway/ingest_api/routes/forward.py
- [[test_gmail_credential_retrieval.py]] - code - gateway/tests/test_gmail_credential_retrieval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_196
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Webhook Receiver]]
- 2 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 2 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 1 edge to [[_COMMUNITY_Module Group 195]]
- 1 edge to [[_COMMUNITY_Module Group 82]]
- 1 edge to [[_COMMUNITY_SOC Router & Correlation]]

## Top bridge nodes
- [[.__init__()_36]] - degree 5, connects to 3 communities
- [[._run()]] - degree 6, connects to 2 communities
- [[Path_4]] - degree 5, connects to 2 communities
- [[_get_gmail_app_password()]] - degree 11, connects to 1 community
- [[._can_create_directory()]] - degree 4, connects to 1 community