---
source_file: "gateway/tests/test_http_proxy_coverage.py"
type: "code"
community: "HTTP Proxy Coverage Tests"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_Proxy_Coverage_Tests
---

# test_http_proxy_coverage.py

## Connections
- [[HTTPConnectProxy]] - `imports` [EXTRACTED]
- [[WebProxy_1]] - `imports` [EXTRACTED]
- [[WebProxyConfig]] - `imports` [EXTRACTED]
- [[_CloseRaisesTargetWriter]] - `contains` [EXTRACTED]
- [[_CloseRaisesWriter]] - `contains` [EXTRACTED]
- [[_DummyTargetWriter_1]] - `contains` [EXTRACTED]
- [[_HeaderTimeoutReader]] - `contains` [EXTRACTED]
- [[_MockWriter_1]] - `contains` [EXTRACTED]
- [[_SocketTransportWriter]] - `contains` [EXTRACTED]
- [[_TimeoutReader]] - `contains` [EXTRACTED]
- [[_allowlist_proxy()]] - `contains` [EXTRACTED]
- [[_capture_scans()]] - `contains` [EXTRACTED]
- [[_eof_target_connection()]] - `contains` [EXTRACTED]
- [[_make_stream()_1]] - `contains` [EXTRACTED]
- [[test_bypass_logging_failure_does_not_block_tunnel()]] - `contains` [EXTRACTED]
- [[test_bypass_with_egress_filter_lacking_approval_queue()]] - `contains` [EXTRACTED]
- [[test_clamav_scan_clean_records_nothing()]] - `contains` [EXTRACTED]
- [[test_clamav_scan_infected_records_stats()]] - `contains` [EXTRACTED]
- [[test_clamav_scan_unavailable_degrades_silently()]] - `contains` [EXTRACTED]
- [[test_clamav_scan_unlink_failure_swallowed()]] - `contains` [EXTRACTED]
- [[test_empty_request_line_returns_nothing()]] - `contains` [EXTRACTED]
- [[test_handle_client_swallows_generic_exception()]] - `contains` [EXTRACTED]
- [[test_handle_client_swallows_timeout_and_closes_writer()]] - `contains` [EXTRACTED]
- [[test_handle_client_tolerates_writer_close_failure()]] - `contains` [EXTRACTED]
- [[test_header_read_timeout_returns_408()]] - `contains` [EXTRACTED]
- [[test_keepalive_set_on_both_tunnel_ends()]] - `contains` [EXTRACTED]
- [[test_keepalive_skipped_when_socket_is_none()]] - `contains` [EXTRACTED]
- [[test_keepalive_socket_lookup_failure_is_swallowed()]] - `contains` [EXTRACTED]
- [[test_non_numeric_port_returns_400()]] - `contains` [EXTRACTED]
- [[test_recent_stats_trimmed_to_100_entries()]] - `contains` [EXTRACTED]
- [[test_relay_and_scan_idle_timeout_no_data_no_scan()]] - `contains` [EXTRACTED]
- [[test_relay_and_scan_limit_reached_scans_once()]] - `contains` [EXTRACTED]
- [[test_relay_and_scan_read_error_scans_partial_buffer()]] - `contains` [EXTRACTED]
- [[test_relay_and_scan_small_download_scanned_at_eof()]] - `contains` [EXTRACTED]
- [[test_relay_and_scan_swallows_writer_close_failure()]] - `contains` [EXTRACTED]
- [[test_relay_copies_bytes_until_eof()]] - `contains` [EXTRACTED]
- [[test_relay_idle_timeout_closes_writer()]] - `contains` [EXTRACTED]
- [[test_relay_swallows_read_errors()]] - `contains` [EXTRACTED]
- [[test_relay_swallows_writer_close_failure()]] - `contains` [EXTRACTED]
- [[test_request_line_timeout_returns_408()]] - `contains` [EXTRACTED]
- [[test_start_serves_and_stop_closes_loopback()]] - `contains` [EXTRACTED]
- [[test_stop_without_start_is_noop()]] - `contains` [EXTRACTED]
- [[test_target_without_port_defaults_to_443()]] - `contains` [EXTRACTED]
- [[test_tunnel_all_attempts_fail_returns_502()]] - `contains` [EXTRACTED]
- [[test_tunnel_retries_then_succeeds()]] - `contains` [EXTRACTED]
- [[test_tunnel_target_writer_close_failure_swallowed()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_Proxy_Coverage_Tests
