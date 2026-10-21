---
source_file: "gateway/security/egress_filter.py"
type: "code"
community: "First iteration ingests + records; second sees dedup and skips. (2)"
location: "L36"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips_2
---

# EgressAttempt

## Connections
- [[dot-_check_impl()]] - `references` [EXTRACTED]
- [[dot-_record()_1]] - `references` [EXTRACTED]
- [[dot-check()_5]] - `references` [EXTRACTED]
- [[dot-check_async()]] - `references` [EXTRACTED]
- [[dot-get_log()]] - `references` [EXTRACTED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[FakeAuditStore_1]] - `uses` [INFERRED]
- [[TestAuditStorePersistence]] - `uses` [INFERRED]
- [[TestEgressAttempt]] - `uses` [INFERRED]
- [[TestEgressPolicy]] - `uses` [INFERRED]
- [[TestEnforceMode]] - `uses` [INFERRED]
- [[TestIPRules]] - `uses` [INFERRED]
- [[TestInteractiveApproval]] - `uses` [INFERRED]
- [[TestLogging]] - `uses` [INFERRED]
- [[TestMonitorMode]] - `uses` [INFERRED]
- [[TestOpenClawResearchDomainsAllowlisted]] - `uses` [INFERRED]
- [[TestPerAgentPolicy]] - `uses` [INFERRED]
- [[TestSMTPIMAPPorts]] - `uses` [INFERRED]
- [[TestURLParsing]] - `uses` [INFERRED]
- [[egress_filter.py_1]] - `contains` [EXTRACTED]
- [[test_egress_filter.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/First_iteration_ingests__records_second_sees_dedup_and_skips_2
