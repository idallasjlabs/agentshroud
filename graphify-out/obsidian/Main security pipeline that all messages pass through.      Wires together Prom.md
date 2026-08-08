---
source_file: "gateway/proxy/pipeline.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L318"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Main security pipeline that all messages pass through.      Wires together: Prom

## Connections
- [[SecurityPipeline]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline