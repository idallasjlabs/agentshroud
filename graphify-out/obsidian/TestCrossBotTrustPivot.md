---
source_file: "gateway/tests/test_security_regressions_v1_2.py"
type: "code"
community: "Community 26"
location: "L160"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_26
---

# TestCrossBotTrustPivot

## Connections
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - `method` [EXTRACTED]
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - `method` [EXTRACTED]
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - `method` [EXTRACTED]
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - `rationale_for` [EXTRACTED]
- [[SharedMemoryManager]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[test_security_regressions_v1_2.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_26