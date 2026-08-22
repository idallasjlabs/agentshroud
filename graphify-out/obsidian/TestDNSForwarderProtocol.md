---
source_file: "gateway/tests/test_dns_canvas_coverage.py"
type: "code"
community: "Dns Canvas Coverage"
location: "L221"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Dns_Canvas_Coverage
---

# TestDNSForwarderProtocol

## Connections
- [[._make_protocol()]] - `method` [EXTRACTED]
- [[.test_all_upstreams_fail_sends_servfail()]] - `method` [EXTRACTED]
- [[.test_blocked_a_query_returns_zero_ip()]] - `method` [EXTRACTED]
- [[.test_blocked_aaaa_query_returns_null_ipv6()]] - `method` [EXTRACTED]
- [[.test_blocked_other_qtype_returns_nxdomain()]] - `method` [EXTRACTED]
- [[.test_datagram_received_schedules_handler()]] - `method` [EXTRACTED]
- [[.test_error_received_logs()]] - `method` [EXTRACTED]
- [[.test_forwarded_query_relays_upstream_response()]] - `method` [EXTRACTED]
- [[.test_short_upstream_response_still_relayed()]] - `method` [EXTRACTED]
- [[.test_unparseable_short_query_no_servfail_sent()]] - `method` [EXTRACTED]
- [[DNSBlocklist]] - `uses` [INFERRED]
- [[DNSForwarderProtocol]] - `uses` [INFERRED]
- [[test_dns_canvas_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Dns_Canvas_Coverage