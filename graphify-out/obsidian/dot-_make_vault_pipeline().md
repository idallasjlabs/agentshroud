---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "AuditChain"
location: "L592"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# ._make_vault_pipeline()

## Connections
- [[dot-_passthrough_pii()]] - `calls` [EXTRACTED]
- [[dot-test_clean_response_passes_unchanged()]] - `calls` [EXTRACTED]
- [[dot-test_generic_key_pattern_audited_but_not_blocked()]] - `calls` [EXTRACTED]
- [[dot-test_key_leak_increments_sanitized_stat_and_audits()]] - `calls` [EXTRACTED]
- [[dot-test_stored_key_value_redacted_from_outbound()]] - `calls` [EXTRACTED]
- [[KeyLeakDetector]] - `calls` [EXTRACTED]
- [[KeyVault]] - `calls` [EXTRACTED]
- [[KeyVaultConfig]] - `calls` [EXTRACTED]
- [[SecurityPipeline_2]] - `calls` [EXTRACTED]
- [[TestKeyLeakDetection_1]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain
