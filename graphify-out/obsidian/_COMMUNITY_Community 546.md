---
type: community
cohesion: 0.12
members: 17
---

# Community 546

**Cohesion:** 0.12 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_forward_file_download_aborts_at_size_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_forward_file_download_returns_raw_body_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_oversized_document_update_is_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_proxy_request_api_path_still_json_parsed()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_proxy_request_file_download_error_returns_502()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_proxy_request_file_prefix_returns_binary_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[ri for a user not in immune set must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size  limit must be dropped (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for _forward_file_download() and proxy_request() binary path.      Regress]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download must raise when streamed bytes exceed limit (CVE-2026-320]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download returns dict with _raw_body, _content_type, _status_code.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request returns 502 sentinel when file download raises.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request with path_prefix='file' returns _raw_body sentinel (no JSON parse]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request without file prefix still JSON-parses the response.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_546
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 4 edges to [[_COMMUNITY_Community 31]]
- 1 edge to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]
- 1 edge to [[_COMMUNITY_Community 77]]

## Top bridge nodes
- [[TestFileDownload]] - degree 12, connects to 4 communities
- [[.test_oversized_document_update_is_dropped()]] - degree 6, connects to 2 communities
- [[.test_within_limit_document_update_passes()]] - degree 6, connects to 2 communities
- [[.test_forward_file_download_aborts_at_size_limit()]] - degree 4, connects to 2 communities
- [[.test_forward_file_download_returns_raw_body_sentinel()]] - degree 4, connects to 1 community