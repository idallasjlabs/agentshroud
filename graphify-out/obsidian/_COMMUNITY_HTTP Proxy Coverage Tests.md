---
type: community
cohesion: 0.07
members: 66
---

# HTTP Proxy Coverage Tests

**Cohesion:** 0.07 - loosely connected
**Members:** 66 nodes

## Members
- [[.__init__()_120]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.__init__()_119]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.__init__()_122]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.close()_12]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.close()_11]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.drain()_2]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.get_extra_info()_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.readline()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[.write()_2]] - code - gateway/tests/test_http_proxy_coverage.py
- [[Bytes relayed before a connection error are still sampled for scanning.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[Egress filter without _approval_queue attr - bypass proceeds silently.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[First open_connection attempt fails; retry (with patched sleep) succeeds.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[First readline returns the request line; the next stalls.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[HTTPConnectProxy_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[Host-only CONNECT target defaults to port 443; blocked host - 403.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[Minimal StreamWriter stand-in that records written bytes.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[StreamReader_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[Transport without an underlying socket (None) is skipped cleanly.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[Writer exposing a .transport whose socket records setsockopt calls.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[_CloseRaisesWriter]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_HeaderTimeoutReader]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_MockWriter_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_SocketTransportWriter]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_TimeoutReader]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_allowlist_proxy()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_capture_scans()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_eof_target_connection()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_make_stream()_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[asyncio.open_connection replacement returning an immediately-EOF stream.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[clamscan binary missing (sidecar down) - no exception, temp file removed.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[get_extra_info raising must not break the established tunnel.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[log_external_decision raising must not break the CONNECT.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[readline() always raises TimeoutError — simulates a stalled client.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[target_writer.close() raising after relay completes must not propagate.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[test_bypass_logging_failure_does_not_block_tunnel()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_bypass_with_egress_filter_lacking_approval_queue()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_clean_records_nothing()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_infected_records_stats()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unavailable_degrades_silently()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unlink_failure_swallowed()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_empty_request_line_returns_nothing()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_handle_client_swallows_generic_exception()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_handle_client_swallows_timeout_and_closes_writer()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_handle_client_tolerates_writer_close_failure()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_header_read_timeout_returns_408()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_http_proxy_coverage.py]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_keepalive_set_on_both_tunnel_ends()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_keepalive_skipped_when_socket_is_none()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_keepalive_socket_lookup_failure_is_swallowed()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_non_numeric_port_returns_400()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_recent_stats_trimmed_to_100_entries()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_and_scan_idle_timeout_no_data_no_scan()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_and_scan_limit_reached_scans_once()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_and_scan_read_error_scans_partial_buffer()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_and_scan_small_download_scanned_at_eof()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_and_scan_swallows_writer_close_failure()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_copies_bytes_until_eof()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_idle_timeout_closes_writer()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_swallows_read_errors()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_relay_swallows_writer_close_failure()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_request_line_timeout_returns_408()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_stop_without_start_is_noop()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_target_without_port_defaults_to_443()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_tunnel_all_attempts_fail_returns_502()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_tunnel_retries_then_succeeds()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_tunnel_target_writer_close_failure_swallowed()]] - code - gateway/tests/test_http_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HTTP_Proxy_Coverage_Tests
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_Module Group 65]]
- 18 edges to [[_COMMUNITY_HTTP CONNECT Proxy & Egress]]
- 5 edges to [[_COMMUNITY_Module Group 386]]

## Top bridge nodes
- [[test_http_proxy_coverage.py]] - degree 46, connects to 3 communities
- [[HTTPConnectProxy_1]] - degree 31, connects to 3 communities
- [[_HeaderTimeoutReader]] - degree 8, connects to 3 communities
- [[_MockWriter_1]] - degree 32, connects to 2 communities
- [[StreamReader_1]] - degree 13, connects to 2 communities