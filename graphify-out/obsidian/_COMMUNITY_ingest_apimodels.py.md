---
type: community
members: 110
---

# ingest_api/models.py

**Members:** 110 nodes

## Members
- [[dot-body_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-content_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-path_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-subject_not_empty()]] - code - gateway/ingest_api/models.py
- [[dot-test_status_response_model()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_monitor_mode()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-test_status_response_optional_fields()]] - code - gateway/tests/test_enhanced_status.py
- [[dot-validate_base64()]] - code - gateway/ingest_api/models.py
- [[dot-validate_source()]] - code - gateway/ingest_api/models.py
- [[ApprovalDecision]] - code - gateway/ingest_api/models.py
- [[Auth dependency that uses the app state config.]] - rationale - gateway/ingest_api/routes/forward.py
- [[AuthRequired]] - code
- [[BaseModel_3]] - code
- [[BaseModel_4]] - code
- [[Catch-all error handler Never leaks stack traces or internal details to client.…]] - rationale - gateway/ingest_api/main.py
- [[Email send gateway (P3 channel ownership). The bot submits email send requests…]] - rationale - gateway/ingest_api/routes/forward.py
- [[EmailSendRequest]] - code - gateway/ingest_api/models.py
- [[EmailSendResponse]] - code - gateway/ingest_api/models.py
- [[Everything the post-routing forwarding steps (blocking or streaming) need, once…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Exception_5]] - code
- [[ForwardResponse]] - code - gateway/ingest_api/models.py
- [[Health check response with v0.8.0 security dashboard data]] - rationale - gateway/ingest_api/models.py
- [[LedgerQueryResponse]] - code - gateway/ingest_api/models.py
- [[Main ingest endpoint Receives data from iOS Shortcuts, browser extension, or…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Message forwarding routes. Core message forwarding endpoints -…]] - rationale - gateway/ingest_api/routes/forward.py
- [[OwnerEmailRequest]] - code - gateway/ingest_api/routes/forward.py
- [[Paginated ledger query results]] - rationale - gateway/ingest_api/models.py
- [[Reject request bodies larger than 1MB before parsing. Checks Content-Length…]] - rationale - gateway/ingest_api/main.py
- [[Request_3]] - code
- [[Request to send an email through the gateway (P3 channel ownership). The bot…]] - rationale - gateway/ingest_api/models.py
- [[Request to write file content to an allowlisted SSH host. Unlike…]] - rationale - gateway/ingest_api/models.py
- [[Response after content is ingested, sanitized, and logged]] - rationale - gateway/ingest_api/models.py
- [[Response from POST emailsend.]] - rationale - gateway/ingest_api/models.py
- [[Response from POST sshwrite_file. success reflects whether the remote write…]] - rationale - gateway/ingest_api/models.py
- [[Return True if the email address is on the pre-approved recipient list.]] - rationale - gateway/ingest_api/routes/forward.py
- [[SSHWriteFileRequest]] - code - gateway/ingest_api/models.py
- [[SSHWriteFileResponse]] - code - gateway/ingest_api/models.py
- [[Send an email to the owner without exposing the recipient address in the…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Simplified unit tests for main.py to achieve 90% coverage Focuses on easily…]] - rationale - gateway/tests/test_main_simple.py
- [[StatusResponse]] - code - gateway/ingest_api/models.py
- [[Streaming variant of forward for OpenAI-compat agents (Hermes). Same inbound…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Target resolution + P1 middleware + inbound security pipeline — shared by the…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Telegram inbound webhook (P3 channel ownership). All Telegram messages…]] - rationale - gateway/ingest_api/routes/forward.py
- [[Test ApprovalDecision with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test ApprovalRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test FastAPI lifespan initialization]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects empty content]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest rejects invalid source]] - rationale - gateway/tests/test_main_simple.py
- [[Test ForwardRequest with valid data]] - rationale - gateway/tests/test_main_simple.py
- [[Test enhanced status endpoint with observatory mode and egress info.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test global exception handler]] - rationale - gateway/tests/test_main_simple.py
- [[Test global exception handler with HTTPException]] - rationale - gateway/tests/test_main_simple.py
- [[Test request logging middleware]] - rationale - gateway/tests/test_main_simple.py
- [[Test status response in monitor mode.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that StatusResponse model accepts new fields.]] - rationale - gateway/tests/test_enhanced_status.py
- [[Test that new fields are optional (backward compat).]] - rationale - gateway/tests/test_enhanced_status.py
- [[TestEnhancedStatus]] - code - gateway/tests/test_enhanced_status.py
- [[User's decision on a pending approval request]] - rationale - gateway/ingest_api/models.py
- [[_InboundResult]] - code - gateway/ingest_api/routes/forward.py
- [[_body_stream()]] - code - gateway/ingest_api/main.py
- [[_is_email_recipient_allowed()]] - code - gateway/ingest_api/routes/forward.py
- [[_process_inbound()]] - code - gateway/ingest_api/routes/forward.py
- [[asyncio_32]] - code
- [[auth_dep()_1]] - code - gateway/ingest_api/routes/forward.py
- [[disconnecting_stream()]] - code - gateway/tests/test_main_simple.py
- [[email_send()]] - code - gateway/ingest_api/routes/forward.py
- [[email_send_owner()]] - code - gateway/ingest_api/routes/forward.py
- [[exception_handler]] - code
- [[field_validator_1]] - code
- [[forward.py]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content()]] - code - gateway/ingest_api/routes/forward.py
- [[forward_content_stream()]] - code - gateway/ingest_api/routes/forward.py
- [[global_exception_handler()]] - code - gateway/ingest_api/main.py
- [[ingest_apimodels.py]] - code - gateway/ingest_api/models.py
- [[limit_request_body re-injects a fully-read chunked body and calls downstream.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body rejects chunked bodies over 1MB with 413.]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body returns a clean 400 when the client drops mid-upload.…]] - rationale - gateway/tests/test_main_simple.py
- [[limit_request_body()]] - code - gateway/ingest_api/main.py
- [[mock_call_next()]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next()_1]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next()_2]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next()_3]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next()_4]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next_raises()]] - code - gateway/tests/test_main_simple.py
- [[mock_call_next_raises()_1]] - code - gateway/tests/test_main_simple.py
- [[oversized_stream()]] - code - gateway/tests/test_main_simple.py
- [[post_3]] - code
- [[pydantic_1]] - document - docs/vault/05 - Dependencies/pydantic.md
- [[security_headers_middleware adds expected security headers.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware re-raises BaseExceptions that are not groups.]] - rationale - gateway/tests/test_main_simple.py
- [[security_headers_middleware returns 500 when anyio BaseExceptionGroup is…]] - rationale - gateway/tests/test_main_simple.py
- [[small_stream()]] - code - gateway/tests/test_main_simple.py
- [[telegram_webhook()]] - code - gateway/ingest_api/routes/forward.py
- [[test_approval_decision_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_approval_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_enhanced_status.py]] - code - gateway/tests/test_enhanced_status.py
- [[test_forward_request_valid()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_empty_content()]] - code - gateway/tests/test_main_simple.py
- [[test_forward_request_validation_invalid_source()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler()]] - code - gateway/tests/test_main_simple.py
- [[test_global_exception_handler_http_exception()]] - code - gateway/tests/test_main_simple.py
- [[test_lifespan_initialization()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_over_limit_rejected()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_chunked_body_within_limit_passes_through()]] - code - gateway/tests/test_main_simple.py
- [[test_limit_request_body_client_disconnect_returns_clean_response()]] - code - gateway/tests/test_main_simple.py
- [[test_log_requests_middleware()]] - code - gateway/tests/test_main_simple.py
- [[test_main_simple.py]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_catches_exception_group()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_normal_response()]] - code - gateway/tests/test_main_simple.py
- [[test_security_headers_middleware_reraises_non_group()]] - code - gateway/tests/test_main_simple.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingest_api/modelspy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_ingest_apimain.py]]
- 13 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 12 edges to [[_COMMUNITY_TestConfigValidation]]
- 9 edges to [[_COMMUNITY_ApprovalRequest]]
- 9 edges to [[_COMMUNITY_fastapi]]
- 9 edges to [[_COMMUNITY_test_forward_stream.py]]
- 8 edges to [[_COMMUNITY_AgentTarget]]
- 6 edges to [[_COMMUNITY_RedactionResult]]
- 4 edges to [[_COMMUNITY_ApprovalStore]]
- 4 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 3 edges to [[_COMMUNITY_app]]
- 3 edges to [[_COMMUNITY__get_gmail_app_password]]
- 2 edges to [[_COMMUNITY_GatewayEmailService]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_WebhookReceiver]]
- 2 edges to [[_COMMUNITY_test_channel_ownership.py]]
- 2 edges to [[_COMMUNITY_test_forward_routing.py]]
- 2 edges to [[_COMMUNITY_IntelReportStore]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_Pydantic]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_socmodels.py]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_installer.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]

## Top bridge nodes
- [[forward.py]] - degree 42, connects to 15 communities
- [[ingest_apimodels.py]] - degree 45, connects to 13 communities
- [[pydantic_1]] - degree 17, connects to 13 communities
- [[BaseModel_3]] - degree 17, connects to 7 communities
- [[test_main_simple.py]] - degree 26, connects to 4 communities
