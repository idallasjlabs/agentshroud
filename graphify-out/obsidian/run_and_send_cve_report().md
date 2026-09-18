---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "test_daily_cve_report.py"
location: "L235"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# run_and_send_cve_report()

## Connections
- [[.test_failed_send_does_not_write_stamp_or_mark_sent_date()_1]] - `calls` [EXTRACTED]
- [[.test_returns_summary_without_token()_1]] - `calls` [EXTRACTED]
- [[.test_sends_telegram_on_success()_1]] - `calls` [EXTRACTED]
- [[.test_trivy_error_still_sends_error_report()_1]] - `calls` [EXTRACTED]
- [[Any_15]] - `references` [EXTRACTED]
- [[Run a Trivy scan, format the report, and send via Telegram.      Args         b]] - `rationale_for` [EXTRACTED]
- [[_build_image_targets()]] - `calls` [EXTRACTED]
- [[_send_telegram()]] - `calls` [EXTRACTED]
- [[cve_report_scheduler()]] - `calls` [EXTRACTED]
- [[daily_cve_report.py]] - `contains` [EXTRACTED]
- [[format_cve_report()]] - `calls` [EXTRACTED]
- [[generate_summary()_3]] - `calls` [EXTRACTED]
- [[run_trivy_scan()_1]] - `calls` [EXTRACTED]
- [[save_report()_1]] - `calls` [EXTRACTED]
- [[test_daily_cve_report.py_1]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_daily_cve_reportpy