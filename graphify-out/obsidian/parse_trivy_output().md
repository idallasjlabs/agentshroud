---
source_file: "gateway/security/trivy_report.py"
type: "code"
community: "Security Toolchain"
location: "L88"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Toolchain
---

# parse_trivy_output()

## Connections
- [[.test_custom_prefix()]] - `calls` [EXTRACTED]
- [[.test_default_prefix()]] - `calls` [EXTRACTED]
- [[.test_log_dir_created_if_missing()]] - `calls` [EXTRACTED]
- [[.test_parse_affected_packages()]] - `calls` [EXTRACTED]
- [[.test_parse_counts_by_severity()]] - `calls` [EXTRACTED]
- [[.test_parse_empty_output()]] - `calls` [EXTRACTED]
- [[.test_parse_has_timestamp()]] - `calls` [EXTRACTED]
- [[.test_parse_no_results_key()]] - `calls` [EXTRACTED]
- [[.test_parse_scanner_name()]] - `calls` [EXTRACTED]
- [[.test_parse_top_cves_limited()]] - `calls` [EXTRACTED]
- [[.test_parse_top_cves_ordered_by_severity()]] - `calls` [EXTRACTED]
- [[.test_parse_total_vulnerabilities()]] - `calls` [EXTRACTED]
- [[.test_parse_unknown_severity()]] - `calls` [EXTRACTED]
- [[.test_report_content_persisted()]] - `calls` [EXTRACTED]
- [[.test_summary_clean()]] - `calls` [EXTRACTED]
- [[.test_summary_critical()]] - `calls` [EXTRACTED]
- [[.test_summary_top_cves_ids()]] - `calls` [EXTRACTED]
- [[.test_summary_warning_high_only()]] - `calls` [EXTRACTED]
- [[Any_64]] - `references` [EXTRACTED]
- [[Parse raw Trivy JSON output into a structured summary.      Args         raw R]] - `rationale_for` [EXTRACTED]
- [[run_trivy_scan()_1]] - `calls` [EXTRACTED]
- [[test_security_toolchain.py]] - `imports` [EXTRACTED]
- [[trivy_report.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Toolchain