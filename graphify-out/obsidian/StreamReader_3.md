---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "Community 67"
location: "L33"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_67
---

# StreamReader

## Connections
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_make_stream()_1]] - `references` [EXTRACTED]
- [[test_empty_request_line_returns_nothing()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_generic_exception()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_timeout_and_closes_writer()]] - `calls` [EXTRACTED]
- [[test_handle_client_tolerates_writer_close_failure()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_limit_reached_scans_once()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_plain_http_port_still_scans()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_small_download_scanned_at_eof()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_swallows_writer_close_failure()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_tls_tunnel_skips_ciphertext_scan()]] - `calls` [EXTRACTED]
- [[test_relay_copies_bytes_until_eof()]] - `calls` [EXTRACTED]
- [[test_relay_swallows_writer_close_failure()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_67