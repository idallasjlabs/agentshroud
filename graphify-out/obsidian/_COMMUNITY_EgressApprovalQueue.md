---
type: community
members: 28
---

# EgressApprovalQueue

**Members:** 28 nodes

## Members
- [[dot-_assess_risk()]] - code - gateway/security/egress_approval.py
- [[dot-_check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[dot-_rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[dot-assess_risk()]] - code - gateway/security/egress_approval.py
- [[dot-get_all_rules()]] - code - gateway/security/egress_approval.py
- [[dot-get_decision_log()]] - code - gateway/security/egress_approval.py
- [[dot-get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[dot-get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[dot-log_external_decision()]] - code - gateway/security/egress_approval.py
- [[dot-preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[dot-request_approval()]] - code - gateway/security/egress_approval.py
- [[dot-set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[dot-set_event_bus()_1]] - code - gateway/security/egress_approval.py
- [[Assess risk level for a domainport combination. Returns RiskLevel.GREEN…]] - rationale - gateway/security/egress_approval.py
- [[Check if domain matches an existing rule.]] - rationale - gateway/security/egress_approval.py
- [[EgressApprovalQueue]] - code - gateway/security/egress_approval.py
- [[Enabledisable emergency global egress deny.]] - rationale - gateway/security/egress_approval.py
- [[Get all rules (permanent and session) with scope information.]] - rationale - gateway/security/egress_approval.py
- [[Get emergency block-all state.]] - rationale - gateway/security/egress_approval.py
- [[Get list of pending approval requests.]] - rationale - gateway/security/egress_approval.py
- [[Log an automatic allowdeny from EgressFilter.check() (non-interactive).…]] - rationale - gateway/security/egress_approval.py
- [[Pre-approve known service domains at startup without interactive prompts.…]] - rationale - gateway/security/egress_approval.py
- [[Public risk assessment helper for managementAPI surfaces.]] - rationale - gateway/security/egress_approval.py
- [[Request approval for egress to a domainport. Args domain Target domain port…]] - rationale - gateway/security/egress_approval.py
- [[Return recent approvaldenial decisions (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Set optional event bus for approval telemetry.]] - rationale - gateway/security/egress_approval.py
- [[Thread-safe asyncio queue for managing egress approval requests. Features -…]] - rationale - gateway/security/egress_approval.py
- [[source()]] - code - gateway/tests/test_anthropic_openai_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_EgressRule]]
- 6 edges to [[_COMMUNITY_EgressScope]]
- 6 edges to [[_COMMUNITY_ApprovalMode]]
- 2 edges to [[_COMMUNITY_fixture]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_anthropic_openai_translator.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[EgressApprovalQueue]] - degree 32, connects to 7 communities
- [[source()]] - degree 4, connects to 3 communities
- [[dot-request_approval()]] - degree 7, connects to 2 communities
- [[dot-_check_existing_rule()]] - degree 5, connects to 1 community
- [[dot-_assess_risk()]] - degree 4, connects to 1 community
