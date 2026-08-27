---
type: community
members: 79
---

# Community 1338

**Members:** 79 nodes

## Members
- [[.__init__()_103]] - code - gateway/security/outbound_filter.py
- [[._compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[._time_one_filter()]] - code - gateway/tests/test_outbound_filter.py
- [[.get_stats()_17]] - code - gateway/security/outbound_filter.py
- [[.setup_method()_17]] - code - gateway/tests/test_outbound_filter.py
- [[.test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_code_block_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_common_tools_not_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_custom_patterns()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_edge_cases()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_default()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_internal_url_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_mcp_tool_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_multiple_categories()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_operational_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_partial_xml_tool_tag_is_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_pattern_overlaps()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_performance()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_risk_classification()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_security_architecture_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_stats()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_tailscale_hostname_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[Admin-private service references should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[AgentShroud brand name must pass through unredacted (Fix C).]] - rationale - gateway/tests/test_outbound_filter.py
- [[Any_52]] - code - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Known collaborator names should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Set up test fixtures.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Split-fragment XML tags must still be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test adding custom filter patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test against realistic attack scenarios.]] - rationale - gateway/tests/test_outbound_filter.py
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
- [[TestIntegration]] - code - gateway/tests/test_outbound_filter.py
- [[TestOutboundInfoFilter]] - code - gateway/tests/test_outbound_filter.py
- [[Workspace runtime paths should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1338
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 22]]
- 2 edges to [[_COMMUNITY_Community 23]]
- 1 edge to [[_COMMUNITY_Community 78]]

## Top bridge nodes
- [[InfoCategory]] - degree 9, connects to 3 communities
- [[test_outbound_filter.py]] - degree 5, connects to 2 communities
- [[TestOutboundInfoFilter]] - degree 35, connects to 1 community
- [[TestIntegration]] - degree 6, connects to 1 community
- [[.__init__()_103]] - degree 5, connects to 1 community