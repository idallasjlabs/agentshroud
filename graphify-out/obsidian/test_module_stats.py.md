---
source_file: "gateway/tests/test_module_stats.py"
type: "code"
community: "ADR-006: Multi-Runtime Container Support"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-006_Multi-Runtime_Container_Support
---

# test_module_stats.py

## Connections
- [[Decision_2]] - `imports` [EXTRACTED]
- [[EgressAction]] - `imports` [EXTRACTED]
- [[EgressFilter_2]] - `imports` [EXTRACTED]
- [[ModuleStatsCollector]] - `imports` [EXTRACTED]
- [[TestEgressWiringEndToEnd]] - `contains` [EXTRACTED]
- [[TestEnforcementWiring]] - `contains` [EXTRACTED]
- [[ToolACLEnforcer]] - `imports` [EXTRACTED]
- [[get_collector()]] - `imports` [EXTRACTED]
- [[module_stats.py]] - `references` [EXTRACTED]
- [[record_decision()]] - `imports` [EXTRACTED]
- [[test_block_rate_computed()]] - `contains` [EXTRACTED]
- [[test_empty_module_zero_rate_not_division_error()]] - `contains` [EXTRACTED]
- [[test_record_and_snapshot()]] - `contains` [EXTRACTED]
- [[test_record_ignores_invalid_decision_safely()]] - `contains` [EXTRACTED]
- [[test_reset()]] - `contains` [EXTRACTED]
- [[test_sanitize_decision()]] - `contains` [EXTRACTED]
- [[test_thread_safe_under_concurrency()]] - `contains` [EXTRACTED]
- [[test_unknown_module_created_on_demand()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-006_Multi-Runtime_Container_Support
