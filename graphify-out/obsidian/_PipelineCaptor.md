---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "Community 104"
location: "L19"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_104
---

# _PipelineCaptor

## Connections
- [[.__init__()_156]] - `method` [EXTRACTED]
- [[._run_forward()]] - `references` [EXTRACTED]
- [[.process_inbound()_3]] - `method` [EXTRACTED]
- [[.process_outbound()_3]] - `method` [EXTRACTED]
- [[.test_agent_id_propagated_for_hermes()]] - `calls` [EXTRACTED]
- [[.test_agent_id_propagated_for_openclaw()]] - `calls` [EXTRACTED]
- [[.test_body_owner_id_with_matching_trusted_header_is_honored()]] - `calls` [EXTRACTED]
- [[.test_body_owner_id_without_trusted_header_is_stripped()]] - `calls` [EXTRACTED]
- [[.test_default_not_used_in_pipeline()]] - `calls` [EXTRACTED]
- [[.test_forward_passes_user_id_in_metadata_to_process_inbound()]] - `calls` [EXTRACTED]
- [[.test_non_owner_body_user_id_passes_through()]] - `calls` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[Minimal pipeline mock that records which agent_id it was called with.]] - `rationale_for` [EXTRACTED]
- [[_make_mock_app_state()]] - `references` [EXTRACTED]
- [[test_forward_routing.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_104