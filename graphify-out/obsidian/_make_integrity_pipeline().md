---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L275"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Action__Instruction_Envelope
---

# _make_integrity_pipeline()

## Connections
- [[.test_high_score_forwards_and_records()]] - `calls` [EXTRACTED]
- [[.test_lockdown_block_is_audited()]] - `calls` [EXTRACTED]
- [[.test_lockdown_score_allows_owner()]] - `calls` [EXTRACTED]
- [[.test_lockdown_score_blocks_non_owner()]] - `calls` [EXTRACTED]
- [[.test_scorer_error_allows_owner()]] - `calls` [EXTRACTED]
- [[.test_scorer_error_fails_closed_non_owner()]] - `calls` [EXTRACTED]
- [[.test_scorer_invoked_with_session_segments()]] - `calls` [EXTRACTED]
- [[.test_warn_zone_forwards()]] - `calls` [EXTRACTED]
- [[AsyncMock]] - `calls` [INFERRED]
- [[Pipeline with ContextGuard + ContextIntegrityScorer mocks.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[_FakeIntegrityScore]] - `calls` [EXTRACTED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Action__Instruction_Envelope
