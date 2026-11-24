---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "rationale"
community: "TestOutboundPipelineIntegration"
location: "L1875"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutboundPipelineIntegration
---

# Missing content-type must not bypass form draft leak filtering.

## Connections
- [[dot-test_urlencoded_without_content_type_draft_is_still_filtered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutboundPipelineIntegration
