---
source_file: "gateway/tests/test_performance.py"
type: "code"
community: "Tool Result Sanitizer"
location: "L208"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Tool_Result_Sanitizer
---

# TestFullPipelineLatency

## Connections
- [[.ledger()_1]] - `method` [EXTRACTED]
- [[.test_single_message_pipeline_under_100ms()]] - `method` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[End-to-end pipeline latency for a single message.]] - `rationale_for` [EXTRACTED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_performance.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Tool_Result_Sanitizer