---
source_file: "gateway/tests/test_performance.py"
type: "rationale"
community: "Gateway Config & PII Sanitizer"
location: "L291"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Config__PII_Sanitizer
---

# Single message through SecurityPipeline.process_inbound < 200ms.

## Connections
- [[dot-test_single_inbound_under_200ms()]] - `rationale_for` [EXTRACTED]
- [[dot-test_single_outbound_under_200ms()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Config__PII_Sanitizer