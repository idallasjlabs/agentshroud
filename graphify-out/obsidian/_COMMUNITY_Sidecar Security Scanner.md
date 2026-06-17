---
type: community
cohesion: 0.04
members: 70
---

# Sidecar Security Scanner

**Cohesion:** 0.04 - loosely connected
**Members:** 70 nodes

## Members
- [[.__init__()_26]] - code - gateway/proxy/sidecar.py
- [[.__init__()_116]] - code - gateway/tests/test_e2e_proxy.py
- [[.__init__()_115]] - code - gateway/tests/test_e2e_proxy.py
- [[.forward()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[.get_stats()_7]] - code - gateway/proxy/sidecar.py
- [[.process_inbound()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[.process_outbound()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[.scan()]] - code - gateway/proxy/sidecar.py
- [[A pipeline-blocked outbound response must NOT be delivered.      Regression test]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_17]] - code - gateway/proxy/sidecar.py
- [[Configure egress filter to block a domain — verify denied.]] - rationale - gateway/tests/test_e2e_proxy.py
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
- [[ScanRequest]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[Send 10 messages — verify all in ledger with valid SHA-256 chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send command requiring approval — verify queued, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send message with SSN — verify it's redacted before forwarding.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Send prompt injection — verify blocked, not forwarded.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Sidecar security scanner — reduced security, traffic can bypass.      This is fo]] - rationale - gateway/proxy/sidecar.py
- [[SidecarScanner]] - code - gateway/proxy/sidecar.py
- [[Trigger freeze mode — verify pipeline blocks all traffic.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify allowed domains pass egress check.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify both inbound and outbound are in audit chain.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify clean messages pass through without blocking.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify multiple injection patterns are detected.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify pipeline statistics are tracked correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify processing time is tracked.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify sidecar scanner works.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify that direct connection to OpenClaw internal port fails.      In Docker pr]] - rationale - gateway/tests/test_e2e_proxy.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder]] - code - gateway/tests/test_e2e_proxy.py
- [[pii_config()]] - code - gateway/tests/test_e2e_proxy.py
- [[pipeline()]] - code - gateway/tests/test_e2e_proxy.py
- [[prompt_guard()]] - code - gateway/tests/test_e2e_proxy.py
- [[sanitizer()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[sidecar.py]] - code - gateway/proxy/sidecar.py
- [[test_approval_queue_enforced()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_integrity()]] - code - gateway/tests/test_e2e_proxy.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Sidecar_Security_Scanner
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 9 edges to [[_COMMUNITY_Module Group 92]]
- 8 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 8 edges to [[_COMMUNITY_Webhook Receiver]]
- 7 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 4 edges to [[_COMMUNITY_Module Group 88]]
- 4 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 3 edges to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 3 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 3 edges to [[_COMMUNITY_Module Group 71]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 52, connects to 10 communities
- [[_PassInboundPipeline]] - degree 23, connects to 10 communities
- [[_StubForwarder]] - degree 22, connects to 10 communities
- [[test_forwarder_error_handling()]] - degree 5, connects to 1 community
- [[test_inbound_outbound_both_audited()]] - degree 5, connects to 1 community