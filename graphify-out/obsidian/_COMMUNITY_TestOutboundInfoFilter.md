---
type: community
members: 120
---

# TestOutboundInfoFilter

**Members:** 120 nodes

## Members
- [[dot-__init__()_98]] - code - gateway/security/outbound_filter.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[dot-_has_fabricated_match()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-_time_one_filter()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-filter_response()]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_10]] - code - gateway/security/outbound_filter.py
- [[dot-setup_method()_14]] - code - gateway/tests/test_outbound_filter.py
- [[dot-setup_method()_15]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocked_unauthorized_command()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_blocking_suspicious_code_execution()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_case_insensitive()_1]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_category_is_operational()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_code_block_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_common_tools_not_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_continues_blocking()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_custom_patterns()_1]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_edge_cases()_3]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_exact_past_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_flagging_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_initialization_default()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_internal_url_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_legitimate_responses_not_matched()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_mcp_tool_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_multiple_categories()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_operational_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_partial_xml_tool_tag_is_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_pattern_overlaps()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_performance()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_possessive_flagging()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_present_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_prevents_form()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_progressive_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_redaction_applied()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_risk_classification()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_security_architecture_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_stats()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailscale_hostname_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Admin-private service references should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[AgentShroud brand name must pass through unredacted (Fix C).]] - rationale - gateway/tests/test_outbound_filter.py
- [[Any_32]] - code - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[FR4 Data Confidentiality]] - concept - docs/compliance/iec-62443-matrix.md
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Known collaborator names should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - rationale - gateway/security/outbound_filter.py
- [[Matched text is replaced with RESPONSE_FILTERED.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Normal helpful responses must NOT trigger the pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Original pattern exact past-tense form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Outbound Information Filter Tests]] - code - gateway/tests/test_outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Pattern is case-insensitive.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Pattern is in the OPERATIONAL category.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Possessive form AGENTSHROUD's behavioral analysis flagging.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Set up test fixtures._3]] - rationale - gateway/tests/test_outbound_filter.py
- [[Split-fragment XML tags must still be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Standalone 'blocked unauthorized command execution' without AGENTSHROUD prefix.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test adding custom filter patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test against realistic attack scenarios.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test cases for the widened fabricated_security_notice pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test context-aware user ID filtering.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test edge cases and boundary conditions.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter initializes with custom configuration.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter initializes with default configuration.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter statistics.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filtering with multiple information categories.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test handling of overlapping patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test response risk level classification.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test suite for the outbound information filter.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that Tailscale hostnames are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that Telegram user IDs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that common English words are not filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that credential paths are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that filtering performance is acceptable.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that function_calls XML blocks are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that internal URLs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that internal file paths are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that monitor mode logs but doesn't redact.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that outbound filter works alongside PII sanitizer.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that private IP addresses are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that security module references are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that sensitive MCP tool names are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that tailnet IDs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that trust level overrides work correctly.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test with realistic agent response patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestFabricatedSecurityNotice]] - code - gateway/tests/test_outbound_filter.py
- [[TestIntegration]] - code - gateway/tests/test_outbound_filter.py
- [[TestOutboundInfoFilter]] - code - gateway/tests/test_outbound_filter.py
- [[Workspace runtime paths should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[blocking suspicious code execution' variant.]] - rationale - gateway/tests/test_outbound_filter.py
- [[blocking' continuous form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[continues blocking' — adverb + gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[flagging' gerund form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_AuditChain]]
- 4 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_AlertDispatcher (2) (4)]]
- 2 edges to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_diagramsREADME]]
- 1 edge to [[_COMMUNITY_PHASE_3A_3B_IMPLEMENTATION]]

## Top bridge nodes
- [[FR4 Data Confidentiality]] - degree 8, connects to 6 communities
- [[OutboundInfoFilter]] - degree 38, connects to 4 communities
- [[outbound_filter.py]] - degree 9, connects to 4 communities
- [[InfoCategory]] - degree 9, connects to 1 community
- [[dot-filter_response()]] - degree 6, connects to 1 community
