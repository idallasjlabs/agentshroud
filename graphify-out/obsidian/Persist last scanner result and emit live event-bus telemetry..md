---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L1430"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Persist last scanner result and emit live event-bus telemetry.

## Connections
- [[_record_scanner_result()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline