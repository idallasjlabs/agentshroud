---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Community 521"
location: "L79"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_521
---

# BlockingPipeline

## Connections
- [[dot-process_inbound()_7]] - `method` [EXTRACTED]
- [[dot-test_clean_message_passes_through()]] - `calls` [EXTRACTED]
- [[dot-test_form_outbound_pipeline_block_non_owner()]] - `calls` [INFERRED]
- [[dot-test_inbound_text_normalized_before_pipeline()]] - `calls` [EXTRACTED]
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - `calls` [INFERRED]
- [[dot-test_multipart_pipeline_block_non_owner()]] - `calls` [INFERRED]
- [[dot-test_owner_message_not_blocked()]] - `calls` [EXTRACTED]
- [[dot-test_prompt_injection_blocked_on_getUpdates()]] - `calls` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[Pipeline that blocks any message containing injection keywords.]] - `rationale_for` [EXTRACTED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_521