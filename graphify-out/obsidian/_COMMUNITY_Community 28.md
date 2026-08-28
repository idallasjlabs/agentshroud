---
type: community
cohesion: 0.03
members: 111
---

# Community 28

**Cohesion:** 0.03 - loosely connected
**Members:** 111 nodes

## Members
- [[.__init__()_34]] - code - gateway/proxy/sidecar.py
- [[.__init__()_45]] - code - gateway/proxy/webhook_receiver.py
- [[.__init__()_154]] - code - gateway/tests/test_e2e_proxy.py
- [[.__init__()_153]] - code - gateway/tests/test_e2e_proxy.py
- [[._can_create_directory()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_message()]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_user_id()_1]] - code - gateway/proxy/webhook_receiver.py
- [[._extract_username()]] - code - gateway/proxy/webhook_receiver.py
- [[._prepare_session_payload()]] - code - gateway/proxy/webhook_receiver.py
- [[._replace_message()]] - code - gateway/proxy/webhook_receiver.py
- [[.forward()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[.get_stats()_7]] - code - gateway/proxy/sidecar.py
- [[.get_stats()_11]] - code - gateway/proxy/webhook_receiver.py
- [[.process_inbound()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[.process_outbound()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[.process_webhook()]] - code - gateway/proxy/webhook_receiver.py
- [[.scan()]] - code - gateway/proxy/sidecar.py
- [[.test_webhook_conversation_logging()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_session_context_injection()]] - code - gateway/tests/test_session_isolation.py
- [[.test_webhook_user_id_extraction()]] - code - gateway/tests/test_session_isolation.py
- [[.validate_signature()]] - code - gateway/proxy/webhook_receiver.py
- [[A pipeline-blocked outbound response must NOT be delivered.      Regression test]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_20]] - code - gateway/proxy/sidecar.py
- [[Any_24]] - code - gateway/proxy/webhook_receiver.py
- [[Check if we can create the given directory path.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[Configure egress filter to block a domain — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Extract display name from webhook payload.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract message text from webhook payload (Telegram format).]] - rationale - gateway/proxy/webhook_receiver.py
- [[Extract user ID from webhook payload based on source platform.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Forwarder stub returning a canned bot response body.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[If the outbound pipeline crashes, the bot response must be withheld.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Insert messages, modify a hash — verify chain integrity check fails.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Low-trust agent requests elevated action — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Message with both PII and injection — blocked before PII scan.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Mock OpenClaw response containing PII — verify stripped.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Path_4]] - code - gateway/proxy/webhook_receiver.py
- [[Pipeline stub inbound passes through; outbound behavior injectable.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Prepare payload with session context injection.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Process an incoming webhook through the security pipeline.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Receives webhooks and routes them through the security pipeline.      In product]] - rationale - gateway/proxy/webhook_receiver.py
- [[Replace message text in payload with sanitized version.]] - rationale - gateway/proxy/webhook_receiver.py
- [[Request to scan a message.]] - rationale - gateway/proxy/sidecar.py
- [[Response from sidecar scan.]] - rationale - gateway/proxy/sidecar.py
- [[Scan a message through the security pipeline.]] - rationale - gateway/proxy/sidecar.py
- [[ScanRequest]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[SecurityPipeline (external, referenced)]] - code - gateway/proxy/pipeline.py
- [[SecurityPipeline.process_inbound]] - code - gateway/proxy/pipeline.py
- [[Send 10 messages — verify all in ledger with valid SHA-256 chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send command requiring approval — verify queued, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send message with SSN — verify it's redacted before forwarding.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send prompt injection — verify blocked, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Sidecar security scanner — reduced security, traffic can bypass.      This is fo]] - rationale - gateway/proxy/sidecar.py
- [[SidecarScanner]] - code - gateway/proxy/sidecar.py
- [[Test that conversations are logged per user.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that session context is injected into forwarded requests.]] - rationale - gateway/tests/test_session_isolation.py
- [[Test that user IDs are properly extracted from webhook payloads.]] - rationale - gateway/tests/test_session_isolation.py
- [[Trigger freeze mode — verify pipeline blocks all traffic.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Validate the X-Telegram-Bot-Api-Secret-Token header.          Uses constant-time]] - rationale - gateway/proxy/webhook_receiver.py
- [[Verify allowed domains pass egress check.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify both inbound and outbound are in audit chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify clean messages pass through without blocking.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify multiple injection patterns are detected.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify pipeline statistics are tracked correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify processing time is tracked.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify sidecar scanner works.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify that direct connection to OpenClaw internal port fails.      In Docker pr]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[WebhookReceiver]] - code - gateway/proxy/webhook_receiver.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder_2]] - code - gateway/tests/test_e2e_proxy.py
- [[pii_config()]] - code - gateway/tests/test_e2e_proxy.py
- [[pipeline()]] - code - gateway/tests/test_e2e_proxy.py
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[prompt_guard()]] - code - gateway/tests/test_e2e_proxy.py
- [[sanitizer()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[sidecar.py]] - code - gateway/proxy/sidecar.py
- [[test_approval_queue_enforced()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_empty_valid()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_integrity()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_single_entry()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_clean_message_passes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_direct_bypass_blocked()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_e2e_proxy.py]] - code - gateway/tests/test_e2e_proxy.py
- [[test_egress_allowed_domain()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_egress_blocked()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_forwarder_mock()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_inbound_outbound_both_audited()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_kill_switch_freezes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_mixed_pii_and_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_multiple_prompt_patterns()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_outbound_pii_stripped()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_pii_stripped_inbound()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_pipeline_processing_time()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_pipeline_stats()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_prompt_injection_blocked()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_sidecar_scanner()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_tampered_audit_detected()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_trust_level_enforced()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_blocks_injection()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_outbound_block_withheld()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_28
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 12 edges to [[_COMMUNITY_Session Management]]
- 10 edges to [[_COMMUNITY_Community 65]]
- 7 edges to [[_COMMUNITY_Progressive Trust]]
- 6 edges to [[_COMMUNITY_Key Vault & Audit Chain]]
- 6 edges to [[_COMMUNITY_Community 74]]
- 4 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 4 edges to [[_COMMUNITY_Community 78]]
- 3 edges to [[_COMMUNITY_Community 159]]
- 3 edges to [[_COMMUNITY_Community 47]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 3 edges to [[_COMMUNITY_Community 50]]
- 3 edges to [[_COMMUNITY_Community 217]]
- 2 edges to [[_COMMUNITY_Community 618]]
- 1 edge to [[_COMMUNITY_Community 565]]
- 1 edge to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 83]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 53, connects to 8 communities
- [[_PassInboundPipeline]] - degree 23, connects to 8 communities
- [[_StubForwarder_2]] - degree 22, connects to 8 communities
- [[WebhookReceiver]] - degree 44, connects to 7 communities
- [[Path_4]] - degree 5, connects to 3 communities