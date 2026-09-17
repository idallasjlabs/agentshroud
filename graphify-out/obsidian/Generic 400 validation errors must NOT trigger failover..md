---
source_file: "gateway/tests/test_llm_quota_detector.py"
type: "rationale"
community: "is_quota_exhausted()"
location: "L68"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/is_quota_exhausted
---

# Generic 400 validation errors must NOT trigger failover.

## Connections
- [[test_400_without_quota_substring_not_flagged()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/is_quota_exhausted