---
source_file: "gateway/ingest_api/sanitizer.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L271"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Sanitize using regex patterns (fallback mode)          Detects:         - US_SSN

## Connections
- [[._sanitize_regex()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline