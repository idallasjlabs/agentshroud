---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L4701"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Outbound filter must redact egress banners but NOT call _send_owner_admin_notice

## Connections
- [[TestEgressBannerRedactionNoOwnerNotice]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline