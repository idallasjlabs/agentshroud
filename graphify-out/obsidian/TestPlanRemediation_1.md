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
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()_1]] - `method` [EXTRACTED]
- [[.test_downstream_build_suffix_on_the_pin_is_ignored()_1]] - `method` [EXTRACTED]
- [[.test_empty_registry_is_a_no_op_plan()_1]] - `method` [EXTRACTED]
- [[.test_max_target_caps_the_bump()_1]] - `method` [EXTRACTED]
- [[.test_no_upgrade_needed_yields_no_target()_1]] - `method` [EXTRACTED]
- [[.test_only_under_review_entries_are_considered()_1]] - `method` [EXTRACTED]
- [[.test_picks_minimum_version_clearing_every_remediable_advisory()_1]] - `method` [EXTRACTED]
- [[.test_plan_is_serialisable_for_the_unattended_audit_trail()_1]] - `method` [EXTRACTED]
- [[.test_separates_advisories_already_fixed_at_the_current_pin()_1]] - `method` [EXTRACTED]
- [[.test_unparseable_fixed_in_is_treated_as_not_remediable()_1]] - `method` [EXTRACTED]
- [[RemediationPlan]] - `uses` [INFERRED]
- [[The planner decides WHAT bump remediates WHICH advisories.]] - `rationale_for` [EXTRACTED]
- [[test_auto_remediate_cves.py_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/plan_remediation