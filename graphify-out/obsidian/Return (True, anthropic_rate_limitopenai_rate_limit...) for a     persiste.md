---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a     persiste

## Connections
- [[is_rate_limited_post_retry()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite