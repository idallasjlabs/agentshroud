---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "format_cve_report()"
location: "L21"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/format_cve_report
---

# _make_report()

## Connections
- [[.test_affected_packages_count_shown()_1]] - `calls` [EXTRACTED]
- [[.test_contains_cve_ids()_1]] - `calls` [EXTRACTED]
- [[.test_contains_header()_1]] - `calls` [EXTRACTED]
- [[.test_contains_package_names()_1]] - `calls` [EXTRACTED]
- [[.test_contains_severity_counts()_1]] - `calls` [EXTRACTED]
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()_1]] - `calls` [EXTRACTED]
- [[.test_fixed_version_shown()_1]] - `calls` [EXTRACTED]
- [[.test_returns_summary_without_token()_1]] - `calls` [EXTRACTED]
- [[.test_sends_telegram_on_success()_1]] - `calls` [EXTRACTED]
- [[.test_status_clean_when_no_critical_high()_1]] - `calls` [EXTRACTED]
- [[.test_status_critical_when_critical_present()_1]] - `calls` [EXTRACTED]
- [[.test_total_vulnerability_count_shown()_1]] - `calls` [EXTRACTED]
- [[.test_zero_count_severity_omitted()_1]] - `calls` [EXTRACTED]
- [[Build a minimal parsed Trivy report.]] - `rationale_for` [EXTRACTED]
- [[test_daily_cve_report.py_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/format_cve_report