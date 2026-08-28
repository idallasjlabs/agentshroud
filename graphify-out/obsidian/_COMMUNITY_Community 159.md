---
type: community
cohesion: 0.08
members: 41
---

# Community 159

**Cohesion:** 0.08 - loosely connected
**Members:** 41 nodes

## Members
- [[.body_not_empty()]] - code - gateway/ingest_api/models.py
- [[.subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/forward.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[FastAPI app instance]] - code - gateway/ingest_api/main.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_5]] - code - gateway/ingest_api/routes/forward.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_2]] - code - gateway/tests/test_channel_ownership.py
- [[client()_7]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[version_routes APIRouter — apiv1versions]] - code - gateway/ingest_api/version_routes.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_159
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 8 edges to [[_COMMUNITY_Community 119]]
- 7 edges to [[_COMMUNITY_Ingest API & Approval Routes]]
- 4 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 3 edges to [[_COMMUNITY_Community 14]]
- 3 edges to [[_COMMUNITY_Community 178]]
- 3 edges to [[_COMMUNITY_Community 32]]
- 3 edges to [[_COMMUNITY_Community 28]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Config Validation & Router]]
- 2 edges to [[_COMMUNITY_Community 56]]
- 2 edges to [[_COMMUNITY_SOC Collaborators]]
- 2 edges to [[_COMMUNITY_Community 228]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Community 1503]]
- 1 edge to [[_COMMUNITY_Community 26]]
- 1 edge to [[_COMMUNITY_Community 565]]
- 1 edge to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Session Management]]
- 1 edge to [[_COMMUNITY_Community 545]]
- 1 edge to [[_COMMUNITY_Community 986]]
- 1 edge to [[_COMMUNITY_Community 111]]
- 1 edge to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 1059]]
- 1 edge to [[_COMMUNITY_Community 811]]
- 1 edge to [[_COMMUNITY_Community 458]]

## Top bridge nodes
- [[forward.py]] - degree 36, connects to 13 communities
- [[FastAPI app instance]] - degree 10, connects to 7 communities
- [[_process_inbound()]] - degree 12, connects to 4 communities
- [[email_send()]] - degree 13, connects to 3 communities
- [[forward_content()]] - degree 9, connects to 3 communities