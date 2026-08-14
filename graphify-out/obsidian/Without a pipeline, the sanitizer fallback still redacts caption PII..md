---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "SECURITY.md"
location: "L5182"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SECURITYmd
---

# Without a pipeline, the sanitizer fallback still redacts caption PII.

## Connections
- [[.test_multipart_sanitizer_fallback_redacts_pii()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SECURITYmd