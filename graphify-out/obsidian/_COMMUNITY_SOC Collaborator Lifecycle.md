---
type: community
members: 117
---

# SOC Collaborator Lifecycle

**Members:** 117 nodes

## Members
- [[.__init__()_21]] - code - gateway/proxy/forwarder.py
- [[.__init__()_33]] - code - gateway/proxy/sidecar.py
- [[.__init__()_149]] - code - gateway/tests/test_e2e_proxy.py
- [[.__init__()_150]] - code - gateway/tests/test_e2e_proxy.py
- [[.forward()_1]] - code - gateway/proxy/forwarder.py
- [[.forward()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[.get_stats()_2]] - code - gateway/proxy/forwarder.py
- [[.get_stats()_7]] - code - gateway/proxy/sidecar.py
- [[.health_check()_1]] - code - gateway/proxy/forwarder.py
- [[.is_healthy()]] - code - gateway/proxy/forwarder.py
- [[.last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[.process_inbound()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[.process_outbound()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[.scan()]] - code - gateway/proxy/sidecar.py
- [[.set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[A pipeline-blocked outbound response must NOT be delivered.      Regression test]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_13]] - code - gateway/proxy/forwarder.py
- [[Any_20]] - code - gateway/proxy/sidecar.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[Check if the OpenClaw backend is healthy.]] - rationale - gateway/proxy/forwarder.py
- [[Configuration for the HTTP forwarder.]] - rationale - gateway/proxy/forwarder.py
- [[Configure egress filter to block a domain — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Forward a request to the OpenClaw backend.]] - rationale - gateway/proxy/forwarder.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[Forwarder stub returning a canned bot response body.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[If the outbound pipeline crashes, the bot response must be withheld.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Insert messages, modify a hash — verify chain integrity check fails.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Low-trust agent requests elevated action — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Message with both PII and injection — blocked before PII scan.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Mock OpenClaw response containing PII — verify stripped.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Pipeline stub inbound passes through; outbound behavior injectable.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Request to scan a message.]] - rationale - gateway/proxy/sidecar.py
- [[Response from sidecar scan.]] - rationale - gateway/proxy/sidecar.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[Scan a message through the security pipeline.]] - rationale - gateway/proxy/sidecar.py
- [[ScanRequest]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[Send 10 messages — verify all in ledger with valid SHA-256 chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send command requiring approval — verify queued, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send message with SSN — verify it's redacted before forwarding.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send prompt injection — verify blocked, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Sidecar security scanner — reduced security, traffic can bypass.      This is fo]] - rationale - gateway/proxy/sidecar.py
- [[SidecarScanner]] - code - gateway/proxy/sidecar.py
- [[Trigger freeze mode — verify pipeline blocks all traffic.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify allowed domains pass egress check.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify both inbound and outbound are in audit chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[Verify clean messages pass through without blocking.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify multiple injection patterns are detected.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify pipeline statistics are tracked correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify processing time is tracked.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify sidecar scanner works.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify that direct connection to OpenClaw internal port fails.      In Docker pr]] - rationale - gateway/tests/test_e2e_proxy.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder_2]] - code - gateway/tests/test_e2e_proxy.py
- [[canary.py]] - code - gateway/security/canary.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[forwarder()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[forwarder.py]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[pii_config()]] - code - gateway/tests/test_e2e_proxy.py
- [[pipeline()]] - code - gateway/tests/test_e2e_proxy.py
- [[prompt_guard()]] - code - gateway/tests/test_e2e_proxy.py
- [[run_canary()]] - code - gateway/security/canary.py
- [[sanitizer()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[sidecar.py]] - code - gateway/proxy/sidecar.py
- [[test_approval_queue_enforced()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_empty_valid()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_integrity()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_single_entry()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_canary.py]] - code - gateway/tests/test_canary.py
- [[test_canary_fails_without_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_message_contains_fake_pii()]] - code - gateway/tests/test_canary.py
- [[test_canary_passes_with_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_result_serialization()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_audit_chain()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_pii_stripping()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_clean_message_passes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_direct_bypass_blocked()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_e2e_proxy.py]] - code - gateway/tests/test_e2e_proxy.py
- [[test_egress_allowed_domain()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_egress_blocked()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_forwarder_error_handling()]] - code - gateway/tests/test_e2e_proxy.py
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
- [[test_webhook_outbound_block_withheld()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - code - gateway/tests/test_e2e_proxy.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOC_Collaborator_Lifecycle
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_SOC RBAC & Auth]]
- 12 edges to [[_COMMUNITY_Telegram Proxy Test Suite]]
- 8 edges to [[_COMMUNITY_Planning Docs]]
- 6 edges to [[_COMMUNITY_Audit Export Pipeline]]
- 6 edges to [[_COMMUNITY_MCP Policy Engine]]
- 4 edges to [[_COMMUNITY_Security Docs]]
- 3 edges to [[_COMMUNITY_Auth & Exception Types]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Slack API Proxy]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 52, connects to 9 communities
- [[_PassInboundPipeline]] - degree 23, connects to 9 communities
- [[_StubForwarder_2]] - degree 22, connects to 9 communities
- [[test_canary.py]] - degree 19, connects to 4 communities
- [[canary_pipeline()]] - degree 6, connects to 4 communities