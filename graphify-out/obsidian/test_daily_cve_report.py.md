---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "asyncio"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/asyncio
---

# test_daily_cve_report.py

## Connections
- [[TestAlreadyCheckedUpstreamToday]] - `contains` [EXTRACTED]
- [[TestAlreadyIngestedGhsaToday]] - `contains` [EXTRACTED]
- [[TestAlreadySentToday]] - `contains` [EXTRACTED]
- [[TestBuildImageTargets]] - `contains` [EXTRACTED]
- [[TestCheckUpstreamCves]] - `contains` [EXTRACTED]
- [[TestCveReportSchedulerRetry]] - `contains` [EXTRACTED]
- [[TestFormatCveReport]] - `contains` [EXTRACTED]
- [[TestFormatUpstreamCveAlert]] - `contains` [EXTRACTED]
- [[TestGhsaIngestScheduler]] - `contains` [EXTRACTED]
- [[TestGhsaIngestSchedulerRetry]] - `contains` [EXTRACTED]
- [[TestPerAgentUpstreamChecks]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReport]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReportFailedDeliveryNotMarkedSent]] - `contains` [EXTRACTED]
- [[TestRunAndSendCveReportImageScans]] - `contains` [EXTRACTED]
- [[TestRunUpstreamCveCheck]] - `contains` [EXTRACTED]
- [[TestRunningImageResolution]] - `contains` [EXTRACTED]
- [[TestSendTelegramTruncation]] - `contains` [EXTRACTED]
- [[TestTrivySkipDirs]] - `contains` [EXTRACTED]
- [[TestUpstreamCveCheckSchedulerRetry]] - `contains` [EXTRACTED]
- [[Tests for gateway.security.daily_cve_report.]] - `rationale_for` [EXTRACTED]
- [[_already_sent_today]] - `imports` [EXTRACTED]
- [[_build_image_targets]] - `imports` [EXTRACTED]
- [[_make_error_report()]] - `contains` [EXTRACTED]
- [[_make_github_advisory()]] - `contains` [EXTRACTED]
- [[_make_report()]] - `contains` [EXTRACTED]
- [[check_upstream_cves]] - `imports` [EXTRACTED]
- [[datetime]] - `imports_from` [EXTRACTED]
- [[format_cve_report]] - `imports` [EXTRACTED]
- [[format_upstream_cve_alert]] - `imports` [EXTRACTED]
- [[gateway.security.agent_cve_registry]] - `imports_from` [EXTRACTED]
- [[gateway.security.daily_cve_report]] - `imports_from` [EXTRACTED]
- [[gateway.security.trivy_report]] - `imports_from` [EXTRACTED]
- [[list_cve_agents]] - `imports` [EXTRACTED]
- [[run_and_send_cve_report]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/asyncio