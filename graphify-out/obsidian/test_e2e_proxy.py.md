---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "Sidecar Security Scanner"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Sidecar_Security_Scanner
---

# test_e2e_proxy.py

## Connections
- [[AuditChain]] - `imports` [EXTRACTED]
- [[EgressFilter_1]] - `imports` [EXTRACTED]
- [[EgressFilterConfig]] - `imports` [EXTRACTED]
- [[EgressPolicy]] - `imports` [EXTRACTED]
- [[ForwarderConfig]] - `imports` [EXTRACTED]
- [[HTTPForwarder]] - `imports` [EXTRACTED]
- [[PIIConfig]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[PipelineAction]] - `imports` [EXTRACTED]
- [[PromptGuard]] - `imports` [EXTRACTED]
- [[ScanRequest]] - `imports` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[SidecarScanner]] - `imports` [EXTRACTED]
- [[TrustConfig]] - `imports` [EXTRACTED]
- [[TrustManager]] - `imports` [EXTRACTED]
- [[WebhookReceiver]] - `imports` [EXTRACTED]
- [[_PassInboundPipeline]] - `contains` [EXTRACTED]
- [[_StubForwarder]] - `contains` [EXTRACTED]
- [[egress_filter()]] - `contains` [EXTRACTED]
- [[forwarder()]] - `contains` [EXTRACTED]
- [[pii_config()]] - `contains` [EXTRACTED]
- [[pipeline()]] - `contains` [EXTRACTED]
- [[prompt_guard()]] - `contains` [EXTRACTED]
- [[sanitizer()_1]] - `contains` [EXTRACTED]
- [[test_approval_queue_enforced()]] - `contains` [EXTRACTED]
- [[test_audit_chain_empty_valid()]] - `contains` [EXTRACTED]
- [[test_audit_chain_integrity()]] - `contains` [EXTRACTED]
- [[test_audit_chain_single_entry()]] - `contains` [EXTRACTED]
- [[test_clean_message_passes()]] - `contains` [EXTRACTED]
- [[test_direct_bypass_blocked()]] - `contains` [EXTRACTED]
- [[test_egress_allowed_domain()]] - `contains` [EXTRACTED]
- [[test_egress_blocked()]] - `contains` [EXTRACTED]
- [[test_forwarder_error_handling()]] - `contains` [EXTRACTED]
- [[test_forwarder_mock()]] - `contains` [EXTRACTED]
- [[test_inbound_outbound_both_audited()]] - `contains` [EXTRACTED]
- [[test_kill_switch_freezes()]] - `contains` [EXTRACTED]
- [[test_mixed_pii_and_injection()]] - `contains` [EXTRACTED]
- [[test_multiple_prompt_patterns()]] - `contains` [EXTRACTED]
- [[test_outbound_pii_stripped()]] - `contains` [EXTRACTED]
- [[test_pii_stripped_inbound()]] - `contains` [EXTRACTED]
- [[test_pipeline_processing_time()]] - `contains` [EXTRACTED]
- [[test_pipeline_stats()]] - `contains` [EXTRACTED]
- [[test_prompt_injection_blocked()]] - `contains` [EXTRACTED]
- [[test_sidecar_scanner()]] - `contains` [EXTRACTED]
- [[test_tampered_audit_detected()]] - `contains` [EXTRACTED]
- [[test_trust_level_enforced()]] - `contains` [EXTRACTED]
- [[test_webhook_blocks_injection()]] - `contains` [EXTRACTED]
- [[test_webhook_outbound_block_withheld()]] - `contains` [EXTRACTED]
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `contains` [EXTRACTED]
- [[test_webhook_receiver_processes()]] - `contains` [EXTRACTED]
- [[test_webhook_strips_pii()]] - `contains` [EXTRACTED]
- [[trust_manager()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Sidecar_Security_Scanner