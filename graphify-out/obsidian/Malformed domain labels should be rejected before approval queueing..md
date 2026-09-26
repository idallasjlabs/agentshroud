---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "_PII_PATTERNS (URL PII regex set)"
location: "L2970"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_PII_PATTERNS_URL_PII_regex_set
---

# Malformed domain labels should be rejected before approval queueing.

## Connections
- [[.test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_PII_PATTERNS_URL_PII_regex_set