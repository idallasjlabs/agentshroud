---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Sunday Upgrade Report — 2026-09-17 (prod, on-demand)"
location: "L7789"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Sunday_Upgrade_Report__2026-09-17_prod_on-demand
---

# .test_stranger_rate_limit_cooldown_suppresses_repeated_notices()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Repeated rate-limited messages within the cooldown window send at most one…]] - `rationale_for` [EXTRACTED]
- [[TestStrangerRateLimit]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_rl_notice()_2]] - `contains` [EXTRACTED]
- [[fake_rl_notice()_1]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Sunday_Upgrade_Report__2026-09-17_prod_on-demand
