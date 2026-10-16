---
source_file: "gateway/tests/test_e2e_proxy.py"
type: "code"
community: "EgressFilterConfig"
location: "L421"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/EgressFilterConfig
---

# _PassInboundPipeline

## Connections
- [[dot-__init__()_190]] - `method` [EXTRACTED]
- [[dot-process_inbound()_10]] - `method` [EXTRACTED]
- [[dot-process_outbound()_7]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[ForwarderConfig]] - `uses` [INFERRED]
- [[HTTPForwarder]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[Pipeline stub inbound passes through; outbound behavior injectable.]] - `rationale_for` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[ScanRequest_1]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[SidecarScanner]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_4]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[test_e2e_proxy.py]] - `contains` [EXTRACTED]
- [[test_webhook_outbound_block_withheld()]] - `calls` [EXTRACTED]
- [[test_webhook_outbound_pipeline_crash_fails_closed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/EgressFilterConfig
