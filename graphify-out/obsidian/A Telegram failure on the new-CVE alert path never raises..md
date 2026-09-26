---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "Mac App Discovery Skill"
location: "L748"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Mac_App_Discovery_Skill
---

# A Telegram failure on the new-CVE alert path never raises.

## Connections
- [[.test_alert_send_failure_is_swallowed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Mac_App_Discovery_Skill