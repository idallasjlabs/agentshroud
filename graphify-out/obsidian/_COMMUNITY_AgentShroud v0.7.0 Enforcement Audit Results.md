---
type: community
cohesion: 0.10
members: 34
---

# AgentShroud v0.7.0 Enforcement Audit Results

**Cohesion:** 0.10 - loosely connected
**Members:** 34 nodes

## Members
- [[.test_pin_revert_restores_the_exact_original_string()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_missing_key_returns_none()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_returns_the_pinned_value()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_is_idempotent()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_refuses_an_absent_key()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_replaces_only_the_target_line()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_round_trips_through_read_pin()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.to_dict()_17]] - code - scripts/auto_remediate_cves.py
- [[Any_75]] - code - scripts/auto_remediate_cves.py
- [[Bump the pin, run the gated upgrade, revert the pin if it does not hold.      Re]] - rationale - scripts/auto_remediate_cves.py
- [[Import the committed OpenClaw registry.]] - rationale - scripts/auto_remediate_cves.py
- [[Origin-Aware Authorization (refuse owner elevation over unverified origin)]] - rationale - gateway/security/tool_acl.py
- [[Parse a dotted numeric version to a comparable tuple.      A trailing ``-N`` on]] - rationale - scripts/auto_remediate_cves.py
- [[Path_42]] - code - scripts/auto_remediate_cves.py
- [[Read one ``KEY=value`` pin from a versions.env-style file.]] - rationale - scripts/auto_remediate_cves.py
- [[Reading and rewriting dockerversions.env.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[RemediationPlan]] - code - scripts/auto_remediate_cves.py
- [[Rewrite one pin in place, preserving every other line byte for byte.      Raises]] - rationale - scripts/auto_remediate_cves.py
- [[Serialise for the unattended run's audit trail.]] - rationale - scripts/auto_remediate_cves.py
- [[Silently appending a new key could create a pin nothing consumes.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[TestVersionPinIO]] - code - gateway/tests/test_auto_remediate_cves.py
- [[The rollback path a failed deploy must restore the pin verbatim,         downst]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Two-Arm CVE Remediation (vendor fix + independent AgentShroud gateway control)]] - rationale - prompts/sunday-upgrade.md
- [[What a version bump would and would not remediate.      Every ``under_review`` a]] - rationale - scripts/auto_remediate_cves.py
- [[_print_plan()]] - code - scripts/auto_remediate_cves.py
- [[_run()_1]] - code - scripts/auto_remediate_cves.py
- [[apply_remediation()]] - code - scripts/auto_remediate_cves.py
- [[auto_remediate_cves.py]] - code - scripts/auto_remediate_cves.py
- [[load_registry()]] - code - scripts/auto_remediate_cves.py
- [[main()_15]] - code - scripts/auto_remediate_cves.py
- [[parse_version()]] - code - scripts/auto_remediate_cves.py
- [[read_pin()]] - code - scripts/auto_remediate_cves.py
- [[test_pin_revert_restores_the_exact_original_string]] - code - gateway/tests/test_auto_remediate_cves.py
- [[write_pin()]] - code - scripts/auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v070_Enforcement_Audit_Results
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]
- 4 edges to [[_COMMUNITY_OutputSchemaEnforcer]]
- 2 edges to [[_COMMUNITY_DraftEntry]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_CICD Pipeline Advisor (README)]]
- 1 edge to [[_COMMUNITY__seed_cron]]

## Top bridge nodes
- [[auto_remediate_cves.py]] - degree 18, connects to 5 communities
- [[apply_remediation()]] - degree 9, connects to 2 communities
- [[read_pin()]] - degree 11, connects to 1 community
- [[TestVersionPinIO]] - degree 10, connects to 1 community
- [[RemediationPlan]] - degree 9, connects to 1 community