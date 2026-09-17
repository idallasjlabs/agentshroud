---
type: community
cohesion: 0.08
members: 25
---

# record_decision

**Cohesion:** 0.08 - loosely connected
**Members:** 25 nodes

## Members
- [[A2AGovernanceProxy._check_peer]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._process]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._sanitize_message]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_inbound]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_outbound]] - code - gateway/security/a2a_governance.py
- [[CredentialInjector.scan_for_credential_leak]] - code - gateway/security/credential_injector.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py
- [[PIISanitizer.block_credentials]] - code - gateway/ingest_api/sanitizer.py
- [[SOC Per-Module Enforcement Heat-Map (SCRUM-80)]] - document - docker/README.md
- [[TokenValidator.validate]] - code - gateway/security/token_validation.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_from_origin]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py
- [[record_decision]] - code - gateway/security/module_stats.py
- [[test_console_source_not_blocked]] - code - gateway/tests/test_block_credentials.py
- [[test_telegram_blocks_password]] - code - gateway/tests/test_block_credentials.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record_decision
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 2 edges to [[_COMMUNITY_A2AMethod]]
- 2 edges to [[_COMMUNITY_load_config()]]
- 1 edge to [[_COMMUNITY_AgentShroud Docker Configuration]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_A2AProxyResult]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[record_decision]] - degree 17, connects to 7 communities
- [[SOC Per-Module Enforcement Heat-Map (SCRUM-80)]] - degree 2, connects to 1 community