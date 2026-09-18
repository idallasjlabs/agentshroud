---
type: community
cohesion: 0.08
members: 43
---

# auto_remediate_cves.py

**Cohesion:** 0.08 - loosely connected
**Members:** 43 nodes

## Members
- [[.test_pin_revert_restores_the_exact_original_string()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_pin_revert_restores_the_exact_original_string()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_missing_key_returns_none()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_missing_key_returns_none()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_returns_the_pinned_value()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_read_pin_returns_the_pinned_value()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_is_idempotent()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_is_idempotent()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_refuses_an_absent_key()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_refuses_an_absent_key()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_replaces_only_the_target_line()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_replaces_only_the_target_line()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_round_trips_through_read_pin()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.test_write_pin_round_trips_through_read_pin()_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[.to_dict()]] - code - scripts/auto_remediate_cves.py
- [[Any_30]] - code
- [[Automated CVE remediation — actually patch the advisories, don't just file…]] - rationale - scripts/auto_remediate_cves.py
- [[Bump the pin, run the gated upgrade, revert the pin if it does not hold.…]] - rationale - scripts/auto_remediate_cves.py
- [[Import the committed OpenClaw registry.]] - rationale - scripts/auto_remediate_cves.py
- [[Parse a dotted numeric version to a comparable tuple. A trailing ``-N`` on any…]] - rationale - scripts/auto_remediate_cves.py
- [[Path_12]] - code
- [[Phantom Tag Bug Class (scanningbuilding a version tag that is not the one actually running)]] - rationale - prompts/sunday-upgrade.md
- [[Read one ``KEY=value`` pin from a versions.env-style file.]] - rationale - scripts/auto_remediate_cves.py
- [[Reading and rewriting dockerversions.env.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Rewrite one pin in place, preserving every other line byte for byte. Raises…]] - rationale - scripts/auto_remediate_cves.py
- [[Serialise for the unattended run's audit trail.]] - rationale - scripts/auto_remediate_cves.py
- [[Silently appending a new key could create a pin nothing consumes.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[TestVersionPinIO]] - code - gateway/tests/test_auto_remediate_cves.py
- [[TestVersionPinIO_1]] - code - gateway/tests/test_auto_remediate_cves.py
- [[The rollback path a failed deploy must restore the pin verbatim,         downst]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[The rollback path a failed deploy must restore the pin verbatim, downstream…]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[Two-Arm CVE Remediation (vendor fix + independent AgentShroud gateway control)]] - rationale - prompts/sunday-upgrade.md
- [[_print_plan()]] - code - scripts/auto_remediate_cves.py
- [[_run()]] - code - scripts/auto_remediate_cves.py
- [[apply_remediation()]] - code - scripts/auto_remediate_cves.py
- [[auto_remediate_cves.py]] - code - scripts/auto_remediate_cves.py
- [[load_registry()]] - code - scripts/auto_remediate_cves.py
- [[main()_3]] - code - scripts/auto_remediate_cves.py
- [[parse_version()_1]] - code - scripts/auto_remediate_cves.py
- [[read_pin()]] - code - scripts/auto_remediate_cves.py
- [[test_pin_revert_restores_the_exact_original_string]] - code - gateway/tests/test_auto_remediate_cves.py
- [[versions.env]] - document - docker/versions.env
- [[write_pin()]] - code - scripts/auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/auto_remediate_cvespy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_plan_remediation()]]
- 3 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 2 edges to [[_COMMUNITY_triage-cve-mitigations.py]]
- 2 edges to [[_COMMUNITY_sunday-upgrade]]
- 2 edges to [[_COMMUNITY_check-vendor-compat.sh]]
- 1 edge to [[_COMMUNITY_gateway.security.agent_cve_registry]]
- 1 edge to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 1 edge to [[_COMMUNITY__t()]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_asb]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[auto_remediate_cves.py]] - degree 20, connects to 5 communities
- [[apply_remediation()]] - degree 9, connects to 3 communities
- [[versions.env]] - degree 4, connects to 3 communities
- [[Phantom Tag Bug Class (scanningbuilding a version tag that is not the one actually running)]] - degree 3, connects to 2 communities
- [[Two-Arm CVE Remediation (vendor fix + independent AgentShroud gateway control)]] - degree 3, connects to 2 communities