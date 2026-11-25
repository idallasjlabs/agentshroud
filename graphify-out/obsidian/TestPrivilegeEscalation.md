---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "TestPrivilegeEscalation"
location: "L511"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestPrivilegeEscalation
---

# TestPrivilegeEscalation

## Connections
- [[dot-test_consent_required_for_sensitive_ops()]] - `method` [EXTRACTED]
- [[dot-test_session_cannot_impersonate()]] - `method` [EXTRACTED]
- [[dot-test_subagent_monitor_tracks_events()]] - `method` [EXTRACTED]
- [[dot-test_trust_cannot_exceed_max()]] - `method` [EXTRACTED]
- [[dot-test_unregistered_agent_blocked()]] - `method` [EXTRACTED]
- [[dot-test_violation_drops_trust_significantly()]] - `method` [EXTRACTED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[Test trust boundaries and privilege escalation prevention.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestPrivilegeEscalation
