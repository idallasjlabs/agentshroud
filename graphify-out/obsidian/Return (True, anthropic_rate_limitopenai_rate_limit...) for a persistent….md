---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "rationale"
community: "is_quota_exhausted"
location: "L215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/is_quota_exhausted
---

# Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a persistent…

## Connections
- [[is_rate_limited_post_retry()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/is_quota_exhausted
