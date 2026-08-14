---
source_file: "gateway/ingest_api/main.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L1478"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# run_clamav_scan()

## Connections
- [[AuthRequired]] - `references` [EXTRACTED]
- [[AuthRequired_5]] - `references` [EXTRACTED]
- [[Run ClamAV antivirus scan. Tries clamdscan (daemon) first, falls back to clamsca]] - `rationale_for` [EXTRACTED]
- [[_record_scanner_result()]] - `calls` [EXTRACTED]
- [[main.py_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline