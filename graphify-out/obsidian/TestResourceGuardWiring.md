---
source_file: "gateway/tests/test_resource_guard_wiring.py"
type: "code"
community: "LLM Proxy Resource Guard"
location: "L20"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/LLM_Proxy_Resource_Guard
---

# TestResourceGuardWiring

## Connections
- [[.test_setup_resource_guard_returns_real_guard_with_default_limits()]] - `method` [EXTRACTED]
- [[.test_setup_with_custom_limits_overrides_defaults()]] - `method` [EXTRACTED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[ResourceGuard is instantiated at startup and reachable on app_state.]] - `rationale_for` [EXTRACTED]
- [[ResourceLimits]] - `uses` [INFERRED]
- [[test_resource_guard_wiring.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/LLM_Proxy_Resource_Guard