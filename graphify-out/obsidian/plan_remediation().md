---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "PHASE_3A_3B_IMPLEMENTATION.md"
location: "L169"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PHASE_3A_3B_IMPLEMENTATIONmd
---

# plan_remediation()

## Connections
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - `calls` [INFERRED]
- [[.test_downstream_build_suffix_on_the_pin_is_ignored()]] - `calls` [INFERRED]
- [[.test_empty_registry_is_a_no_op_plan()]] - `calls` [INFERRED]
- [[.test_max_target_caps_the_bump()]] - `calls` [INFERRED]
- [[.test_no_upgrade_needed_yields_no_target()]] - `calls` [INFERRED]
- [[.test_only_under_review_entries_are_considered()]] - `calls` [INFERRED]
- [[.test_picks_minimum_version_clearing_every_remediable_advisory()]] - `calls` [INFERRED]
- [[.test_plan_is_serialisable_for_the_unattended_audit_trail()]] - `calls` [INFERRED]
- [[.test_real_registry_plan_is_internally_consistent()]] - `calls` [INFERRED]
- [[.test_separates_advisories_already_fixed_at_the_current_pin()]] - `calls` [INFERRED]
- [[.test_unparseable_fixed_in_is_treated_as_not_remediable()]] - `calls` [INFERRED]
- [[Any_75]] - `references` [EXTRACTED]
- [[RemediationPlan]] - `references` [EXTRACTED]
- [[Work out the minimum version bump that remediates the most advisories.      Only]] - `rationale_for` [EXTRACTED]
- [[auto_remediate_cves.py]] - `contains` [EXTRACTED]
- [[main()_15]] - `calls` [EXTRACTED]
- [[parse_version()]] - `calls` [EXTRACTED]
- [[test_auto_remediate_cves.py (CVE remediation planner tests)]] - `calls` [EXTRACTED]
- [[test_real_registry_plan_is_internally_consistent]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PHASE_3A_3B_IMPLEMENTATIONmd