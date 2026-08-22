---
source_file: "gateway/proxy/webhook_receiver.py"
type: "code"
community: "Middleware & Session Isolation"
location: "L30"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# WebhookReceiver

## Connections
- [[.__init__()_45]] - `method` [EXTRACTED]
- [[._can_create_directory()]] - `method` [EXTRACTED]
- [[._extract_message()]] - `method` [EXTRACTED]
- [[._extract_user_id()_1]] - `method` [EXTRACTED]
- [[._extract_username()]] - `method` [EXTRACTED]
- [[._prepare_session_payload()]] - `method` [EXTRACTED]
- [[._replace_message()]] - `method` [EXTRACTED]
- [[.get_stats()_11]] - `method` [EXTRACTED]
- [[.process_webhook()]] - `method` [EXTRACTED]
- [[.test_webhook_conversation_logging()]] - `calls` [EXTRACTED]
- [[.test_webhook_session_context_injection()]] - `calls` [EXTRACTED]
- [[.test_webhook_user_id_extraction()]] - `calls` [EXTRACTED]
- [[.validate_signature()]] - `method` [EXTRACTED]
- [[Collaborator Tracker Tests]] - `references` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Receives webhooks and routes them through the security pipeline.      In product]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[SlackAPIProxy_1]] - `uses` [INFERRED]
- [[TestHandleEvent]] - `uses` [INFERRED]
- [[TestMiddlewareSessionEnforcement]] - `uses` [INFERRED]
- [[TestMultiFieldOutboundScanning]] - `uses` [INFERRED]
- [[TestOwnerChannelFiltering]] - `uses` [INFERRED]
- [[TestProxyOutbound]] - `uses` [INFERRED]
- [[TestSessionIsolationEndToEnd]] - `uses` [INFERRED]
- [[TestSocketModeRelay]] - `uses` [INFERRED]
- [[TestUserSessionManager]] - `uses` [INFERRED]
- [[TestWebhookReceiverIntegration]] - `uses` [INFERRED]
- [[TestWebhookReceiverSlackExtraction]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[_PassInboundPipeline]] - `uses` [INFERRED]
- [[_StubForwarder_2]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[telegram_webhook()]] - `calls` [EXTRACTED]
- [[test_collaborator_tracker.py]] - `imports` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_session_isolation.py]] - `imports` [EXTRACTED]
- [[test_slack_proxy.py]] - `imports` [EXTRACTED]
- [[test_webhook_blocks_injection()]] - `calls` [EXTRACTED]
- [[test_webhook_outbound_block_withheld()]] - `calls` [EXTRACTED]
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `calls` [EXTRACTED]
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - `calls` [EXTRACTED]
- [[test_webhook_receiver_processes()]] - `calls` [EXTRACTED]
- [[test_webhook_strips_pii()]] - `calls` [EXTRACTED]
- [[webhook_receiver.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Middleware__Session_Isolation