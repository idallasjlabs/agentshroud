---
source_file: "gateway/tests/test_performance.py"
type: "code"
community: "Tool Result Sanitizer"
location: "L118"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Tool_Result_Sanitizer
---

# TestAuditChainPerformance

## Connections
- [[.ledger()]] - `method` [EXTRACTED]
- [[.test_1000_entries_under_5s()]] - `method` [EXTRACTED]
- [[.test_query_after_1000_entries()]] - `method` [EXTRACTED]
- [[Audit chain 1000 entries in  5s.]] - `rationale_for` [EXTRACTED]
- [[DataLedger]] - `uses` [INFERRED]
- [[LedgerConfig]] - `uses` [INFERRED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_performance.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Tool_Result_Sanitizer