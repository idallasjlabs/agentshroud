---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "rationale"
community: "Rate Limit Failover"
location: "L215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Rate_Limit_Failover
---

# Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a     persiste

## Connections
- [[is_rate_limited_post_retry()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Rate_Limit_Failover