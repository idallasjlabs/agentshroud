---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Gateway Test Suite"
location: "L8456"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# TestFileDownload

## Connections
- [[.test_forward_file_download_aborts_at_size_limit()]] - `method` [EXTRACTED]
- [[.test_forward_file_download_returns_raw_body_sentinel()]] - `method` [EXTRACTED]
- [[.test_oversized_document_update_is_dropped()]] - `method` [EXTRACTED]
- [[.test_proxy_request_api_path_still_json_parsed()]] - `method` [EXTRACTED]
- [[.test_proxy_request_file_download_error_returns_502()]] - `method` [EXTRACTED]
- [[.test_proxy_request_file_prefix_returns_binary_sentinel()]] - `method` [EXTRACTED]
- [[.test_within_limit_document_update_passes()]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Tests for _forward_file_download() and proxy_request() binary path.      Regress]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite