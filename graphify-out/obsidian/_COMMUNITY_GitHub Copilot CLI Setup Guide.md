---
type: community
cohesion: 0.06
members: 47
---

# GitHub Copilot CLI Setup Guide

**Cohesion:** 0.06 - loosely connected
**Members:** 47 nodes

## Members
- [[.__init__()_45]] - code - gateway/proxy/webhook_receiver.py
- [[._can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[._prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[._replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[.get_stats()_11]] - code - gateway/proxy/webhook_receiver.py
- [[.mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[.mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[.process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[.session_manager()_1]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()]] - code - gateway/tests/test_session_isolation.py
- [[.temp_workspace()_1]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[.validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[Any_24]] - code - gateway/proxy/webhook_receiver.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a session manager.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a temporary workspace for testing.]] - rationale - gateway/tests/test_session_isolation.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Path_4]] - code - gateway/proxy/webhook_receiver.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Test WebhookReceiver integration with session isolation.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[TestWebhookReceiverIntegration]] - code - gateway/tests/test_session_isolation.py
- [[Validate the X-Telegram-Bot-Api-Secret-Token header.          Uses constant-time]] - rationale - gateway/proxy/webhook_receiver.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py
- [[webhook_receiver.py]] - code - gateway/proxy/webhook_receiver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitHub_Copilot_CLI_Setup_Guide
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 7 edges to [[_COMMUNITY_KeyVaultConfig]]
- 6 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 4 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 3 edges to [[_COMMUNITY_RateLimiter]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_input_normalizer.py]]
- 2 edges to [[_COMMUNITY_Pre-Purge Secret Rotation Checklist]]
- 2 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_Remediation]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[WebhookReceiver]] - degree 44, connects to 10 communities
- [[TestWebhookReceiverIntegration]] - degree 13, connects to 4 communities
- [[Path_4]] - degree 5, connects to 3 communities
- [[webhook_receiver.py]] - degree 4, connects to 3 communities
- [[Any_24]] - degree 9, connects to 2 communities