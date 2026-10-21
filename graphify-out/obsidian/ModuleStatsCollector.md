---
source_file: "gateway/security/module_stats.py"
type: "code"
community: "ADR-006: Multi-Runtime Container Support"
location: "L38"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ADR-006_Multi-Runtime_Container_Support
---

# ModuleStatsCollector

## Connections
- [[dot-__init__()_123]] - `method` [EXTRACTED]
- [[dot-record()]] - `method` [EXTRACTED]
- [[dot-reset()_1]] - `method` [EXTRACTED]
- [[dot-snapshot()]] - `method` [EXTRACTED]
- [[TestEgressWiringEndToEnd]] - `uses` [INFERRED]
- [[TestEnforcementWiring]] - `uses` [INFERRED]
- [[Thread-safe per-module allowblocksanitize counters.]] - `rationale_for` [EXTRACTED]
- [[get_collector()]] - `references` [EXTRACTED]
- [[module_stats.py]] - `contains` [EXTRACTED]
- [[test_block_rate_computed()]] - `calls` [EXTRACTED]
- [[test_empty_module_zero_rate_not_division_error()]] - `calls` [EXTRACTED]
- [[test_module_stats.py]] - `imports` [EXTRACTED]
- [[test_record_and_snapshot()]] - `calls` [EXTRACTED]
- [[test_record_ignores_invalid_decision_safely()]] - `calls` [EXTRACTED]
- [[test_reset()]] - `calls` [EXTRACTED]
- [[test_sanitize_decision()]] - `calls` [EXTRACTED]
- [[test_thread_safe_under_concurrency()]] - `calls` [EXTRACTED]
- [[test_unknown_module_created_on_demand()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ADR-006_Multi-Runtime_Container_Support
