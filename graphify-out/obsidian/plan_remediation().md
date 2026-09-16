---
source_file: "scripts/auto_remediate_cves.py"
type: "code"
community: "Community 274"
location: "L169"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_274
---

# plan_remediation()

## Connections
- [[dot-test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - `calls` [INFERRED]
- [[dot-test_downstream_build_suffix_on_the_pin_is_ignored()]] - `calls` [INFERRED]
- [[dot-test_empty_registry_is_a_no_op_plan()]] - `calls` [INFERRED]
- [[dot-test_max_target_caps_the_bump()]] - `calls` [INFERRED]
- [[dot-test_no_upgrade_needed_yields_no_target()]] - `calls` [INFERRED]
- [[dot-test_only_under_review_entries_are_considered()]] - `calls` [INFERRED]
- [[dot-test_picks_minimum_version_clearing_every_remediable_advisory()]] - `calls` [INFERRED]
- [[dot-test_plan_is_serialisable_for_the_unattended_audit_trail()]] - `calls` [INFERRED]
- [[dot-test_real_registry_plan_is_internally_consistent()]] - `calls` [INFERRED]
- [[dot-test_separates_advisories_already_fixed_at_the_current_pin()]] - `calls` [INFERRED]
- [[dot-test_unparseable_fixed_in_is_treated_as_not_remediable()]] - `calls` [INFERRED]
- [[Any_31]] - `references` [EXTRACTED]
- [[RemediationPlan]] - `calls` [EXTRACTED]
- [[Work out the minimum version bump that remediates the most advisories. Only…]] - `rationale_for` [EXTRACTED]
- [[auto_remediate_cves.py]] - `contains` [EXTRACTED]
- [[main()_3]] - `calls` [EXTRACTED]
- [[parse_version()_1]] - `calls` [EXTRACTED]
- [[test_auto_remediate_cves.py (CVE remediation planner tests)]] - `calls` [EXTRACTED]
- [[test_real_registry_plan_is_internally_consistent]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_274