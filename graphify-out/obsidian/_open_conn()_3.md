---
source_file: "gateway/tests/test_http_proxy.py"
type: "code"
community: "HTTPConnectProxy"
location: "L230"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/HTTPConnectProxy
---

# _open_conn()

## Connections
- [[_DummyTargetWriter_1]] - `calls` [EXTRACTED]
- [[test_connect_system_bypass_domain_skips_policy_checks()]] - `indirect_call` [INFERRED]
- [[test_connect_unknown_domain_can_be_allowed_by_interactive_egress()]] - `indirect_call` [INFERRED]
- [[test_system_bypass_domain_logs_external_decision()]] - `indirect_call` [INFERRED]
- [[test_system_bypass_without_egress_filter()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/HTTPConnectProxy
