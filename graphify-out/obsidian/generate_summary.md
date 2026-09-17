---
source_file: "gateway/security/trivy_report.py"
type: "code"
community: "test_security_toolchain.py"
location: "188"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_security_toolchainpy
---

# generate_summary

## Connections
- [[.test_run_empty_stdout_is_error_not_clean()]] - `calls` [EXTRACTED]
- [[.test_run_nonzero_exit_code_is_error()]] - `calls` [EXTRACTED]
- [[.test_summary_clean()]] - `calls` [EXTRACTED]
- [[.test_summary_critical()]] - `calls` [EXTRACTED]
- [[.test_summary_error()]] - `calls` [EXTRACTED]
- [[.test_summary_top_cves_ids()]] - `calls` [EXTRACTED]
- [[.test_summary_warning_high_only()]] - `calls` [EXTRACTED]
- [[Any_36]] - `references` [EXTRACTED]
- [[Generate a summary dict suitable for the health report.      Args         alert]] - `rationale_for` [EXTRACTED]
- [[format_cve_report]] - `calls` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `imports` [EXTRACTED]
- [[gateway.security.trivy_report]] - `contains` [EXTRACTED]
- [[health_report.py]] - `shares_data_with` [EXTRACTED]
- [[run_and_send_cve_report]] - `calls` [EXTRACTED]
- [[scanner_integration.py]] - `imports` [EXTRACTED]
- [[test_security_toolchain.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_security_toolchainpy