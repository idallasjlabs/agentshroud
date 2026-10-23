---
type: community
cohesion: 0.04
members: 100
---

# SubagentGovernance

**Cohesion:** 0.04 - loosely connected
**Members:** 100 nodes

## Members
- [[dot-__init__()_143]] - code - gateway/security/subagent_governance.py
- [[dot-_check_budget()]] - code - gateway/security/subagent_governance.py
- [[dot-_log_event()_1]] - code - gateway/security/subagent_governance.py
- [[dot-acceptable()]] - code - gateway/security/subagent_governance.py
- [[dot-authorize_spawn()]] - code - gateway/security/subagent_governance.py
- [[dot-authorize_tool()]] - code - gateway/security/subagent_governance.py
- [[dot-deregister()_1]] - code - gateway/security/subagent_governance.py
- [[dot-get_governance_events()]] - code - gateway/security/subagent_governance.py
- [[dot-get_summary()]] - code - gateway/security/subagent_governance.py
- [[dot-get_usage()]] - code - gateway/security/subagent_governance.py
- [[dot-record_api_call()]] - code - gateway/security/subagent_governance.py
- [[dot-record_egress()]] - code - gateway/security/subagent_governance.py
- [[dot-record_tokens()]] - code - gateway/security/subagent_governance.py
- [[dot-record_tool_call()]] - code - gateway/security/subagent_governance.py
- [[dot-runtime_seconds()]] - code - gateway/security/subagent_governance.py
- [[dot-score_output()]] - code - gateway/security/subagent_governance.py
- [[dot-test_allowed_tool()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_api_calls_exceed()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_api_key_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_api_key_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_basic_spawn()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_clean_output_high_score()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_clean_text_no_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_credit_card_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_in_monitor_still_allows()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_cronjob()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_delegate_task()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_memory()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_denied_tool_send_message()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_depth_exceeded_allowed_in_monitor()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_depth_exceeded_denied()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_depth_penalty_reduces_trust()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_deregister_cleans_up()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_deregister_returns_usage()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_disabled_always_allows()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_email_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_base64()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_hex()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_pattern_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_webhook()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_role()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_system_prompt()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_low_agent_trust_penalty()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_no_tracking_returns_ok()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_pii_detected_lowers_score()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_ssn_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_strict_inheritance_caps_trust()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_summary()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tokens_exceed_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tokens_within_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tool_calls_budget_blocks_authorize_tool()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_warning_at_80_percent()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-to_dict()_8]] - code - gateway/security/subagent_governance.py
- [[Authorize a subagent spawn. Returns (allowed, reason).]] - rationale - gateway/security/subagent_governance.py
- [[Check if a resource budget is exceeded.]] - rationale - gateway/security/subagent_governance.py
- [[Check if a subagent is allowed to use a specific tool.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for PII patterns. Returns list of pattern names found.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for data exfiltration patterns.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for prompt injection patterns.]] - rationale - gateway/security/subagent_governance.py
- [[Configuration for subagent output trust scoring.]] - rationale - gateway/security/subagent_governance.py
- [[Default governance instance in enforce mode.]] - rationale - gateway/tests/test_subagent_governance.py
- [[Get a summary of all subagent governance state for a session.]] - rationale - gateway/security/subagent_governance.py
- [[Get current resource usage for a subagent.]] - rationale - gateway/security/subagent_governance.py
- [[Governance in monitor mode (log but don't block).]] - rationale - gateway/tests/test_subagent_governance.py
- [[GovernanceConfig]] - code - gateway/security/subagent_governance.py
- [[GovernanceEvent]] - code - gateway/security/subagent_governance.py
- [[GovernanceEventType]] - code - gateway/security/subagent_governance.py
- [[OutputScore]] - code - gateway/security/subagent_governance.py
- [[OutputTrustConfig]] - code - gateway/security/subagent_governance.py
- [[Per-subagent resource limits.]] - rationale - gateway/security/subagent_governance.py
- [[Privilege escalation prevention policy.]] - rationale - gateway/security/subagent_governance.py
- [[PrivilegePolicy]] - code - gateway/security/subagent_governance.py
- [[Record a tool invocation.]] - rationale - gateway/security/subagent_governance.py
- [[Record an LLM API call.]] - rationale - gateway/security/subagent_governance.py
- [[Record outbound data volume.]] - rationale - gateway/security/subagent_governance.py
- [[Record token consumption. Returns (within_budget, message).]] - rationale - gateway/security/subagent_governance.py
- [[Remove a subagent from governance tracking. Returns final usage.]] - rationale - gateway/security/subagent_governance.py
- [[ResourceBudget]] - code - gateway/security/subagent_governance.py
- [[ResourceUsage]] - code - gateway/security/subagent_governance.py
- [[Result of scoring a subagent's output.]] - rationale - gateway/security/subagent_governance.py
- [[Score a subagent's output for safety and quality.          In a full deployment,]] - rationale - gateway/security/subagent_governance.py
- [[SubagentGovernance]] - code - gateway/security/subagent_governance.py
- [[TestLifecycle_1]] - code - gateway/tests/test_subagent_governance.py
- [[TestOutputTrustScoring]] - code - gateway/tests/test_subagent_governance.py
- [[TestPatternDetection]] - code - gateway/tests/test_subagent_governance.py
- [[TestResourceBudgets]] - code - gateway/tests/test_subagent_governance.py
- [[TestSpawnAuthorization]] - code - gateway/tests/test_subagent_governance.py
- [[TestToolAuthorization]] - code - gateway/tests/test_subagent_governance.py
- [[Top-level governance configuration.]] - rationale - gateway/security/subagent_governance.py
- [[Tracks cumulative resource consumption for a single subagent.]] - rationale - gateway/security/subagent_governance.py
- [[Unified governance layer for subagent lifecycle.      Wraps SubagentMonitor with]] - rationale - gateway/security/subagent_governance.py
- [[_check_exfil_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_injection_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_pii_patterns()]] - code - gateway/security/subagent_governance.py
- [[disabled_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[gov()]] - code - gateway/tests/test_subagent_governance.py
- [[monitor_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[subagent_governance.py]] - code - gateway/security/subagent_governance.py
- [[test_subagent_governance.py]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SubagentGovernance
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[subagent_governance.py]] - degree 15, connects to 2 communities
- [[test_subagent_governance.py]] - degree 17, connects to 1 community
- [[TestPatternDetection]] - degree 16, connects to 1 community
- [[GovernanceEventType]] - degree 12, connects to 1 community
- [[TestOutputTrustScoring]] - degree 12, connects to 1 community
