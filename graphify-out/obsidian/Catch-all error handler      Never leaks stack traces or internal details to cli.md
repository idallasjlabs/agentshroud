---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L393"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Catch-all error handler      Never leaks stack traces or internal details to cli

## Connections
- [[global_exception_handler()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline