---
source_file: "gateway/tests/test_subagent_governance.py"
type: "code"
community: "Subagent Governance"
location: "L161"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Subagent_Governance
---

# TestOutputTrustScoring

## Connections
- [[.test_api_key_detected()]] - `method` [EXTRACTED]
- [[.test_clean_output_high_score()]] - `method` [EXTRACTED]
- [[.test_exfil_pattern_detected()]] - `method` [EXTRACTED]
- [[.test_injection_detected()]] - `method` [EXTRACTED]
- [[.test_low_agent_trust_penalty()]] - `method` [EXTRACTED]
- [[.test_pii_detected_lowers_score()]] - `method` [EXTRACTED]
- [[GovernanceAction]] - `uses` [INFERRED]
- [[GovernanceConfig]] - `uses` [INFERRED]
- [[GovernanceEventType]] - `uses` [INFERRED]
- [[OutputTrustConfig]] - `uses` [INFERRED]
- [[PrivilegePolicy]] - `uses` [INFERRED]
- [[ResourceBudget]] - `uses` [INFERRED]
- [[SubagentGovernance]] - `uses` [INFERRED]
- [[test_subagent_governance.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Subagent_Governance