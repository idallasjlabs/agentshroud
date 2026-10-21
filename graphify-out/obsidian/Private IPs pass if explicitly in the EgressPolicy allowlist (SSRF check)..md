---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "TestOutboundPipelineIntegration"
location: "L134"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOutboundPipelineIntegration
---

# Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).

## Connections
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOutboundPipelineIntegration
