---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: "test_telegram_executor.py"
location: "L1032"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_executorpy
---

# Regression guard (2026-08-30): the report scanned :latest tags         while dep

## Connections
- [[.test_prefers_running_image_over_configured_tag()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_executorpy