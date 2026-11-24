---
source_file: "gateway/proxy/pipeline.py"
type: "code"
community: "AuditChain"
location: "L131"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# AuditChain

## Connections
- [[dot-__init__()_180]] - `calls` [EXTRACTED]
- [[dot-__init__()_179]] - `method` [EXTRACTED]
- [[dot-__len__()_1]] - `method` [EXTRACTED]
- [[dot-append()_1]] - `method` [EXTRACTED]
- [[dot-append_block()]] - `method` [EXTRACTED]
- [[dot-append_owner_bypass()]] - `method` [EXTRACTED]
- [[dot-entries()_1]] - `method` [EXTRACTED]
- [[dot-last_hash()_1]] - `method` [EXTRACTED]
- [[dot-test_append_chain()]] - `calls` [EXTRACTED]
- [[dot-test_append_owner_bypass_persists_high_severity()]] - `calls` [EXTRACTED]
- [[dot-test_append_single()]] - `calls` [EXTRACTED]
- [[dot-test_audit_chain_hash_chained()]] - `calls` [EXTRACTED]
- [[dot-test_chain_continuity_preserved_across_wrap()]] - `calls` [EXTRACTED]
- [[dot-test_content_hash_deterministic()]] - `calls` [EXTRACTED]
- [[dot-test_default_window_is_10k()_1]] - `calls` [EXTRACTED]
- [[dot-test_different_content_different_hash()_1]] - `calls` [EXTRACTED]
- [[dot-test_entries_returns_copy()]] - `calls` [EXTRACTED]
- [[dot-test_genesis()]] - `calls` [EXTRACTED]
- [[dot-test_metadata()]] - `calls` [EXTRACTED]
- [[dot-test_persisted_event_records_true_previous_hash()]] - `calls` [EXTRACTED]
- [[dot-test_tamper_in_retained_window_detected()_1]] - `calls` [EXTRACTED]
- [[dot-test_unwrapped_chain_must_anchor_at_genesis()]] - `calls` [EXTRACTED]
- [[dot-test_verify_chain_valid_after_wrap()_1]] - `calls` [EXTRACTED]
- [[dot-test_verify_tampered_chain_hash()]] - `calls` [EXTRACTED]
- [[dot-test_verify_tampered_previous_hash()]] - `calls` [EXTRACTED]
- [[dot-test_verify_valid()]] - `calls` [EXTRACTED]
- [[dot-test_window_capped_at_max_entries()_1]] - `calls` [EXTRACTED]
- [[dot-total_appended()_1]] - `method` [EXTRACTED]
- [[dot-verify_chain()_2]] - `method` [EXTRACTED]
- [[SHA-256 hash chain for tamper-evident audit logging.]] - `rationale_for` [EXTRACTED]
- [[TestAuditChain_1]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestE2E08AuditChainIntegrity]] - `uses` [INFERRED]
- [[audit_chain()]] - `uses` [INFERRED]
- [[pipeline.py_1]] - `contains` [EXTRACTED]
- [[test_audit_chain_empty_valid()]] - `uses` [INFERRED]
- [[test_audit_chain_integrity()]] - `uses` [INFERRED]
- [[test_audit_chain_single_entry()]] - `uses` [INFERRED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_inbound_outbound_both_audited()]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain
