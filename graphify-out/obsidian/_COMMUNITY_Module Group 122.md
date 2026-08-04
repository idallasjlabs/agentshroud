---
type: community
cohesion: 0.09
members: 38
---

# Module Group 122

**Cohesion:** 0.09 - loosely connected
**Members:** 38 nodes

## Members
- [[.test_initial_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_infected()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_not_run()_2]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_managed_when_no_criticals_but_high()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_measured_or_higher_when_fully_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_measured_when_clean_not_fresh()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_optimizing_when_installed_clean_no_timestamp()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_optimizing_when_installed_clean_no_timestamp()]] - code - gateway/tests/test_scanner_integration.py
- [[A report that is 48h old must not score above 1.]] - rationale - gateway/tests/test_scorecard_integrity.py
- [[Fresh clean report with zero CVEs should score 5.]] - rationale - gateway/tests/test_scorecard_integrity.py
- [[Score domain 2 Vulnerability Management (0-5).      1=module installed but no r]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 6 Malware Defense (0-5).      1=module installed or not_run, 3=cla]] - rationale - gateway/security/scanner_integration.py
- [[Stale ClamAV report (48h) must not score above 1.]] - rationale - gateway/tests/test_scorecard_integrity.py
- [[TestScoreMalwareDefense]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreVulnerabilityManagement]] - code - gateway/tests/test_scanner_integration.py
- [[_clean_clamav()]] - code - gateway/tests/test_scorecard_integrity.py
- [[_clean_trivy()]] - code - gateway/tests/test_scorecard_integrity.py
- [[_not_run_clamav()]] - code - gateway/tests/test_scorecard_integrity.py
- [[_not_run_trivy()]] - code - gateway/tests/test_scorecard_integrity.py
- [[_score_malware_defense()]] - code - gateway/security/scanner_integration.py
- [[_score_vulnerability_management()]] - code - gateway/security/scanner_integration.py
- [[test_empty_collaborator_activity_no_score()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_empty_key_rotation_log_no_score()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_host_hardening_empty_audit_log_no_bonus()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_host_hardening_nonempty_audit_log_adds_score()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_malware_fresh_clean_scores_5()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_malware_not_run_scores_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_malware_stale_report_scores_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_no_scan_reports_malware_defense_le_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_no_scan_reports_vuln_management_le_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_nonempty_collaborator_activity_adds_score()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_nonempty_key_rotation_log_adds_score()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_scorecard_integrity.py]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_vuln_fresh_clean_report_scores_5()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_vuln_no_report_dir_scores_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_vuln_not_run_scores_1()]] - code - gateway/tests/test_scorecard_integrity.py
- [[test_vuln_stale_report_scores_1()]] - code - gateway/tests/test_scorecard_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_122
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 5 edges to [[_COMMUNITY_Security Scanner Integration]]
- 2 edges to [[_COMMUNITY_Module Group 381]]
- 2 edges to [[_COMMUNITY_Module Group 228]]
- 2 edges to [[_COMMUNITY_Module Group 134]]

## Top bridge nodes
- [[_score_vulnerability_management()]] - degree 17, connects to 5 communities
- [[_score_malware_defense()]] - degree 15, connects to 5 communities
- [[test_scorecard_integrity.py]] - degree 24, connects to 1 community
- [[TestScoreVulnerabilityManagement]] - degree 6, connects to 1 community
- [[TestScoreMalwareDefense]] - degree 5, connects to 1 community
