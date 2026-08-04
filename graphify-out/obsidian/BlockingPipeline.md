---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Authentication & Rate Limiting"
location: "L79"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Authentication__Rate_Limiting
---

# BlockingPipeline

## Connections
- [[.process_inbound()_5]] - `method` [EXTRACTED]
- [[.test_clean_message_passes_through()]] - `calls` [EXTRACTED]
- [[.test_form_outbound_pipeline_block_non_owner()]] - `calls` [INFERRED]
- [[.test_inbound_text_normalized_before_pipeline()]] - `calls` [EXTRACTED]
- [[.test_json_caption_pipeline_block_replaces_caption()]] - `calls` [INFERRED]
- [[.test_multipart_pipeline_block_non_owner()]] - `calls` [INFERRED]
- [[.test_owner_message_not_blocked()]] - `calls` [EXTRACTED]
- [[.test_prompt_injection_blocked_on_getUpdates()]] - `calls` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Pipeline that blocks any message containing injection keywords.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Authentication__Rate_Limiting
