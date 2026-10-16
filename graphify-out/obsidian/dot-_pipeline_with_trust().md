---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "AuditChain"
location: "L841"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# ._pipeline_with_trust()

## Connections
- [[dot-test_blocked_request_decays_trust_score()]] - `calls` [EXTRACTED]
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - `calls` [EXTRACTED]
- [[dot-test_clean_request_does_not_touch_trust_score()]] - `calls` [EXTRACTED]
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[SecurityPipeline_2]] - `calls` [EXTRACTED]
- [[TestTrustViolationRecording]] - `method` [EXTRACTED]
- [[TrustConfig]] - `calls` [EXTRACTED]
- [[TrustManager_4]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain
