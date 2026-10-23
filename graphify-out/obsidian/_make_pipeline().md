---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "asyncio"
location: "L113"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# _make_pipeline()

## Connections
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - `rationale_for` [EXTRACTED]
- [[_passthrough()]] - `indirect_call` [INFERRED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_clean_payload()]] - `calls` [EXTRACTED]
- [[test_pipeline_clamav_error_fail_open()]] - `calls` [EXTRACTED]
- [[test_pipeline_clamav_malware_blocked()]] - `calls` [EXTRACTED]
- [[test_pipeline_clamav_not_configured()]] - `calls` [EXTRACTED]
- [[test_pipeline_short_base64_not_scanned()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio
