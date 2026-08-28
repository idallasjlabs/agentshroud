---
source_file: "gateway/proxy/pipeline.py"
type: "rationale"
community: "PII Sanitizer & E2E Tests"
location: "L318"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__E2E_Tests
---

# Main security pipeline that all messages pass through.      Wires together: Prom

## Connections
- [[SecurityPipeline]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__E2E_Tests