---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L332"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Log all incoming requests      Never logs request bodies (may contain PII).

## Connections
- [[log_requests()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline