---
type: community
members: 45
---

# email_send

**Members:** 45 nodes

## Members
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-content_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[dot-validate_source()]] - code - gateway/ingest_api/models.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_3]] - code
- [[BaseModel_3]] - code
- [[Email send gateway (P3 channel ownership). The bot submits email send requests…]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming) need, once…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Main ingest endpoint Receives data from iOS Shortcuts, browser extension, or…]] - rationale - gateway/ingest_api/routes/forward.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Request_3]] - code
- [[Request to send an email through the gateway (P3 channel ownership). The bot…]] - rationale - gateway/ingest_api/models.py
- [[Request to write file content to an allowlisted SSH host. Unlike…]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[SSHWriteFileRequest]] - code - gateway/ingest_api/models.py
- [[Send an email to the owner without exposing the recipient address in the…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes). Same inbound…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline — shared by the…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership). All Telegram messages…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Tests for P3 Channel Ownership — Telegram webhook + email send. TDD red phase…]] - rationale - gateway/tests/test_channel_ownership.py
- [[Tests that owner-bound email bypasses PII sanitisation. Root cause of the…]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_9]] - code - gateway/tests/test_channel_ownership.py
- [[client()_10]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[field_validator_1]] - code
- [[fixture_54]] - code
- [[fixture_55]] - code
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[post_3]] - code
- [[source()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/email_send
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_ingest_apimain.py]]
- 8 edges to [[_COMMUNITY_AgentTarget]]
- 5 edges to [[_COMMUNITY_GatewayConfig]]
- 4 edges to [[_COMMUNITY_app]]
- 4 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_TestEmailSend]]
- 1 edge to [[_COMMUNITY_TestTelegramWebhook]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_test_anthropic_openai_translator.py]]
- 1 edge to [[_COMMUNITY__get_gmail_app_password]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]

## Top bridge nodes
- [[email_send()]] - degree 11, connects to 4 communities
- [[forward_content()]] - degree 10, connects to 4 communities
- [[test_channel_ownership.py]] - degree 9, connects to 4 communities
- [[forward_content_stream()]] - degree 10, connects to 3 communities
- [[_process_inbound()]] - degree 9, connects to 3 communities
