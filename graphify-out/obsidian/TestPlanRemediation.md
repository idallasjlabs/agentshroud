---
source_file: "gateway/tests/test_auto_remediate_cves.py"
type: "code"
community: "plan_remediation()"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/plan_remediation
---

# TestPlanRemediation

## Connections
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - `method` [EXTRACTED]
- [[.test_downstream_build_suffix_on_the_pin_is_ignored()]] - `method` [EXTRACTED]
- [[.test_empty_registry_is_a_no_op_plan()]] - `method` [EXTRACTED]
- [[.test_max_target_caps_the_bump()]] - `method` [EXTRACTED]
- [[.test_no_upgrade_needed_yields_no_target()]] - `method` [EXTRACTED]
- [[.test_only_under_review_entries_are_considered()]] - `method` [EXTRACTED]
- [[.test_picks_minimum_version_clearing_every_remediable_advisory()]] - `method` [EXTRACTED]
- [[.test_plan_is_serialisable_for_the_unattended_audit_trail()]] - `method` [EXTRACTED]
- [[.test_separates_advisories_already_fixed_at_the_current_pin()]] - `method` [EXTRACTED]
- [[.test_unparseable_fixed_in_is_treated_as_not_remediable()]] - `method` [EXTRACTED]
- [[The planner decides WHAT bump remediates WHICH advisories.]] - `rationale_for` [EXTRACTED]
- [[test_auto_remediate_cves.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/plan_remediation