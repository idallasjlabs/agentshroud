---
type: community
cohesion: 0.04
members: 74
---

# EgressFilterConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 74 nodes

## Members
- [[dot-__init__()_189]] - code - gateway/proxy/sidecar.py
- [[dot-__init__()_190]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-__init__()_191]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-forward()_4]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-get_stats()_19]] - code - gateway/proxy/sidecar.py
- [[dot-process_inbound()_10]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-process_outbound()_7]] - code - gateway/tests/test_e2e_proxy.py
- [[dot-scan()_4]] - code - gateway/proxy/sidecar.py
- [[A pipeline-blocked outbound response must NOT be delivered.      Regression test]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Any_81]] - code - gateway/proxy/sidecar.py
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
- [[ScanRequest_1]] - code - gateway/proxy/sidecar.py
- [[ScanResponse]] - code - gateway/proxy/sidecar.py
- [[SecurityPipeline (external, referenced)]] - code - gateway/proxy/pipeline.py
- [[SecurityPipeline.process_inbound]] - code - gateway/proxy/pipeline.py
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
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify forwarder mock works correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify multiple injection patterns are detected.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify pipeline statistics are tracked correctly.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify processing time is tracked.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify sidecar scanner works.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify that direct connection to OpenClaw internal port fails.      In Docker pr]] - rationale - gateway/tests/test_e2e_proxy.py
- [[_PassInboundPipeline]] - code - gateway/tests/test_e2e_proxy.py
- [[_StubForwarder_2]] - code - gateway/tests/test_e2e_proxy.py
- [[egress_filter()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[pii_config()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[prompt_guard()_2]] - code - gateway/tests/test_e2e_proxy.py
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
- [[test_webhook_outbound_block_withheld()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - code - gateway/tests/test_e2e_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_PipelineAction]]
- 9 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig]]
- 8 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 7 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 4 edges to [[_COMMUNITY_ContextSegment]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_egress_filter.py_3]]

## Top bridge nodes
- [[test_e2e_proxy.py]] - degree 53, connects to 10 communities
- [[_PassInboundPipeline]] - degree 23, connects to 9 communities
- [[_StubForwarder_2]] - degree 22, connects to 9 communities
- [[SidecarScanner]] - degree 13, connects to 2 communities
- [[egress_filter()_1]] - degree 4, connects to 2 communities
