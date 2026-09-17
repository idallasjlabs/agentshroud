---
type: community
cohesion: 0.08
members: 51
---

# plan_remediation()

**Cohesion:** 0.08 - loosely connected
**Members:** 51 nodes

## Members
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_advisory_without_a_fixed_in_is_not_claimed_remediable()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_downstream_build_suffix_on_the_pin_is_ignored()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_downstream_build_suffix_on_the_pin_is_ignored()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_empty_registry_is_a_no_op_plan()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_empty_registry_is_a_no_op_plan()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_max_target_caps_the_bump()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_max_target_caps_the_bump()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_no_upgrade_needed_yields_no_target()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_no_upgrade_needed_yields_no_target()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_only_under_review_entries_are_considered()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_only_under_review_entries_are_considered()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_picks_minimum_version_clearing_every_remediable_advisory()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_picks_minimum_version_clearing_every_remediable_advisory()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_plan_is_serialisable_for_the_unattended_audit_trail()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_plan_is_serialisable_for_the_unattended_audit_trail()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_real_registry_plan_is_internally_consistent()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_real_registry_plan_is_internally_consistent()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_separates_advisories_already_fixed_at_the_current_pin()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_separates_advisories_already_fixed_at_the_current_pin()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_unparseable_fixed_in_is_treated_as_not_remediable()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_unparseable_fixed_in_is_treated_as_not_remediable()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[2026.7.1-2' is AgentShroud's own rebuild counter, not upstream semver.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[2026.7.1-2' is AgentShroud's own rebuild counter, not upstream semver. An…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Already-triaged entries are somebody's assessed verdict — a version         bump]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[An operator may cap how far forward an unattended job may jump.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Minimal registry entry shaped like agent_cve_registry.py's dicts.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[No upstream fix means no version bump can honestly clear it.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[RemediationPlan]] - code - scripts/auto_remediate_cves.py
- [[Sanity-check the planner against the real committed registry.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanAgainstRealRegistry]] - code - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanAgainstRealRegistry_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanRemediation]] - code - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanRemediation_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[Tests for scriptsauto_remediate_cves.py — automated CVE remediation planning.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[The planner decides WHAT bump remediates WHICH advisories.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[What a version bump would and would not remediate. Every ``under_review``…]] - rationale - scripts/auto_remediate_cves.py
- [[Work out the minimum version bump that remediates the most advisories. Only…]] - rationale - scripts/auto_remediate_cves.py
- [[_OPENCLAW_CVE_REGISTRY]] - code - gateway/security/agent_cve_registry.py
- [[_entry()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[_entry()_2]] - code - gateway/tests/test_auto_remediate_cves.py
- [[fixed_in = pin means the vulnerable code is not present at all.          These]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[fixed_in = pin means the vulnerable code is not present at all. These are mis-…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[plan_remediation()]] - code - scripts/auto_remediate_cves.py
- [[read_pin]] - code - scripts/auto_remediate_cves.py
- [[test_auto_remediate_cves.py]] - code - gateway/tests/test_auto_remediate_cves.py
- [[test_auto_remediate_cves.py_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[test_auto_remediate_cves.py (CVE remediation planner tests)]] - code - gateway/tests/test_auto_remediate_cves.py
- [[test_no_entry_id_looks_like_a_cve]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_real_registry_plan_is_internally_consistent]] - code - gateway/tests/test_auto_remediate_cves.py
- [[write_pin]] - code - scripts/auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/plan_remediation
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_auto_remediate_cves.py]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_check_upstream_cves()]]
- 1 edge to [[_COMMUNITY_sunday-upgrade]]

## Top bridge nodes
- [[test_auto_remediate_cves.py_1]] - degree 9, connects to 2 communities
- [[_OPENCLAW_CVE_REGISTRY]] - degree 5, connects to 2 communities
- [[plan_remediation()]] - degree 30, connects to 1 community
- [[RemediationPlan]] - degree 9, connects to 1 community
- [[test_auto_remediate_cves.py]] - degree 6, connects to 1 community