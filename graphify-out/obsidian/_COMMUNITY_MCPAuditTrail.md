---
type: community
cohesion: 0.10
members: 35
---

# MCPAuditTrail

**Cohesion:** 0.10 - loosely connected
**Members:** 35 nodes

## Members
- [[._all_not_run_patches()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_all_domains_have_required_fields()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_compliance_new_keys_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_compute_weighted_subscore_full_score()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_compute_weighted_subscore_zero_for_empty_map()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_disa_stig_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_eu_ai_act_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_iso_42001_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_maturity_labels_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_network_segmentation_baseline_three()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_nist_csf_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_maturity_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_thirty_three_domains()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_scorecard_domain_ids_are_sequential()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_secrets_management_baseline_two()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_standard_basis_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_timestamp_present()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_totals_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_version_is_v090()]] - code - gateway/tests/test_scanner_integration.py
- [[Compute the 33-domain Security Scorecard.      Domains 1–21 Container infrastru]] - rationale - gateway/security/scanner_integration.py
- [[DISA STIG domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Determine composite compliance level using the weakest-link rule.      All 7 sub]] - rationale - gateway/security/scanner_integration.py
- [[Determine the highest achieved IEC 62443 Security Level.      SL 1 All IEC-mapp]] - rationale - gateway/security/scanner_integration.py
- [[EU AI Act domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[ISO 42001 domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[NIST CSF domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[New compliance sub-scores (EU AI Act, ISO 42001, NIST CSF, DISA STIG) appear in]] - rationale - gateway/tests/test_scanner_integration.py
- [[Return weighted sub-score as 0.0–100.0 percentage.]] - rationale - gateway/security/scanner_integration.py
- [[TestComputeScorecard]] - code - gateway/tests/test_scanner_integration.py
- [[_compute_weighted_subscore returns 0.0 for an empty domain map.]] - rationale - gateway/tests/test_scanner_integration.py
- [[_compute_weighted_subscore returns 100.0 when all domains score 5.]] - rationale - gateway/tests/test_scanner_integration.py
- [[_compute_weighted_subscore()]] - code - gateway/security/scanner_integration.py
- [[_determine_compliance_level()]] - code - gateway/security/scanner_integration.py
- [[_determine_iec_sl()]] - code - gateway/security/scanner_integration.py
- [[compute_scorecard()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPAuditTrail
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 16 edges to [[_COMMUNITY_A2AMethod]]
- 3 edges to [[_COMMUNITY_Canvas Skill]]
- 2 edges to [[_COMMUNITY_AgentShroud Dev Environment — Raspberry Pi 4 (8G]]
- 1 edge to [[_COMMUNITY_agentshroud-bot]]
- 1 edge to [[_COMMUNITY_Step-by-Step Installation]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_🟢 INFO (nice to have)]]
- 1 edge to [[_COMMUNITY_iCloud Data Manager (ICLOUD)]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]

## Top bridge nodes
- [[compute_scorecard()]] - degree 61, connects to 11 communities
- [[_compute_weighted_subscore()]] - degree 6, connects to 2 communities
- [[TestComputeScorecard]] - degree 21, connects to 1 community
- [[._all_not_run_patches()]] - degree 18, connects to 1 community
- [[_determine_compliance_level()]] - degree 3, connects to 1 community