---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "PIISanitizer"
location: "L724"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIISanitizer
---

# TestInboundPIIOwnerExemption

## Connections
- [[dot-_redacting_pii()]] - `method` [EXTRACTED]
- [[dot-test_non_owner_inbound_query_still_redacted()]] - `method` [EXTRACTED]
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - `method` [EXTRACTED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[Step 2 PII sanitisation must be skipped for the authenticated owner. Non-owner…]] - `rationale_for` [EXTRACTED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIISanitizer
