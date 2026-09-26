---
type: community
cohesion: 0.04
members: 81
---

# RateLimiter

**Cohesion:** 0.04 - loosely connected
**Members:** 81 nodes

## Members
- [[.__enter__()_2]] - code - gateway/tests/test_gateway_email_service.py
- [[.__exit__()_2]] - code - gateway/tests/test_gateway_email_service.py
- [[.__init__()_11]] - code - gateway/ingest_api/email_service.py
- [[.__init__()_159]] - code - gateway/tests/test_gateway_email_service.py
- [[.body_not_empty()]] - code - gateway/ingest_api/models.py
- [[.build_message()]] - code - gateway/ingest_api/email_service.py
- [[.login()]] - code - gateway/ingest_api/email_service.py
- [[.login()_1]] - code - gateway/tests/test_gateway_email_service.py
- [[.send()]] - code - gateway/ingest_api/email_service.py
- [[.sender()]] - code - gateway/ingest_api/email_service.py
- [[.sendmail()]] - code - gateway/ingest_api/email_service.py
- [[.sendmail()_1]] - code - gateway/tests/test_gateway_email_service.py
- [[.subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[.test_default_transport_is_smtp_ssl()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_email_send_routes_through_injectable_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_html_message_has_plain_fallback_then_html()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_plain_message_has_single_plain_part()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_send_html_uses_html_payload()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_send_logs_in_and_sendmails_over_injected_transport()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_send_propagates_auth_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[.test_send_propagates_generic_smtp_error()]] - code - gateway/tests/test_gateway_email_service.py
- [[AgentTarget_2]] - code - gateway/ingest_api/routes/forward.py
- [[Auth dependency that uses the app state config._2]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired_3]] - code - gateway/ingest_api/routes/forward.py
- [[Build the MIME message string (multipartalternative).          For HTML mail th]] - rationale - gateway/ingest_api/email_service.py
- [[Email send gateway (P3 channel ownership).      The bot submits email send requ]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest_1]] - code - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming)     need, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[ForwardRequest_2]] - code - gateway/ingest_api/routes/forward.py
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[GatewayEmailService_1]] - code - gateway/tests/test_gateway_email_service.py
- [[GatewayEmailService]] - code - gateway/ingest_api/email_service.py
- [[Main ingest endpoint      Receives data from iOS Shortcuts, browser extension, o]] - rationale - gateway/ingest_api/routes/forward.py
- [[MiddlewareManager.process_request()]] - code - gateway/ingest_api/middleware.py
- [[Owner-allowlist checked before PII sanitisation to avoid CVEdate-dense body collapse]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[POST emailsend to the owner sends via forward._email_service — proving]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Protocol]] - code
- [[Records loginsendmail; usable as a context manager like SMTP_SSL.]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Request_4]] - code - gateway/ingest_api/routes/forward.py
- [[Request to send an email through the gateway (P3 channel ownership).      The b]] - rationale - gateway/ingest_api/models.py
- [[Resolve the outbound trust level for `request`, shared by the blocking     and s]] - rationale - gateway/ingest_api/routes/forward.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send an email to the owner without exposing the recipient address in the request]] - rationale - gateway/ingest_api/routes/forward.py
- [[Send one email synchronously.  Blocking — call in an executor.          Raises t]] - rationale - gateway/ingest_api/email_service.py
- [[Sends owner-comms email over an injectable SMTP transport.]] - rationale - gateway/ingest_api/email_service.py
- [[SmtpLike]] - code - gateway/ingest_api/email_service.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes).      Same inbou]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline —     shared by th]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership).      All Telegram messages des]] - rationale - gateway/ingest_api/routes/forward.py
- [[TestBuildMessage]] - code - gateway/tests/test_gateway_email_service.py
- [[TestEndpointUsesService]] - code - gateway/tests/test_gateway_email_service.py
- [[TestSend]] - code - gateway/tests/test_gateway_email_service.py
- [[The subset of ``smtplib.SMTP_SSL`` the service uses.]] - rationale - gateway/ingest_api/email_service.py
- [[TransportFactory]] - code - gateway/ingest_api/email_service.py
- [[_FakeSmtp]] - code - gateway/tests/test_gateway_email_service.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[_resolve_user_trust_level()]] - code - gateway/ingest_api/routes/forward.py
- [[_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[auth_dep()_3]] - code - gateway/ingest_api/routes/forward.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_2]] - code - gateway/tests/test_channel_ownership.py
- [[client()_7]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[email_service.py]] - code - gateway/ingest_api/email_service.py
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[test_gateway_email_service.py]] - code - gateway/tests/test_gateway_email_service.py
- [[test_sender_property()]] - code - gateway/tests/test_gateway_email_service.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RateLimiter
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TestMultiTurnTracker]]
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_ApprovalRequest]]
- 5 edges to [[_COMMUNITY_SSHProxy]]
- 4 edges to [[_COMMUNITY_main.rs]]
- 3 edges to [[_COMMUNITY_A2APolicyEngine]]
- 3 edges to [[_COMMUNITY_InjectionSeverity]]
- 3 edges to [[_COMMUNITY_GitHub Copilot CLI Setup Guide]]
- 3 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_Skill MCP AWS Profile Configuration (MCPM-AWS-P]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_Remediation]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_Atlas — Curriculum Architect (SKILL)]]

## Top bridge nodes
- [[forward.py]] - degree 38, connects to 12 communities
- [[_process_inbound()]] - degree 12, connects to 4 communities
- [[test_email_owner_bypasses_pii.py]] - degree 7, connects to 3 communities
- [[email_send()]] - degree 13, connects to 2 communities
- [[forward_content()]] - degree 9, connects to 2 communities