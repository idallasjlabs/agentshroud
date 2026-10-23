---
source_file: "gateway/security/a2a_governance.py"
type: "code"
community: "api.py"
location: "L168"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/apipy
---

# A2AGovernanceProxy

## Connections
- [[dot-__init__()_150]] - `method` [EXTRACTED]
- [[dot-_check_message_size()]] - `method` [EXTRACTED]
- [[dot-_check_peer()]] - `method` [EXTRACTED]
- [[dot-_check_rate_limit()]] - `method` [EXTRACTED]
- [[dot-_check_task_concurrency()]] - `method` [EXTRACTED]
- [[dot-_finalize()]] - `method` [EXTRACTED]
- [[dot-_process()]] - `method` [EXTRACTED]
- [[dot-_sanitize_message()]] - `method` [EXTRACTED]
- [[dot-complete_task()]] - `method` [EXTRACTED]
- [[dot-get_events()_2]] - `method` [EXTRACTED]
- [[dot-get_peer()]] - `method` [EXTRACTED]
- [[dot-get_summary()_1]] - `method` [EXTRACTED]
- [[dot-process_inbound()_7]] - `method` [EXTRACTED]
- [[dot-process_outbound()_4]] - `method` [EXTRACTED]
- [[dot-register_peer()_1]] - `method` [EXTRACTED]
- [[dot-test_complete_task_frees_slot()]] - `calls` [EXTRACTED]
- [[dot-test_disabled_allows_all()]] - `calls` [EXTRACTED]
- [[dot-test_oversized_denied()]] - `calls` [EXTRACTED]
- [[dot-test_rate_limit_exceeded()_1]] - `calls` [EXTRACTED]
- [[dot-test_task_limit_exceeded()]] - `calls` [EXTRACTED]
- [[dot-unregister_peer()]] - `method` [EXTRACTED]
- [[dot-update_peer_trust()]] - `method` [EXTRACTED]
- [[A2ADecision]] - `shares_data_with` [EXTRACTED]
- [[A2AGovernanceConfig]] - `shares_data_with` [EXTRACTED]
- [[A2AGovernanceEvent]] - `calls` [EXTRACTED]
- [[A2AMessage]] - `shares_data_with` [EXTRACTED]
- [[A2APeer]] - `shares_data_with` [EXTRACTED]
- [[Governance proxy for Agent-to-Agent communication.      Sits between local agent]] - `rationale_for` [EXTRACTED]
- [[TestDisabledProxy]] - `uses` [INFERRED]
- [[TestInboundProcessing]] - `uses` [INFERRED]
- [[TestMessageFingerprint]] - `uses` [INFERRED]
- [[TestMessageSize]] - `uses` [INFERRED]
- [[TestOutboundProcessing]] - `uses` [INFERRED]
- [[TestPIISanitization]] - `uses` [INFERRED]
- [[TestPeerManagement]] - `uses` [INFERRED]
- [[TestRateLimiting_2]] - `uses` [INFERRED]
- [[TestReporting]] - `uses` [INFERRED]
- [[TestTaskConcurrency]] - `uses` [INFERRED]
- [[ToolACLEnforcer]] - `semantically_similar_to` [INFERRED]
- [[a2a_governance.py]] - `contains` [EXTRACTED]
- [[monitor_proxy()]] - `calls` [EXTRACTED]
- [[proxy()_3]] - `calls` [EXTRACTED]
- [[test_a2a_governance.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/apipy
