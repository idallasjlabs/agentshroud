---
source_file: "gateway/tools/port_manager.py"
type: "code"
community: "Gateway Test Suite"
location: "L85"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# PortManager

## Connections
- [[.__init__()_180]] - `method` [EXTRACTED]
- [[.find_available_port()]] - `method` [EXTRACTED]
- [[.generate_compose_ports()]] - `method` [EXTRACTED]
- [[.is_port_available()]] - `method` [EXTRACTED]
- [[.is_port_available_udp()]] - `method` [EXTRACTED]
- [[.resolve_ports()]] - `method` [EXTRACTED]
- [[.test_all_free_no_conflicts()]] - `calls` [EXTRACTED]
- [[.test_basic_mapping()]] - `calls` [EXTRACTED]
- [[.test_bound_port_is_not_available()]] - `calls` [EXTRACTED]
- [[.test_conflict_auto_resolved()]] - `calls` [EXTRACTED]
- [[.test_conflict_no_auto_resolve()]] - `calls` [EXTRACTED]
- [[.test_duplicate_port_detection()]] - `calls` [EXTRACTED]
- [[.test_finds_base_when_free()]] - `calls` [EXTRACTED]
- [[.test_no_conflict_mapping()]] - `calls` [EXTRACTED]
- [[.test_offset_applied()]] - `calls` [EXTRACTED]
- [[.test_raises_if_no_port_found()]] - `calls` [EXTRACTED]
- [[.test_skips_bound_port()]] - `calls` [EXTRACTED]
- [[.test_skips_excluded_ports()]] - `calls` [EXTRACTED]
- [[.test_udp_bound_not_available()]] - `calls` [EXTRACTED]
- [[.test_udp_unbound_available()]] - `calls` [EXTRACTED]
- [[.test_unbound_port_is_available()]] - `calls` [EXTRACTED]
- [[Detect port conflicts and auto-assign available ports.]] - `rationale_for` [EXTRACTED]
- [[TestFindAvailablePort]] - `uses` [INFERRED]
- [[TestGenerateComposePorts]] - `uses` [INFERRED]
- [[TestIsPortAvailable]] - `uses` [INFERRED]
- [[TestPortResolution]] - `uses` [INFERRED]
- [[TestResolveports]] - `uses` [INFERRED]
- [[check_and_report()]] - `calls` [EXTRACTED]
- [[port_manager.py]] - `contains` [EXTRACTED]
- [[test_port_manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite