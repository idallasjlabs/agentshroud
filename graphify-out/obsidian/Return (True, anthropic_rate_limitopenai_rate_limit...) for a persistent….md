---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "rationale"
community: "test_anthropic_openai_translator.py"
location: "L215"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_anthropic_openai_translatorpy
---

# Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a persistent…

## Connections
- [[is_rate_limited_post_retry()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_anthropic_openai_translatorpy
