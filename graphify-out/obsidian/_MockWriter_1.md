---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L88"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTPConnectProxy
---

# _MockWriter

## Connections
- [[dot-__init__()_214]] - `method` [EXTRACTED]
- [[dot-close()_21]] - `method` [EXTRACTED]
- [[dot-drain()_3]] - `method` [EXTRACTED]
- [[dot-get_extra_info()_1]] - `method` [EXTRACTED]
- [[dot-write()_3]] - `method` [EXTRACTED]
- [[Minimal asyncio.StreamWriter mock that captures written bytes.]] - `rationale_for` [EXTRACTED]
- [[test_blocked_domain_is_tracked_in_recent()]] - `calls` [EXTRACTED]
- [[test_connect_blocked_domain_returns_403()]] - `calls` [EXTRACTED]
- [[test_connect_denied_by_egress_filter_returns_403()]] - `calls` [EXTRACTED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `calls` [EXTRACTED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `calls` [EXTRACTED]
- [[test_http_proxy.py]] - `contains` [EXTRACTED]
- [[test_malformed_request_line_returns_400()]] - `calls` [EXTRACTED]
- [[test_non_connect_method_returns_405()]] - `calls` [EXTRACTED]
- [[test_ssrf_attempt_returns_403()]] - `calls` [EXTRACTED]
- [[test_system_bypass_domain_logs_external_decision()]] - `calls` [EXTRACTED]
- [[test_system_bypass_without_egress_filter()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTPConnectProxy
