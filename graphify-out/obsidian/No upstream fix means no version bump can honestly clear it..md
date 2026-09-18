---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "rationale"
community: "plan_remediation()"
location: "L96"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/plan_remediation
---

# No upstream fix means no version bump can honestly clear it.

## Connections
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - `rationale_for` [EXTRACTED]
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/plan_remediation