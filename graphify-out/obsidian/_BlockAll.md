---
source_file: "gateway/tests/test_dns_canvas_coverage.py"
type: "code"
community: "Dns Canvas Coverage"
location: "L53"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Dns_Canvas_Coverage
---

# _BlockAll

## Connections
- [[.is_blocked()_1]] - `method` [EXTRACTED]
- [[.test_blocked_a_query_returns_zero_ip()]] - `calls` [EXTRACTED]
- [[.test_blocked_aaaa_query_returns_null_ipv6()]] - `calls` [EXTRACTED]
- [[.test_blocked_other_qtype_returns_nxdomain()]] - `calls` [EXTRACTED]
- [[.test_datagram_received_schedules_handler()]] - `calls` [EXTRACTED]
- [[Blocklist stub that blocks every domain.]] - `rationale_for` [EXTRACTED]
- [[DNSBlocklist]] - `uses` [INFERRED]
- [[DNSForwarderProtocol]] - `uses` [INFERRED]
- [[test_dns_canvas_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Dns_Canvas_Coverage