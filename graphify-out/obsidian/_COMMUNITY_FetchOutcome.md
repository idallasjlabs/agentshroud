---
type: community
members: 91
---

# FetchOutcome

**Members:** 91 nodes

## Members
- [[dot-__init__()_136]] - code - gateway/security/outbound_filter.py
- [[dot-_classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[dot-_compile_patterns()]] - code - gateway/security/outbound_filter.py
- [[dot-_is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[dot-_time_one_filter()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-filter_response()_1]] - code - gateway/security/outbound_filter.py
- [[dot-get_stats()_16]] - code - gateway/security/outbound_filter.py
- [[dot-setup_method()_28]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_code_block_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_common_tools_not_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_custom_patterns()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_edge_cases()_3]] - code - gateway/tests/test_outbound_filter.py
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
- [[dot-test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_risk_classification()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_security_architecture_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_stats()_2]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_tailscale_hostname_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[dot-test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[A single match found by the outbound filter.]] - rationale - gateway/security/outbound_filter.py
- [[Admin-private service references should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[AgentShroud brand name must pass through unredacted (Fix C).]] - rationale - gateway/tests/test_outbound_filter.py
- [[Any_52]] - code - gateway/security/outbound_filter.py
- [[Categories of information that may need filtering.]] - rationale - gateway/security/outbound_filter.py
- [[Check if a disclosure category is permitted for the user's trust level.]] - rationale - gateway/security/outbound_filter.py
- [[Classify the risk level of a response based on info disclosure density.]] - rationale - gateway/security/outbound_filter.py
- [[Compile all filter patterns into regex objects.]] - rationale - gateway/security/outbound_filter.py
- [[Filter agent response for sensitive information disclosure.          Args]] - rationale - gateway/security/outbound_filter.py
- [[FilterMatch]] - code - gateway/security/outbound_filter.py
- [[Get filter statistics.]] - rationale - gateway/security/outbound_filter.py
- [[InfoCategory]] - code - gateway/security/outbound_filter.py
- [[Initialize the outbound information filter.          Args             config C]] - rationale - gateway/security/outbound_filter.py
- [[Integration tests with other security components.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Known collaborator names should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - rationale - gateway/security/outbound_filter.py
- [[Outbound Information Filter Tests]] - code - gateway/tests/test_outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Set up test fixtures._4]] - rationale - gateway/tests/test_outbound_filter.py
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
- [[TestIntegration_1]] - code - gateway/tests/test_outbound_filter.py
- [[TestOutboundInfoFilter]] - code - gateway/tests/test_outbound_filter.py
- [[Workspace runtime paths should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[outbound_filter.py]] - code - gateway/security/outbound_filter.py
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FetchOutcome
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 4 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (2)]]
- 2 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 1 edge to [[_COMMUNITY_Deploying AgentShroud on macOS (Apple Silicon  Intel)]]

## Top bridge nodes
- [[OutboundInfoFilter]] - degree 36, connects to 6 communities
- [[outbound_filter.py]] - degree 7, connects to 4 communities
- [[InfoCategory]] - degree 9, connects to 2 communities
- [[dot-filter_response()_1]] - degree 6, connects to 1 community
- [[test_outbound_filter.py]] - degree 5, connects to 1 community
