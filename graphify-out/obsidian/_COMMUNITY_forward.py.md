---
type: community
cohesion: 0.09
members: 31
---

# forward.py

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[Auth dependency that uses the app state config._1]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/forward.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/models.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_4]] - code - gateway/ingest_api/routes/forward.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[auth_dep()_2]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_4]] - code - gateway/tests/test_channel_ownership.py
- [[client()_5]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/forwardpy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_forward.py_1]]
- 6 edges to [[_COMMUNITY_AgentTarget]]
- 6 edges to [[_COMMUNITY_RBACConfig]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_DataLedger]]
- 3 edges to [[_COMMUNITY_WebhookReceiver]]
- 3 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_test_main_endpoints.py_1]]
- 2 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_GatewayEmailService]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 2 edges to [[_COMMUNITY_WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)]]
- 1 edge to [[_COMMUNITY_AsyncMock_1]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_GatewayEmailService_1]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]
- 1 edge to [[_COMMUNITY_TestEmailSend]]
- 1 edge to [[_COMMUNITY_TestEmailSend_1]]

## Top bridge nodes
- [[forward.py]] - degree 37, connects to 14 communities
- [[email_send()]] - degree 13, connects to 3 communities
- [[test_channel_ownership.py]] - degree 7, connects to 3 communities
- [[test_email_owner_bypasses_pii.py]] - degree 7, connects to 3 communities
- [[webhook_receiver.py]] - degree 4, connects to 3 communities
