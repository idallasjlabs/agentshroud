---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: ".test_stranger_rate_limit_notice_includes_reset_time"
location: "L7820"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_stranger_rate_limit_notice_includes_reset_time
---

# .test_stranger_rate_limit_notice_includes_reset_time()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestStrangerRateLimit]] - `method` [EXTRACTED]
- [[_send_stranger_rate_limit_notice must include a reset time in HHMM UTC format.]] - `rationale_for` [EXTRACTED]
- [[asyncio_21]] - `references` [EXTRACTED]
- [[fake_urlopen()_33]] - `contains` [EXTRACTED]
- [[fake_urlopen()_62]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_stranger_rate_limit_notice_includes_reset_time
