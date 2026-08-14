---
type: community
members: 42
---

# Bot CVE Scorecard

**Members:** 42 nodes

## Members
- [[.setup_method()_17]] - code - gateway/tests/test_outbound_filter.py
- [[.test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_custom_patterns()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_edge_cases()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_internal_url_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_mcp_tool_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_multiple_categories()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_operational_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_pattern_overlaps()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_stats()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[Admin-private service references should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[AgentShroud brand name must pass through unredacted (Fix C).]] - rationale - gateway/tests/test_outbound_filter.py
- [[Known collaborator names should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Set up test fixtures.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test adding custom filter patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test against realistic attack scenarios.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test context-aware user ID filtering.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test edge cases and boundary conditions.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter initializes with custom configuration.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filter statistics.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test filtering with multiple information categories.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test handling of overlapping patterns.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test suite for the outbound information filter.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that Telegram user IDs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that credential paths are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that internal URLs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that internal file paths are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that private IP addresses are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that sensitive MCP tool names are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Test that tailnet IDs are filtered.]] - rationale - gateway/tests/test_outbound_filter.py
- [[TestOutboundInfoFilter]] - code - gateway/tests/test_outbound_filter.py
- [[Workspace runtime paths should be redacted.]] - rationale - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bot_CVE_Scorecard
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_MCP Proxy Config]]
- 2 edges to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_Community 1519]]
- 1 edge to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_Docker Deploy Scripts]]
- 1 edge to [[_COMMUNITY_Community 1521]]
- 1 edge to [[_COMMUNITY_docsproject]]
- 1 edge to [[_COMMUNITY_Community 1522]]
- 1 edge to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_Community 1525]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]

## Top bridge nodes
- [[TestOutboundInfoFilter]] - degree 37, connects to 11 communities
- [[.setup_method()_17]] - degree 3, connects to 1 community
- [[.test_initialization_with_config()]] - degree 3, connects to 1 community
- [[.test_custom_patterns()]] - degree 3, connects to 1 community