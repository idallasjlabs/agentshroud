---
type: community
cohesion: 0.11
members: 32
---

# test_daily_cve_report.py

**Cohesion:** 0.11 - loosely connected
**Members:** 32 nodes

## Members
- [[dot-test_pin_revert_restores_the_exact_original_string()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_read_pin_missing_key_returns_none()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_read_pin_returns_the_pinned_value()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_write_pin_is_idempotent()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_write_pin_refuses_an_absent_key()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_write_pin_replaces_only_the_target_line()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-test_write_pin_round_trips_through_read_pin()]] - code - gateway/tests/test_auto_remediate_cves.py
- [[dot-to_dict()_6]] - code - scripts/auto_remediate_cves.py
- [[Any_37]] - code - scripts/auto_remediate_cves.py
- [[Bump the pin, run the gated upgrade, revert the pin if it does not hold.      Re]] - rationale - scripts/auto_remediate_cves.py
- [[Import the committed OpenClaw registry.]] - rationale - scripts/auto_remediate_cves.py
- [[Parse a dotted numeric version to a comparable tuple.      A trailing ``-N`` on]] - rationale - scripts/auto_remediate_cves.py
- [[Path_28]] - code - scripts/auto_remediate_cves.py
- [[Read one ``KEY=value`` pin from a versions.env-style file.]] - rationale - scripts/auto_remediate_cves.py
- [[Reading and rewriting dockerversions.env.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[RemediationPlan dataclass]] - code - scripts/auto_remediate_cves.py
- [[Rewrite one pin in place, preserving every other line byte for byte.      Raises]] - rationale - scripts/auto_remediate_cves.py
- [[Serialise for the unattended run's audit trail.]] - rationale - scripts/auto_remediate_cves.py
- [[Silently appending a new key could create a pin nothing consumes.]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[TestVersionPinIO]] - code - gateway/tests/test_auto_remediate_cves.py
- [[The rollback path a failed deploy must restore the pin verbatim,         downst]] - rationale - gateway/tests/test_auto_remediate_cves.py
- [[What a version bump would and would not remediate.      Every ``under_review`` a]] - rationale - scripts/auto_remediate_cves.py
- [[_print_plan()]] - code - scripts/auto_remediate_cves.py
- [[_run()_3]] - code - scripts/auto_remediate_cves.py
- [[apply_remediation()]] - code - scripts/auto_remediate_cves.py
- [[auto_remediate_cves.py]] - code - scripts/auto_remediate_cves.py
- [[load_registry()]] - code - scripts/auto_remediate_cves.py
- [[main()_12]] - code - scripts/auto_remediate_cves.py
- [[parse_version()_1]] - code - scripts/auto_remediate_cves.py
- [[read_pin()]] - code - scripts/auto_remediate_cves.py
- [[test_pin_revert_restores_the_exact_original_string]] - code - gateway/tests/test_auto_remediate_cves.py
- [[write_pin()]] - code - scripts/auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_daily_cve_reportpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_daily_cve_report.py (2)]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]
- 1 edge to [[_COMMUNITY_One Shroud Over Every Wire (founding mantra)]]
- 1 edge to [[_COMMUNITY__wrap_response() (2)]]
- 1 edge to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY_Sunday Upgrade prompt]]

## Top bridge nodes
- [[auto_remediate_cves.py]] - degree 15, connects to 6 communities
- [[apply_remediation()]] - degree 9, connects to 2 communities
- [[read_pin()]] - degree 11, connects to 1 community
- [[TestVersionPinIO]] - degree 10, connects to 1 community
- [[RemediationPlan dataclass]] - degree 9, connects to 1 community
