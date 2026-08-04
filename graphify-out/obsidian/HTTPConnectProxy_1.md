---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "HTTP Proxy Coverage Tests"
location: "L106"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_Proxy_Coverage_Tests
---

# HTTPConnectProxy

## Connections
- [[HTTPConnectProxy]] - `uses` [INFERRED]
- [[WebProxy_1]] - `uses` [INFERRED]
- [[WebProxyConfig]] - `uses` [INFERRED]
- [[_allowlist_proxy()]] - `references` [EXTRACTED]
- [[_capture_scans()]] - `references` [EXTRACTED]
- [[test_bypass_logging_failure_does_not_block_tunnel()]] - `calls` [EXTRACTED]
- [[test_bypass_with_egress_filter_lacking_approval_queue()]] - `calls` [EXTRACTED]
- [[test_clamav_scan_clean_records_nothing()]] - `calls` [EXTRACTED]
- [[test_clamav_scan_infected_records_stats()]] - `calls` [EXTRACTED]
- [[test_clamav_scan_unavailable_degrades_silently()]] - `calls` [EXTRACTED]
- [[test_clamav_scan_unlink_failure_swallowed()]] - `calls` [EXTRACTED]
- [[test_empty_request_line_returns_nothing()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_generic_exception()]] - `calls` [EXTRACTED]
- [[test_handle_client_swallows_timeout_and_closes_writer()]] - `calls` [EXTRACTED]
- [[test_handle_client_tolerates_writer_close_failure()]] - `calls` [EXTRACTED]
- [[test_header_read_timeout_returns_408()]] - `calls` [EXTRACTED]
- [[test_keepalive_set_on_both_tunnel_ends()]] - `calls` [EXTRACTED]
- [[test_keepalive_skipped_when_socket_is_none()]] - `calls` [EXTRACTED]
- [[test_keepalive_socket_lookup_failure_is_swallowed()]] - `calls` [EXTRACTED]
- [[test_non_numeric_port_returns_400()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_idle_timeout_no_data_no_scan()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_limit_reached_scans_once()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_read_error_scans_partial_buffer()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_small_download_scanned_at_eof()]] - `calls` [EXTRACTED]
- [[test_relay_and_scan_swallows_writer_close_failure()]] - `calls` [EXTRACTED]
- [[test_request_line_timeout_returns_408()]] - `calls` [EXTRACTED]
- [[test_start_serves_and_stop_closes_loopback()]] - `calls` [EXTRACTED]
- [[test_stop_without_start_is_noop()]] - `calls` [EXTRACTED]
- [[test_tunnel_all_attempts_fail_returns_502()]] - `calls` [EXTRACTED]
- [[test_tunnel_retries_then_succeeds()]] - `calls` [EXTRACTED]
- [[test_tunnel_target_writer_close_failure_swallowed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_Proxy_Coverage_Tests
