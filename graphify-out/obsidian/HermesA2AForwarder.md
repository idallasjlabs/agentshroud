---
source_file: "gateway/proxy/a2a_proxy.py"
type: "code"
community: "Community 81"
location: "L425"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_81
---

# HermesA2AForwarder

## Connections
- [[.__init__()_18]] - `method` [EXTRACTED]
- [[.close()_7]] - `method` [EXTRACTED]
- [[.forward()]] - `method` [EXTRACTED]
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APeerTestDouble]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[A2AProxy]] - `calls` [EXTRACTED]
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener.      Matches the]] - `rationale_for` [EXTRACTED]
- [[Request_8]] - `uses` [INFERRED]
- [[Response_1]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[a2a_proxy.py]] - `contains` [EXTRACTED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `calls` [EXTRACTED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_81