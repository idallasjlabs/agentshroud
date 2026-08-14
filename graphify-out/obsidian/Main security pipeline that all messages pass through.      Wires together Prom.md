---
source_file: "gateway/proxy/pipeline.py"
type: "rationale"
community: "SOC RBAC & Auth"
location: "L318"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# Main security pipeline that all messages pass through.      Wires together: Prom

## Connections
- [[SecurityPipeline]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_RBAC__Auth