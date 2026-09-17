---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "Community 82"
location: "235"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_82
---

# run_and_send_cve_report

## Connections
- [[dot-test_failed_send_does_not_write_stamp_or_mark_sent_date()]] - `calls` [EXTRACTED]
- [[dot-test_returns_summary_without_token()]] - `calls` [EXTRACTED]
- [[dot-test_sends_telegram_on_success()]] - `calls` [EXTRACTED]
- [[dot-test_trivy_error_still_sends_error_report()]] - `calls` [EXTRACTED]
- [[Any_16]] - `references` [EXTRACTED]
- [[Run a Trivy scan, format the report, and send via Telegram. Args bot_token…]] - `rationale_for` [EXTRACTED]
- [[_build_image_targets]] - `calls` [EXTRACTED]
- [[_send_telegram]] - `calls` [EXTRACTED]
- [[_t()]] - `indirect_call` [INFERRED]
- [[cve_report_scheduler]] - `calls` [EXTRACTED]
- [[format_cve_report]] - `calls` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `contains` [EXTRACTED]
- [[generate_summary]] - `calls` [EXTRACTED]
- [[run_trivy_scan]] - `calls` [EXTRACTED]
- [[save_report]] - `calls` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_82