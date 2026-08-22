---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "Http Proxy Coverage"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Http_Proxy_Coverage
---

# _MockWriter

## Connections
- [[.__init__()_161]] - `method` [EXTRACTED]
- [[.close()_15]] - `method` [EXTRACTED]
- [[.drain()_2]] - `method` [EXTRACTED]
- [[.get_extra_info()_1]] - `method` [EXTRACTED]
- [[.write()_2]] - `method` [EXTRACTED]
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[Minimal StreamWriter stand-in that records written bytes.]] - `rationale_for` [EXTRACTED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_CloseRaisesWriter]] - `inherits` [EXTRACTED]
- [[_SocketTransportWriter]] - `inherits` [EXTRACTED]
- [[test_bypass_logging_failure_does_not_block_tunnel()]] - `calls` [EXTRACTED]
- [[test_bypass_with_egress_filter_lacking_approval_queue()]] - `calls` [EXTRACTED]
- [[test_empty_request_line_returns_nothing()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_generic_exception()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_timeout_and_closes_writer()]] - `calls` [EXTRACTED]
- [[test_header_read_timeout_returns_408()]] - `calls` [EXTRACTED]
- [[test_http_proxy_coverage.py]] - `contains` [EXTRACTED]
- [[test_non_numeric_port_returns_400()]] - `calls` [EXTRACTED]
- [[test_recent_stats_trimmed_to_100_entries()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_idle_timeout_no_data_no_scan()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_limit_reached_scans_once()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_plain_http_port_still_scans()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_read_error_scans_partial_buffer()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_small_download_scanned_at_eof()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_tls_tunnel_skips_ciphertext_scan()]] - `calls` [EXTRACTED]
- [[test_relay_copies_bytes_until_eof()]] - `calls` [EXTRACTED]
- [[test_relay_idle_timeout_closes_writer()]] - `calls` [EXTRACTED]
- [[test_relay_swallows_read_errors()]] - `calls` [EXTRACTED]
- [[test_request_line_timeout_returns_408()]] - `calls` [EXTRACTED]
- [[test_target_without_port_defaults_to_443()]] - `calls` [EXTRACTED]
- [[test_tunnel_all_attempts_fail_returns_502()]] - `calls` [EXTRACTED]
- [[test_tunnel_connect_falls_back_when_happy_eyeballs_unsupported()]] - `calls` [EXTRACTED]
- [[test_tunnel_connect_uses_happy_eyeballs()]] - `calls` [EXTRACTED]
- [[test_tunnel_retries_then_succeeds()]] - `calls` [EXTRACTED]
- [[test_tunnel_target_writer_close_failure_swallowed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Http_Proxy_Coverage