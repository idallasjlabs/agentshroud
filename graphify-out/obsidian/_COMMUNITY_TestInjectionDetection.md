---
type: community
members: 47
---

# TestInjectionDetection

**Members:** 47 nodes

## Members
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-test_clean_params_no_findings()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_clean_result_passes_through()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_detected()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_credit_card_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_deeply_nested_pii()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_email_detected_but_low_threat()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_empty_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_fake_system_prompt_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_heavy_url_encoding_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_high()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_highest_threat_none()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_identity_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_inspection_result_threat_level()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_large_base64_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_list_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_low_confidence_not_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_nested_injection_caught()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_network_request_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_no_pii_scan()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_none_values_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_normal_text_not_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_pii_in_tool_result_redacted()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_prompt_override_blocked()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_blocked_strict_with_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_not_blocked_default()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_shell_command_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_small_base64_ok()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_special_token_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_detected_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_ssn_redacted_in_params()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_result_none_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_tool_result_string_content()]] - code - gateway/tests/test_mcp_proxy.py
- [[Enum_26]] - code
- [[FindingType]] - code - gateway/proxy/mcp_inspector.py
- [[In strict mode, sensitive ops with injection ARE blocked.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Sensitive ops are flagged but not blocked in default mode.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[TestInjectionDetection]] - code - gateway/tests/test_mcp_proxy.py
- [[TestInspectorEdgeCases]] - code - gateway/tests/test_mcp_proxy.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSensitiveOps]] - code - gateway/tests/test_mcp_proxy.py
- [[TestSuspiciousEncoding]] - code - gateway/tests/test_mcp_proxy.py
- [[TestThreatLevelCalc]] - code - gateway/tests/test_mcp_proxy.py
- [[Threat level classification.]] - rationale - gateway/proxy/mcp_inspector.py
- [[ThreatLevel_1]] - code - gateway/proxy/mcp_inspector.py
- [[Type of security finding.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInjectionDetection
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_mcp_proxy.py]]

## Top bridge nodes
- [[TestInjectionDetection]] - degree 11, connects to 1 community
- [[FindingType]] - degree 10, connects to 1 community
- [[TestPIIDetection_1]] - degree 10, connects to 1 community
- [[ThreatLevel_1]] - degree 9, connects to 1 community
- [[TestInspectorEdgeCases]] - degree 9, connects to 1 community
