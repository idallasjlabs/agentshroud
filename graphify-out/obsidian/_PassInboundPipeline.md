---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "test_e2e_proxy.py"
location: "L421"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_e2e_proxypy
---

# _PassInboundPipeline

## Connections
- [[.__init__()_50]] - `method` [EXTRACTED]
- [[.process_inbound()_6]] - `method` [EXTRACTED]
- [[.process_outbound()_7]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[ForwarderConfig]] - `uses` [INFERRED]
- [[HTTPForwarder]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[Pipeline stub inbound passes through; outbound behavior injectable.]] - `rationale_for` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[ScanRequest]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[SidecarScanner]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[test_e2e_proxy.py]] - `contains` [EXTRACTED]
- [[test_webhook_outbound_block_withheld()]] - `calls` [EXTRACTED]
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_e2e_proxypy