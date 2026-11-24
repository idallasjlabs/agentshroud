---
type: community
members: 85
---

# test_e2e_proxy.py

**Members:** 85 nodes

## Members
- [[dot-__init__()_122]] - code - gateway/proxy/sidecar.py
- [[dot-__init__()_123]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-__init__()_124]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-forward()]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-get_stats()_9]] - code - gateway/proxy/sidecar.py
- [[dot-process_inbound()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-process_outbound()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-scan()_2]] - code - gateway/proxy/sidecar.py
- [[A pipeline-blocked outbound response must NOT be delivered. Regression test…]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_43]] - code
- [[Configure egress filter to block a domain — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[E2E Proxy Pipeline Tests — verify security pipeline actually works. These tests…]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Forwarder stub returning a canned bot response body.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[If the outbound pipeline crashes, the bot response must be withheld.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Insert messages, modify a hash — verify chain integrity check fails.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Low-trust agent requests elevated action — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Message with both PII and injection — blocked before PII scan.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Mock OpenClaw response containing PII — verify stripped.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Pipeline stub inbound passes through; outbound behavior injectable.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Request to scan a message.]] - rationale - gateway/proxy/sidecar.py
- [[Response from sidecar scan.]] - rationale - gateway/proxy/sidecar.py
- [[Scan a message through the security pipeline.]] - rationale - gateway/proxy/sidecar.py
- [[ScanRequest_1]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[Send 10 messages — verify all in ledger with valid SHA-256 chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send command requiring approval — verify queued, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send message with SSN — verify it's redacted before forwarding.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send prompt injection — verify blocked, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Sidecar security scanner — reduced security, traffic can bypass. This is for…]] - rationale - gateway/proxy/sidecar.py
- [[SidecarScanner]] - code - gateway/proxy/sidecar.py
- [[Trigger freeze mode — verify pipeline blocks all traffic.]] - rationale - gateway/tests/test_e2e_proxy.py
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
- [[Verify that direct connection to OpenClaw internal port fails. In Docker proxy…]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver blocks prompt injection.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver routes through pipeline.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify webhook receiver strips PII.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder]] - code - gateway/tests/test_e2e_proxy.py
- [[asyncio_50]] - code
- [[blocking_outbound()]] - code - gateway/tests/test_e2e_proxy.py
- [[crashing_outbound()]] - code - gateway/tests/test_e2e_proxy.py
- [[fixture_88]] - code
- [[forwarder()]] - code - gateway/tests/test_e2e_proxy.py
- [[pii_config()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[pipeline()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[prompt_guard()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[sanitizer()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[sidecar.py_2]] - code - gateway/proxy/sidecar.py
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
- [[test_webhook_receiver_processes()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_strips_pii()]] - code - gateway/tests/test_e2e_proxy.py
- [[trust_manager()_3]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2e_proxypy
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_PipelineAction]]
- 8 edges to [[_COMMUNITY_lifespan.py]]
- 7 edges to [[_COMMUNITY_UserSessionManager]]
- 7 edges to [[_COMMUNITY_HTTPForwarder]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 6 edges to [[_COMMUNITY_EgressFilter]]
- 5 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 63, connects to 10 communities
- [[test_inbound_outbound_both_audited()]] - degree 5, connects to 2 communities
- [[asyncio_50]] - degree 27, connects to 1 community
- [[test_webhook_outbound_block_withheld()]] - degree 7, connects to 1 community
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - degree 7, connects to 1 community
