---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "AgentShroud v0.7.0 Enforcement Audit Results"
location: "L105"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/AgentShroud_v070_Enforcement_Audit_Results
---

# write_pin()

## Connections
- [[.test_pin_revert_restores_the_exact_original_string()]] - `calls` [INFERRED]
- [[.test_write_pin_is_idempotent()]] - `calls` [INFERRED]
- [[.test_write_pin_refuses_an_absent_key()]] - `calls` [INFERRED]
- [[.test_write_pin_replaces_only_the_target_line()]] - `calls` [INFERRED]
- [[.test_write_pin_round_trips_through_read_pin()]] - `calls` [INFERRED]
- [[Path_42]] - `references` [EXTRACTED]
- [[Rewrite one pin in place, preserving every other line byte for byte.      Raises]] - `rationale_for` [EXTRACTED]
- [[apply_remediation()]] - `calls` [EXTRACTED]
- [[auto_remediate_cves.py]] - `contains` [EXTRACTED]
- [[test_pin_revert_restores_the_exact_original_string]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/AgentShroud_v070_Enforcement_Audit_Results