---
type: community
members: 40
---

# create_auth_dependency (2)

**Members:** 40 nodes

## Members
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_1]] - code - gateway/ingest_api/routes/forward.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[ForwardRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_3]] - code - gateway/ingest_api/routes/forward.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_6]] - code - gateway/tests/test_channel_ownership.py
- [[client()_7]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_auth_dependency_2
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_forward_stream.py]]
- 8 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 3 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 3 edges to [[_COMMUNITY_create_auth_dependency]]
- 3 edges to [[_COMMUNITY_GatewayEmailService]]
- 3 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)]]
- 2 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 2 edges to [[_COMMUNITY_WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)]]
- 2 edges to [[_COMMUNITY_TestEmailSend]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_AsyncMock (3)]]
- 1 edge to [[_COMMUNITY_AgentTarget (3)]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)_1]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]

## Top bridge nodes
- [[forward.py]] - degree 37, connects to 15 communities
- [[_process_inbound()]] - degree 12, connects to 4 communities
- [[email_send()]] - degree 13, connects to 3 communities
- [[forward_content()]] - degree 9, connects to 3 communities
- [[test_email_owner_bypasses_pii.py]] - degree 7, connects to 3 communities
