---
type: community
cohesion: 0.03
members: 119
---

# KillSwitchMonitor

**Cohesion:** 0.03 - loosely connected
**Members:** 119 nodes

## Members
- [[.__init__()_22]] - code - gateway/proxy/forwarder.py
- [[.__init__()_34]] - code - gateway/proxy/sidecar.py
- [[.__init__()_154]] - code - gateway/tests/test_e2e_proxy.py
- [[.__init__()_153]] - code - gateway/tests/test_e2e_proxy.py
- [[.forward()_1]] - code - gateway/proxy/forwarder.py
- [[.forward()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[.get_stats()_2]] - code - gateway/proxy/forwarder.py
- [[.get_stats()_7]] - code - gateway/proxy/sidecar.py
- [[.health_check()_1]] - code - gateway/proxy/forwarder.py
- [[.is_healthy()]] - code - gateway/proxy/forwarder.py
- [[.last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[.process_inbound()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[.process_outbound()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[.scan()]] - code - gateway/proxy/sidecar.py
- [[.set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[.to_dict()_6]] - code - gateway/security/canary.py
- [[A pipeline-blocked outbound response must NOT be delivered.      Regression test]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_13]] - code - gateway/proxy/forwarder.py
- [[Any_20]] - code - gateway/proxy/sidecar.py
- [[Any_33]] - code - gateway/security/canary.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
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
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[Scan a message through the security pipeline.]] - rationale - gateway/proxy/sidecar.py
- [[ScanRequest]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[SecurityPipeline (external, referenced)]] - code - gateway/proxy/pipeline.py
- [[SecurityPipeline.process_inbound]] - code - gateway/proxy/pipeline.py
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
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify multiple injection patterns are detected.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify pipeline statistics are tracked correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify processing time is tracked.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify sidecar scanner works.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify that direct connection to OpenClaw internal port fails.      In Docker pr]] - rationale - gateway/tests/test_e2e_proxy.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder_2]] - code - gateway/tests/test_e2e_proxy.py
- [[canary-cron.sh embedded Python main()]] - code - scripts/canary-cron.sh
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
- [[test_audit_chain_integrity()]] - code - gateway/tests/test_e2e_proxy.py
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
TABLE source_file, type FROM #community/KillSwitchMonitor
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_RBACConfig]]
- 14 edges to [[_COMMUNITY_ResourceGuard]]
- 8 edges to [[_COMMUNITY_GitHub Copilot CLI Setup Guide]]
- 7 edges to [[_COMMUNITY_ServiceManager]]
- 5 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 4 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 3 edges to [[_COMMUNITY_falco_monitor.py]]
- 3 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 3 edges to [[_COMMUNITY_awslabs.aws-api-mcp-server configuration (--read]]
- 3 edges to [[_COMMUNITY_ConsentFramework]]
- 3 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_Socrates — Dialogue Architect]]
- 1 edge to [[_COMMUNITY_AgentShroud™ — Trademark Prior Use Record]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 53, connects to 11 communities
- [[_PassInboundPipeline]] - degree 23, connects to 10 communities
- [[_StubForwarder_2]] - degree 22, connects to 10 communities
- [[test_canary.py]] - degree 21, connects to 6 communities
- [[run_canary()]] - degree 20, connects to 5 communities