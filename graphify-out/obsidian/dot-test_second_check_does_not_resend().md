---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "code"
community: "OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)"
location: "L565"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
---

# .test_second_check_does_not_resend()

## Connections
- [[TestUpstreamAlertDedup]] - `method` [EXTRACTED]
- [[_fake_send()_21]] - `contains` [EXTRACTED]
- [[_fake_send()]] - `indirect_call` [INFERRED]
- [[asyncio_3]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/OpenClaw_and_Hermes_are_processed_on_fully_separate_paths_one_failing_never_2
