---
source_file: "gateway/tests/test_rate_limit_failover.py"
type: "code"
community: "test_anthropic_openai_translator.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_anthropic_openai_translatorpy
---

# test_rate_limit_failover.py

## Connections
- [[LLMProxy]] - `imports` [EXTRACTED]
- [[Post-retry rate-limit failover. Observed 2026-06-131415 Anthropic returned…]] - `rationale_for` [EXTRACTED]
- [[is_rate_limited_post_retry()]] - `imports` [EXTRACTED]
- [[llm_proxy.py]] - `imports_from` [EXTRACTED]
- [[llm_quota_detector.py]] - `imports_from` [EXTRACTED]
- [[test_detector_empty_body_still_fires_as_generic_cloud()]] - `contains` [EXTRACTED]
- [[test_detector_fires_on_plain_429()]] - `contains` [EXTRACTED]
- [[test_detector_skips_non_429()]] - `contains` [EXTRACTED]
- [[test_proxy_failover_on_post_retry_429()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_anthropic_openai_translatorpy
