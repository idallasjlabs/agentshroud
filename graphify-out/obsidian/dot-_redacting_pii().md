---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L741"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# ._redacting_pii()

## Connections
- [[dot-test_non_owner_inbound_query_still_redacted()]] - `calls` [EXTRACTED]
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[PII sanitiser mock that simulates two entity redactions.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPIIOwnerExemption]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Signed_Instruction_Envelopes__Security_Pipeline