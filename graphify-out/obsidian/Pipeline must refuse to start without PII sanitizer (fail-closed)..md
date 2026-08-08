---
source_file: "gateway/tests/test_redteam_probes.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L319"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Pipeline must refuse to start without PII sanitizer (fail-closed).

## Connections
- [[test_pipeline_fails_closed_without_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline