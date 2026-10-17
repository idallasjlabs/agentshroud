---
type: community
members: 15
---

# Tests for _forward_file_download() and proxy_request() binary path. Regression…

**Members:** 15 nodes

## Members
- [[dot-test_forward_file_download_aborts_at_size_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_oversized_document_update_is_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_api_path_still_json_parsed()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_download_error_returns_502()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_prefix_returns_binary_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size  limit must be dropped (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for _forward_file_download() and proxy_request() binary path. Regression…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download must raise when streamed bytes exceed limit…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request returns 502 sentinel when file download raises.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request with path_prefix='file' returns _raw_body sentinel (no JSON…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request without file prefix still JSON-parses the response.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tests_for__forward_file_download_and_proxy_request_binary_path_Regression
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 4 edges to [[_COMMUNITY_FakeRBAC]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]

## Top bridge nodes
- [[dot-test_oversized_document_update_is_dropped()]] - degree 6, connects to 3 communities
- [[dot-test_within_limit_document_update_passes()]] - degree 6, connects to 3 communities
- [[TestFileDownload]] - degree 9, connects to 2 communities
- [[dot-test_forward_file_download_aborts_at_size_limit()]] - degree 4, connects to 1 community
- [[dot-test_proxy_request_api_path_still_json_parsed()]] - degree 3, connects to 1 community
