---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "test_daily_cve_report.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_daily_cve_reportpy
---

# test_daily_cve_report.py

## Connections
- [[TestAlreadyCheckedUpstreamToday_1]] - `contains` [EXTRACTED]
- [[TestAlreadyIngestedGhsaToday_1]] - `contains` [EXTRACTED]
- [[TestAlreadySentToday_1]] - `contains` [EXTRACTED]
- [[TestBuildImageTargets_1]] - `contains` [EXTRACTED]
- [[TestCheckUpstreamCves_1]] - `contains` [EXTRACTED]
- [[TestCveReportSchedulerRetry_1]] - `contains` [EXTRACTED]
- [[TestFormatCveReport_1]] - `contains` [EXTRACTED]
- [[TestFormatUpstreamCveAlert_1]] - `contains` [EXTRACTED]
- [[TestGhsaIngestScheduler_1]] - `contains` [EXTRACTED]
- [[TestGhsaIngestSchedulerRetry_1]] - `contains` [EXTRACTED]
- [[TestPerAgentUpstreamChecks_1]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReport_1]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent_1]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans_1]] - `contains` [EXTRACTED]
- [[TestRunUpstreamCveCheck_1]] - `contains` [EXTRACTED]
- [[TestRunningImageResolution_1]] - `contains` [EXTRACTED]
- [[TestSendTelegramTruncation_1]] - `contains` [EXTRACTED]
- [[TestTrivySkipDirs_1]] - `contains` [EXTRACTED]
- [[TestUpstreamCveCheckSchedulerRetry_1]] - `contains` [EXTRACTED]
- [[_already_sent_today()]] - `imports` [EXTRACTED]
- [[_build_image_targets()]] - `references` [EXTRACTED]
- [[_make_error_report()_1]] - `contains` [EXTRACTED]
- [[_make_github_advisory()_1]] - `contains` [EXTRACTED]
- [[_make_report()_1]] - `contains` [EXTRACTED]
- [[_running_image()]] - `references` [EXTRACTED]
- [[agent_cve_registry.py]] - `imports_from` [EXTRACTED]
- [[check_upstream_cves()]] - `references` [EXTRACTED]
- [[daily_cve_report.py]] - `imports_from` [EXTRACTED]
- [[datetime]] - `imports_from` [EXTRACTED]
- [[format_cve_report()]] - `references` [EXTRACTED]
- [[format_upstream_cve_alert()]] - `references` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `imports_from` [EXTRACTED]
- [[list_cve_agents()]] - `imports` [EXTRACTED]
- [[run_and_send_cve_report()]] - `references` [EXTRACTED]
- [[run_trivy_scan()_1]] - `references` [EXTRACTED]
- [[run_upstream_cve_check()]] - `references` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `references` [EXTRACTED]
- [[trivy_report.py_2]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_daily_cve_reportpy