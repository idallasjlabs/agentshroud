---
type: community
cohesion: 0.11
members: 30
---

# Community 274

**Cohesion:** 0.11 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-test_advisory_without_a_fixed_in_is_not_claimed_remediable()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_downstream_build_suffix_on_the_pin_is_ignored()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_empty_registry_is_a_no_op_plan()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_max_target_caps_the_bump()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_no_upgrade_needed_yields_no_target()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_only_under_review_entries_are_considered()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_picks_minimum_version_clearing_every_remediable_advisory()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_plan_is_serialisable_for_the_unattended_audit_trail()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_real_registry_plan_is_internally_consistent()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_separates_advisories_already_fixed_at_the_current_pin()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_unparseable_fixed_in_is_treated_as_not_remediable()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[2026.7.1-2' is AgentShroud's own rebuild counter, not upstream semver. An…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Already-triaged entries are somebody's assessed verdict — a version bump…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[An operator may cap how far forward an unattended job may jump.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Minimal registry entry shaped like agent_cve_registry.py's dicts.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[No upstream fix means no version bump can honestly clear it.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Sanity-check the planner against the real committed registry.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanAgainstRealRegistry]] - code - gateway/tests/test_auto_remediate_cves.py
- [[TestPlanRemediation]] - code - gateway/tests/test_auto_remediate_cves.py
- [[Tests for scriptsauto_remediate_cves.py — automated CVE remediation planning.…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[The planner decides WHAT bump remediates WHICH advisories.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Work out the minimum version bump that remediates the most advisories. Only…]] - rationale - scripts/auto_remediate_cves.py
- [[_OPENCLAW_CVE_REGISTRY]] - code - gateway/security/agent_cve_registry.py
- [[_entry()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[fixed_in = pin means the vulnerable code is not present at all. These are mis-…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[plan_remediation()]] - code - scripts/auto_remediate_cves.py
- [[test_auto_remediate_cves.py]] - code - gateway/tests/test_auto_remediate_cves.py
- [[test_auto_remediate_cves.py (CVE remediation planner tests)]] - code - gateway/tests/test_auto_remediate_cves.py
- [[test_no_entry_id_looks_like_a_cve]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_real_registry_plan_is_internally_consistent]] - code - gateway/tests/test_auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_274
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 195]]
- 1 edge to [[_COMMUNITY_Community 59]]

## Top bridge nodes
- [[plan_remediation()]] - degree 19, connects to 1 community
- [[test_auto_remediate_cves.py]] - degree 6, connects to 1 community
- [[_OPENCLAW_CVE_REGISTRY]] - degree 3, connects to 1 community
- [[dot-test_real_registry_plan_is_internally_consistent()]] - degree 3, connects to 1 community