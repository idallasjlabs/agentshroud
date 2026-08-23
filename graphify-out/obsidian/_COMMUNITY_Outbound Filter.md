---
type: community
cohesion: 0.02
members: 119
---

# Outbound Filter

**Cohesion:** 0.02 - loosely connected
**Members:** 119 nodes

## Members
- [[.__init__()_103]] - code - gateway/security/outbound_filter.py
- [[._classify_response_risk()]] - code - gateway/security/outbound_filter.py
- [[._compile_patterns()_1]] - code - gateway/security/outbound_filter.py
- [[._has_fabricated_match()]] - code - gateway/tests/test_outbound_filter.py
- [[._is_allowed_for_trust()]] - code - gateway/security/outbound_filter.py
- [[._time_one_filter()]] - code - gateway/tests/test_outbound_filter.py
- [[.filter_response()]] - code - gateway/security/outbound_filter.py
- [[.get_stats()_17]] - code - gateway/security/outbound_filter.py
- [[.setup_method()_18]] - code - gateway/tests/test_outbound_filter.py
- [[.setup_method()_17]] - code - gateway/tests/test_outbound_filter.py
- [[.test_admin_private_service_data_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_agentshroud_name_not_redacted()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_blocked_unauthorized_command()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_blocking_suspicious_code_execution()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_case_insensitive()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_category_is_operational()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_code_block_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_collaborator_name_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_common_tools_not_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_comprehensive_attack_scenarios()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_context_aware_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_continues_blocking()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_credential_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_custom_patterns()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_edge_cases()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_exact_past_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_flagging_form()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_default()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_initialization_with_config()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_internal_url_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_legitimate_responses_not_matched()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_mcp_tool_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_monitor_mode()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_multiple_categories()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_operational_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_outbound_filter_still_escalates_fabricated_notice()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_partial_xml_tool_tag_is_filtered()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_pattern_overlaps()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_performance()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_possessive_flagging()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_present_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_prevents_form()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_private_ip_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_progressive_tense()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_real_world_agent_responses()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_redaction_applied()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_risk_classification()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_security_architecture_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_stats()_1]] - code - gateway/tests/test_outbound_filter.py
- [[.test_tailnet_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_tailscale_hostname_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_telegram_user_id_filtering()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_trust_level_overrides()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_with_pii_sanitizer_compatibility()]] - code - gateway/tests/test_outbound_filter.py
- [[.test_workspace_internal_path_filtering()]] - code - gateway/tests/test_outbound_filter.py
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
- [[Matched text is replaced with RESPONSE_FILTERED.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Normal helpful responses must NOT trigger the pattern.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Original pattern exact past-tense form.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Outbound Information Filter Tests]] - code - gateway/tests/test_outbound_filter.py
- [[OutboundInfoFilter]] - code - gateway/security/outbound_filter.py
- [[Pattern is case-insensitive.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Pattern is in the OPERATIONAL category.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Possessive form AGENTSHROUD's behavioral analysis flagging.]] - rationale - gateway/tests/test_outbound_filter.py
- [[Set up test fixtures.]] - rationale - gateway/tests/test_outbound_filter.py
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
- [[test_outbound_filter.py]] - code - gateway/tests/test_outbound_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Outbound_Filter
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Pipeline Unit]]
- 7 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Key Vault]]
- 1 edge to [[_COMMUNITY_Prompt Protection (security)]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[OutboundInfoFilter]] - degree 38, connects to 5 communities
- [[.test_outbound_filter_still_escalates_fabricated_notice()]] - degree 4, connects to 3 communities
- [[InfoCategory]] - degree 9, connects to 2 communities
- [[.filter_response()]] - degree 6, connects to 1 community
- [[FilterMatch]] - degree 4, connects to 1 community