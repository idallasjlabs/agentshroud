---
source_file: "gateway/security/a2a_governance.py"
type: "code"
community: "Community 44"
location: "L168"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_44
---

# A2AGovernanceProxy

## Connections
- [[.__init__()_49]] - `method` [EXTRACTED]
- [[._check_message_size()]] - `method` [EXTRACTED]
- [[._check_peer()]] - `method` [EXTRACTED]
- [[._check_rate_limit()]] - `method` [EXTRACTED]
- [[._check_task_concurrency()]] - `method` [EXTRACTED]
- [[._finalize()]] - `method` [EXTRACTED]
- [[._process()]] - `method` [EXTRACTED]
- [[._sanitize_message()]] - `method` [EXTRACTED]
- [[.complete_task()]] - `method` [EXTRACTED]
- [[.get_events()_1]] - `method` [EXTRACTED]
- [[.get_peer()]] - `method` [EXTRACTED]
- [[.get_summary()]] - `method` [EXTRACTED]
- [[.process_inbound()_1]] - `method` [EXTRACTED]
- [[.process_outbound()_1]] - `method` [EXTRACTED]
- [[.register_peer()]] - `method` [EXTRACTED]
- [[.test_complete_task_frees_slot()]] - `calls` [EXTRACTED]
- [[.test_disabled_allows_all()]] - `calls` [EXTRACTED]
- [[.test_oversized_denied()]] - `calls` [EXTRACTED]
- [[.test_rate_limit_exceeded()]] - `calls` [EXTRACTED]
- [[.test_task_limit_exceeded()]] - `calls` [EXTRACTED]
- [[.unregister_peer()]] - `method` [EXTRACTED]
- [[.update_peer_trust()]] - `method` [EXTRACTED]
- [[Governance proxy for Agent-to-Agent communication.      Sits between local agent]] - `rationale_for` [EXTRACTED]
- [[TestDisabledProxy]] - `uses` [INFERRED]
- [[TestInboundProcessing]] - `uses` [INFERRED]
- [[TestMessageFingerprint]] - `uses` [INFERRED]
- [[TestMessageSize]] - `uses` [INFERRED]
- [[TestOutboundProcessing]] - `uses` [INFERRED]
- [[TestPIISanitization]] - `uses` [INFERRED]
- [[TestPeerManagement]] - `uses` [INFERRED]
- [[TestRateLimiting]] - `uses` [INFERRED]
- [[TestReporting]] - `uses` [INFERRED]
- [[TestTaskConcurrency]] - `uses` [INFERRED]
- [[a2a_governance.py]] - `contains` [EXTRACTED]
- [[monitor_proxy()]] - `calls` [EXTRACTED]
- [[proxy()]] - `calls` [EXTRACTED]
- [[test_a2a_governance.py]] - `tests` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_44