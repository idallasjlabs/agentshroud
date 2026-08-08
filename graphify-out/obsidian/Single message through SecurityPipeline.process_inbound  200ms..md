---
source_file: "gateway/tests/test_performance.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L291"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Single message through SecurityPipeline.process_inbound < 200ms.

## Connections
- [[.test_single_inbound_under_200ms()]] - `rationale_for` [EXTRACTED]
- [[.test_single_outbound_under_200ms()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline