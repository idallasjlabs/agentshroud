---
source_file: "gateway/tests/test_e2e.py"
type: "code"
community: "ingest_api/main.py"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# test_forward_pii_sanitized_and_ledger_entry()

## Connections
- [[EventBus]] - `uses` [INFERRED]
- [[Forward content → PII sanitized → ledger entry created → event bus fired.]] - `rationale_for` [EXTRACTED]
- [[Role]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[asyncio_69]] - `references` [EXTRACTED]
- [[test_e2e.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ingest_api/mainpy
