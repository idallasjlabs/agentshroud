---
source_file: "gateway/tests/test_round2_hardening.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L178"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# TestKeyVaultWired

## Connections
- [[.test_keyvault_instantiated_and_seeded_in_lifespan()]] - `method` [EXTRACTED]
- [[.test_pipeline_scans_outbound_for_key_leaks()]] - `method` [EXTRACTED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_round2_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection