---
type: community
cohesion: 0.03
members: 63
---

# TestOutboundInfoFilter

**Cohesion:** 0.03 - loosely connected
**Members:** 63 nodes

## Members
- [[dot-_time_one_filter()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-setup_method()_37]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_code_block_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_common_tools_not_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_custom_patterns()_1]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_edge_cases()_4]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_initialization_default()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_internal_url_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_mcp_tool_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_multiple_categories()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_operational_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_partial_xml_tool_tag_is_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_pattern_overlaps()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_performance()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_risk_classification()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_security_architecture_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_stats()_2]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailscale_hostname_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[Admin-private service references should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[AgentShroud brand name must pass through unredacted (Fix C).]] - rationale - gateway/tests/test_outbound_filter.py
- [[Known collaborator names should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Set up test fixtures._5]] - rationale - gateway/tests/test_outbound_filter.py
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
- [[Test that private IP addresses are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that security module references are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that sensitive MCP tool names are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that tailnet IDs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that trust level overrides work correctly.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestOutboundInfoFilter]] - code - gateway/tests/test_outbound_filter.py
- [[Workspace runtime paths should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 2 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]

## Top bridge nodes
- [[TestOutboundInfoFilter]] - degree 35, connects to 2 communities
- [[dot-setup_method()_37]] - degree 3, connects to 1 community
- [[dot-test_custom_patterns()_1]] - degree 3, connects to 1 community
- [[dot-test_initialization_with_config()]] - degree 3, connects to 1 community
- [[dot-test_monitor_mode()]] - degree 3, connects to 1 community
