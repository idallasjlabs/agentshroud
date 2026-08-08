---
source_file: "gateway/ingest_api/sanitizer.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L100"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Initialize Microsoft Presidio engines          Falls back to regex if Presidio/s

## Connections
- [[._init_presidio()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline