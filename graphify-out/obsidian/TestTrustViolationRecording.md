---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "asyncio"
location: "L833"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# TestTrustViolationRecording

## Connections
- [[dot-_pipeline_with_trust()]] - `method` [EXTRACTED]
- [[dot-test_blocked_request_decays_trust_score()]] - `method` [EXTRACTED]
- [[dot-test_blocked_request_propagates_to_cross_bot_peer()]] - `method` [EXTRACTED]
- [[dot-test_clean_request_does_not_touch_trust_score()]] - `method` [EXTRACTED]
- [[dot-test_missing_trust_manager_does_not_raise()]] - `method` [EXTRACTED]
- [[dot-test_owner_exempted_block_does_not_decay_trust()]] - `method` [EXTRACTED]
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that fires…]] - `rationale_for` [EXTRACTED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio
