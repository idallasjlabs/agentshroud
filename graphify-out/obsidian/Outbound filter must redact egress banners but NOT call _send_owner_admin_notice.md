---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "test_telegram_proxy_outbound.py"
location: "L4713"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_telegram_proxy_outboundpy
---

# Outbound filter must redact egress banners but NOT call _send_owner_admin_notice

## Connections
- [[TestEgressBannerRedactionNoOwnerNotice]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_telegram_proxy_outboundpy