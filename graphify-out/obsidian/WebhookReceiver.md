---
source_file: "gateway/proxy/webhook_receiver.py"
type: "code"
community: "WebhookReceiver"
location: "L29"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/WebhookReceiver
---

# WebhookReceiver

## Connections
- [[dot-__init__()_181]] - `method` [EXTRACTED]
- [[dot-_can_create_directory()]] - `method` [EXTRACTED]
- [[dot-_extract_message()]] - `method` [EXTRACTED]
- [[dot-_extract_user_id()_1]] - `method` [EXTRACTED]
- [[dot-_extract_username()]] - `method` [EXTRACTED]
- [[dot-_prepare_session_payload()]] - `method` [EXTRACTED]
- [[dot-_replace_message()]] - `method` [EXTRACTED]
- [[dot-get_stats()_16]] - `method` [EXTRACTED]
- [[dot-process_webhook()]] - `method` [EXTRACTED]
- [[dot-test_webhook_conversation_logging()]] - `calls` [EXTRACTED]
- [[dot-test_webhook_session_context_injection()]] - `calls` [EXTRACTED]
- [[dot-test_webhook_user_id_extraction()]] - `calls` [EXTRACTED]
- [[RBACConfig]] - `uses` [INFERRED]
- [[Receives webhooks and routes them through the security pipeline. In production,…]] - `rationale_for` [EXTRACTED]
- [[TestWebhookReceiverIntegration]] - `uses` [INFERRED]
- [[TestWebhookReceiverSlackExtraction]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[telegram_webhook()]] - `uses` [INFERRED]
- [[test_collaborator_tracker.py]] - `imports` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_session_isolation.py]] - `imports` [EXTRACTED]
- [[test_slack_proxy.py]] - `imports` [EXTRACTED]
- [[test_webhook_blocks_injection()]] - `uses` [INFERRED]
- [[test_webhook_outbound_block_withheld()]] - `uses` [INFERRED]
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `uses` [INFERRED]
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - `uses` [INFERRED]
- [[test_webhook_receiver_processes()]] - `uses` [INFERRED]
- [[test_webhook_strips_pii()]] - `uses` [INFERRED]
- [[webhook_receiver.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/WebhookReceiver
