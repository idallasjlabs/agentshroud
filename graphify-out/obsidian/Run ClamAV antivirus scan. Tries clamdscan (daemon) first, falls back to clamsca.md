---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L1479"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Run ClamAV antivirus scan. Tries clamdscan (daemon) first, falls back to clamsca

## Connections
- [[run_clamav_scan()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline