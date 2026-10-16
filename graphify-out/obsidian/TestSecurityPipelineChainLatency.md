---
source_file: "gateway/tests/test_performance.py"
type: "code"
community: "PIIConfig"
location: "L264"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIIConfig
---

# TestSecurityPipelineChainLatency

## Connections
- [[dot-pipeline()_1]] - `method` [EXTRACTED]
- [[dot-test_100_inbound_messages_under_5s()]] - `method` [EXTRACTED]
- [[dot-test_100_outbound_messages_under_5s()]] - `method` [EXTRACTED]
- [[dot-test_pii_inbound_latency()]] - `method` [EXTRACTED]
- [[dot-test_single_inbound_under_200ms()]] - `method` [EXTRACTED]
- [[dot-test_single_outbound_under_200ms()]] - `method` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer_1]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[SecurityPipeline.process_inboundoutbound latency via the real pipeline class.]] - `rationale_for` [EXTRACTED]
- [[TrustManager_4]] - `uses` [INFERRED]
- [[test_performance.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIIConfig
