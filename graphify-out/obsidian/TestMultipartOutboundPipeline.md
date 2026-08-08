---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Gateway Test Suite"
location: "L5007"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestMultipartOutboundPipeline

## Connections
- [[.test_multipart_fails_closed_for_non_owner()]] - `method` [EXTRACTED]
- [[.test_multipart_outbound_pipeline_called()]] - `method` [EXTRACTED]
- [[.test_multipart_overlength_caption_blocked_for_non_owner()]] - `method` [EXTRACTED]
- [[.test_multipart_owner_exempt_from_fail_closed()]] - `method` [EXTRACTED]
- [[.test_multipart_pipeline_block_non_owner()]] - `method` [EXTRACTED]
- [[.test_multipart_sanitized_caption_applied_binary_intact()]] - `method` [EXTRACTED]
- [[.test_multipart_sanitizer_fallback_redacts_pii()]] - `method` [EXTRACTED]
- [[.test_multipart_text_field_scanned_when_no_caption()]] - `method` [EXTRACTED]
- [[.test_multipart_without_text_part_passes_through()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[Multipart captions must get the full pipeline scan, not just the XML filter.]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite