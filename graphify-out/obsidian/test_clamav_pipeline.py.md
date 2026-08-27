---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "Community 331"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_331
---

# test_clamav_pipeline.py

## Connections
- [[PipelineAction]] - `imports` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[_b64_payload()]] - `contains` [EXTRACTED]
- [[_instant_wait_for()]] - `contains` [EXTRACTED]
- [[_make_pipeline()]] - `contains` [EXTRACTED]
- [[_timeout_wait_for()]] - `contains` [EXTRACTED]
- [[scan_bytes()]] - `imports` [EXTRACTED]
- [[test_canary.py]] - `semantically_similar_to` [INFERRED]
- [[test_pipeline_clamav_clean_payload()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_error_fail_open()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_malware_blocked()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_not_configured()]] - `contains` [EXTRACTED]
- [[test_pipeline_short_base64_not_scanned()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_binary_not_found()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_clean()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_empty_input()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_infected()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_timeout()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_331