---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "asyncio"
location: "L21"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# _make_report()

## Connections
- [[.test_affected_packages_count_shown()]] - `calls` [EXTRACTED]
- [[.test_contains_cve_ids()]] - `calls` [EXTRACTED]
- [[.test_contains_header()]] - `calls` [EXTRACTED]
- [[.test_contains_package_names()]] - `calls` [EXTRACTED]
- [[.test_contains_severity_counts()]] - `calls` [EXTRACTED]
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - `calls` [EXTRACTED]
- [[.test_fixed_version_shown()]] - `calls` [EXTRACTED]
- [[.test_returns_summary_without_token()]] - `calls` [EXTRACTED]
- [[.test_sends_telegram_on_success()]] - `calls` [EXTRACTED]
- [[.test_status_clean_when_no_critical_high()]] - `calls` [EXTRACTED]
- [[.test_status_critical_when_critical_present()]] - `calls` [EXTRACTED]
- [[.test_total_vulnerability_count_shown()]] - `calls` [EXTRACTED]
- [[.test_zero_count_severity_omitted()]] - `calls` [EXTRACTED]
- [[Build a minimal parsed Trivy report.]] - `rationale_for` [EXTRACTED]
- [[_fake_trivy_scan()]] - `calls` [EXTRACTED]
- [[_fake_trivy_scan()_1]] - `calls` [EXTRACTED]
- [[_fake_trivy_scan()_2]] - `calls` [EXTRACTED]
- [[_fake_trivy_scan()_3]] - `calls` [EXTRACTED]
- [[_fake_trivy_scan()_4]] - `calls` [EXTRACTED]
- [[_fake_trivy_scan()_5]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio