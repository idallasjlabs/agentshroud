---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)"
location: "L896"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
---

# .test_alert_send_failure_is_swallowed()

## Connections
- [[A Telegram failure on the new-CVE alert path never raises.]] - `rationale_for` [EXTRACTED]
- [[TestPerAgentUpstreamChecks]] - `method` [EXTRACTED]
- [[_boom_send()]] - `contains` [EXTRACTED]
- [[_boom_send()_1]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
