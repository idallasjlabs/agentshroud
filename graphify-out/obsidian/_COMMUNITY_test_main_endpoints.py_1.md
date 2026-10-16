---
type: community
cohesion: 0.08
members: 26
---

# test_main_endpoints.py

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-setup_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_disallowed_vault_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_malformed_reference_returns_422()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_op_subprocess_failure_returns_502()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_path_traversal_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_requires_auth()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_valid_reference_returns_value()]] - code - gateway/tests/test_op_proxy.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_op_proxy.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestOpProxyEndpoint]] - code - gateway/tests/test_op_proxy.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py
- [[auth_dep()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_main_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 2 edges to [[_COMMUNITY_forward.py]]
- 2 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_GatewayEmailService]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]

## Top bridge nodes
- [[auth_dep()]] - degree 14, connects to 7 communities
- [[TestScanParameterAllowlists]] - degree 11, connects to 1 community
- [[TestOpProxyEndpoint]] - degree 8, connects to 1 community
- [[TestQuarantineEndpoints]] - degree 5, connects to 1 community
