---
type: community
cohesion: 0.08
members: 53
---

# _t()

**Cohesion:** 0.08 - loosely connected
**Members:** 53 nodes

## Members
- [[._results()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_all_mapped_layers_exist_in_registry()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_apply_writes_registry_and_gap()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_classification_is_deterministic()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_confidence_is_bounded()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_dry_run_writes_nothing()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_gap_report_renders_and_lists_gaps()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_gaps_are_honest_not_mitigated_or_under_review()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_low_confidence_partial_stays_under_review()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_mitigation_narrative_nonempty_when_applied()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_multiline_parenthesised_value_consumed()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_not_source_fixed_full_class_is_fully_mitigated_without_source_fix()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_not_source_fixed_newer()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_not_source_fixed_partial_class_is_partially_mitigated()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_parse_non_numeric()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_parse_none_and_empty()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_parse_numeric()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_priority_rce_before_generic_injection()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_representative_titles()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_rewrite_is_idempotent()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_rewrite_never_touches_hermes()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_rewrite_sets_status_and_layers()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_rewrite_untargeted_id_unchanged()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_running_version_matches_pinned_openclaw_version()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_source_fixed_equal()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_source_fixed_full_class_is_fully_mitigated()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_source_fixed_older()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_source_fixed_partial_class_upgrades_to_fully()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_summary_counts_sum_to_total()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_triage_agent_does_not_read_hermes()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_triage_agent_openclaw_all_under_review_processed()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_uncovered_class_not_source_fixed_is_gap()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_uncovered_class_source_fixed_uses_source_fix()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_unknown_agent_errors()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_unknown_class_not_source_fixed_stays_under_review()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_unmatched_is_unknown()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_unparseable_is_not_source_fixed()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[.test_unterminated_field_returns_end()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[Every layer the engine can emit must already be used by a mitigated entry in…]] - rationale - gateway/tests/test_triage_cve_mitigations.py
- [[Regression guard for the 2026-07-29 staleness incident. RUNNING_VERSION was…]] - rationale - gateway/tests/test_triage_cve_mitigations.py
- [[TestClassify]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestConsumeFieldEdge]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestDefenseLayerVocabulary]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestDriverIsolation]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestMain]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestRewrite]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestTriageEntry]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestVersion]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[Tests for scriptstriage-cve-mitigations.py — Phase 2 mitigation-triage engine.…]] - rationale - gateway/tests/test_triage_cve_mitigations.py
- [[_entry()_1]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[_t()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[parametrize_3]] - code
- [[test_triage_cve_mitigations.py]] - code - gateway/tests/test_triage_cve_mitigations.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_t
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_gateway.security.agent_cve_registry]]
- 1 edge to [[_COMMUNITY_auto_remediate_cves.py]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]

## Top bridge nodes
- [[test_triage_cve_mitigations.py]] - degree 14, connects to 3 communities
- [[_t()]] - degree 40, connects to 1 community