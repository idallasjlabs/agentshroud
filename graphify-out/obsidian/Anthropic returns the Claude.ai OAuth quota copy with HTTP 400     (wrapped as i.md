---
source_file: "gateway/tests/test_llm_quota_detector.py"
type: "rationale"
community: "is_quota_exhausted()"
location: "L50"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/is_quota_exhausted
---

# Anthropic returns the Claude.ai OAuth quota copy with HTTP 400     (wrapped as i

## Connections
- [[test_detect_anthropic_400_oauth_extra_usage()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/is_quota_exhausted