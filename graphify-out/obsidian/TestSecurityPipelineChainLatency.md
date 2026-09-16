---
source_file: "gateway/tests/test_performance.py"
type: "code"
community: "Gateway Config & PII Sanitizer"
location: "L264"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Config__PII_Sanitizer
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
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[SecurityPipeline.process_inboundoutbound latency via the real pipeline class.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_performance.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Config__PII_Sanitizer