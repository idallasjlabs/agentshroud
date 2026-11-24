---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "TestKeyLeakDetection"
location: "L573"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestKeyLeakDetection
---

# TestKeyLeakDetection

## Connections
- [[dot-_make_vault_pipeline()]] - `method` [EXTRACTED]
- [[dot-_passthrough_pii()]] - `method` [EXTRACTED]
- [[dot-test_clean_response_passes_unchanged()_1]] - `method` [EXTRACTED]
- [[dot-test_detector_failure_fails_closed_for_non_owner()]] - `method` [EXTRACTED]
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - `method` [EXTRACTED]
- [[dot-test_key_leak_increments_sanitized_stat_and_audits()]] - `method` [EXTRACTED]
- [[dot-test_stored_key_value_redacted_from_outbound()]] - `method` [EXTRACTED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - `rationale_for` [EXTRACTED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestKeyLeakDetection
