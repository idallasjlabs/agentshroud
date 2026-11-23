---
source_file: "gateway/tests/test_scanner_integration.py"
type: "rationale"
community: "get_trivy_image_summaries"
location: "L1168"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_trivy_image_summaries
---

# A JSON-corrupt file is silently skipped, others are still returned.

## Connections
- [[dot-test_corrupt_report_file_is_skipped()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_trivy_image_summaries
