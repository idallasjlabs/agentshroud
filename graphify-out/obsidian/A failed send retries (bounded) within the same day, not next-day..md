---
source_file: "gateway/tests/test_daily_cve_report.py"
type: "rationale"
community: ".test_gives_up_and_marks_sent_after_max_retries()"
location: "L1767"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_gives_up_and_marks_sent_after_max_retries
---

# A failed send retries (bounded) within the same day, not next-day.

## Connections
- [[dot-test_retries_on_failed_send_before_giving_up()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_gives_up_and_marks_sent_after_max_retries
