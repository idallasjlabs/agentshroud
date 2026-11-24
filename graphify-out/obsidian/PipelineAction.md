---
source_file: "gateway/proxy/pipeline.py"
type: "code"
community: "PipelineAction"
location: "L44"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PipelineAction
---

# PipelineAction

## Connections
- [[Enum_23]] - `inherits` [EXTRACTED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestE2E01PromptGuardBlocking]] - `uses` [INFERRED]
- [[TestE2E05CanaryTripwire]] - `uses` [INFERRED]
- [[TestE2E09SessionIsolation]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPIIBlockModeInPipeline]] - `uses` [INFERRED]
- [[_make_pipeline_result()]] - `uses` [INFERRED]
- [[pipeline.py_1]] - `contains` [EXTRACTED]
- [[str_14]] - `inherits` [EXTRACTED]
- [[test_approval_queue_enforced()]] - `uses` [INFERRED]
- [[test_clamav_pipeline.py]] - `imports` [EXTRACTED]
- [[test_clean_message_passes()]] - `uses` [INFERRED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_egress_allowed_domain()]] - `uses` [INFERRED]
- [[test_egress_blocked()]] - `uses` [INFERRED]
- [[test_inbound_base64_injection_blocked()]] - `uses` [INFERRED]
- [[test_inbound_outbound_both_audited()]] - `uses` [INFERRED]
- [[test_inbound_owner_encoded_injection_allowed()]] - `uses` [INFERRED]
- [[test_kill_switch_freezes()]] - `uses` [INFERRED]
- [[test_mixed_pii_and_injection()]] - `uses` [INFERRED]
- [[test_outbound_pii_stripped()]] - `uses` [INFERRED]
- [[test_pii_stripped_inbound()]] - `uses` [INFERRED]
- [[test_pipeline_clamav_clean_payload()]] - `uses` [INFERRED]
- [[test_pipeline_clamav_error_fail_open()]] - `uses` [INFERRED]
- [[test_pipeline_clamav_malware_blocked()]] - `uses` [INFERRED]
- [[test_pipeline_clamav_not_configured()]] - `uses` [INFERRED]
- [[test_pipeline_short_base64_not_scanned()]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_prompt_injection_blocked()]] - `uses` [INFERRED]
- [[test_telegram_pipeline.py]] - `imports` [EXTRACTED]
- [[test_trust_level_enforced()]] - `uses` [INFERRED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PipelineAction
