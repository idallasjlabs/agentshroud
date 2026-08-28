---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "rationale"
community: "PII Sanitizer & E2E Tests"
location: "L411"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__E2E_Tests
---

# Pipeline must BLOCK (not pass through) when OutputCanary crashes for non-owner.

## Connections
- [[test_pipeline_fails_closed_on_output_canary_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__E2E_Tests