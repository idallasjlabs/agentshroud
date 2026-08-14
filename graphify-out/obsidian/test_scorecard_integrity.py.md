---
source_file: "gateway/tests/test_scorecard_integrity.py"
type: "code"
community: "docs/vault"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/docs/vault
---

# test_scorecard_integrity.py

## Connections
- [[_clean_clamav()]] - `contains` [EXTRACTED]
- [[_clean_trivy()]] - `contains` [EXTRACTED]
- [[_not_run_clamav()]] - `contains` [EXTRACTED]
- [[_not_run_trivy()]] - `contains` [EXTRACTED]
- [[_score_access_control_authorization()]] - `imports` [EXTRACTED]
- [[_score_data_confidentiality_encryption()]] - `imports` [EXTRACTED]
- [[_score_host_os_hardening()]] - `imports` [EXTRACTED]
- [[_score_malware_defense()]] - `imports` [EXTRACTED]
- [[_score_vulnerability_management()]] - `imports` [EXTRACTED]
- [[test_empty_collaborator_activity_no_score()]] - `contains` [EXTRACTED]
- [[test_empty_key_rotation_log_no_score()]] - `contains` [EXTRACTED]
- [[test_host_hardening_empty_audit_log_no_bonus()]] - `contains` [EXTRACTED]
- [[test_host_hardening_nonempty_audit_log_adds_score()]] - `contains` [EXTRACTED]
- [[test_malware_fresh_clean_scores_5()]] - `contains` [EXTRACTED]
- [[test_malware_not_run_scores_1()]] - `contains` [EXTRACTED]
- [[test_malware_stale_report_scores_1()]] - `contains` [EXTRACTED]
- [[test_no_scan_reports_malware_defense_le_1()]] - `contains` [EXTRACTED]
- [[test_no_scan_reports_vuln_management_le_1()]] - `contains` [EXTRACTED]
- [[test_nonempty_collaborator_activity_adds_score()]] - `contains` [EXTRACTED]
- [[test_nonempty_key_rotation_log_adds_score()]] - `contains` [EXTRACTED]
- [[test_vuln_fresh_clean_report_scores_5()]] - `contains` [EXTRACTED]
- [[test_vuln_no_report_dir_scores_1()]] - `contains` [EXTRACTED]
- [[test_vuln_not_run_scores_1()]] - `contains` [EXTRACTED]
- [[test_vuln_stale_report_scores_1()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/docs/vault